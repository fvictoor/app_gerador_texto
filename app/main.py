import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()

# Integrar secrets do Streamlit, quando disponíveis (Cloud)
try:
    groq_key = st.secrets.get("groq_api_key")
    if groq_key:
        os.environ["GROQ_API_KEY"] = groq_key
    model_id_secret = st.secrets.get("MODEL_ID")
    if model_id_secret:
        os.environ["MODEL_ID"] = model_id_secret
except Exception:
    pass

# Conexão com a LLM
id_model = os.getenv("MODEL_ID", "llama-3.3-70b-versatile")  # Valor padrão caso não esteja no .env
llm = ChatGroq(
    model=id_model,
    temperature=0.7,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# Função de geração
def llm_generate(llm, prompt):
    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um especialista em marketing digital com foco em SEO e escrita persuasiva."),
        ("human", "{prompt}"),
    ])

    chain = template | llm | StrOutputParser()

    res = chain.invoke({"prompt": prompt})
    return res

st.set_page_config(page_title="Gerador de conteúdo 🤖", page_icon="🤖")
st.title("Gerador de conteúdo")

# Campos do formulário
topic = st.text_input("Tema:", placeholder="Ex: saúde mental, alimentação saudável, prevenção, etc.")
platform = st.selectbox("Plataforma:", ['Instagram', 'Facebook', 'LinkedIn', 'Blog', 'E-mail'])
tone = st.selectbox("Tom:", ['Normal', 'Informativo', 'Inspirador', 'Urgente', 'Informal'])
length = st.selectbox("Tamanho:", ['Curto', 'Médio', 'Longo'])
audience = st.selectbox("Público-alvo:", ['Geral', 'Jovens adultos', 'Famílias', 'Idosos', 'Adolescentes'])
cta = st.text_input("Chamada para Ação (CTA):", placeholder="Ex: Clique para aproveitar a promoção!")
hashtags = st.checkbox("Retornar Hashtags")
emogi = st.checkbox("Incluir Emojis")
keywords = st.text_area("Palavras-chave (SEO):", placeholder="Ex: bem-estar, medicina preventiva...")

if st.button("Gerar conteúdo"):
    prompt = f"""
    Escreva um texto com SEO otimizado sobre o tema '{topic}'.
    Retorne em sua resposta apenas o texto final e não inclua ela dentro de aspas.
    - Onde será publicado: {platform}.
    - Tom: {tone}.
    - Público-alvo: {audience}.
    - Comprimento: {length}.
    - {f"Inclua ao final do texto esta chamada para ação:" + cta if cta else "Não inclua chamada para ação."}
    - {"Retorne ao final do texto hashtags relevantes." if hashtags else "Não inclua hashtags."}
    - {"Inclua emojis relevantes ao longo do texto." if emogi else "Não inclua emojis."}
    {"- Palavras-chave que devem estar presentes nesse texto (para SEO): " + keywords if keywords else ""}
    """
    try:
        res = llm_generate(llm, prompt)
        st.markdown(res)
    except Exception as e:
        st.error(f"Erro: {e}")