# Gerador de conteúdo (Streamlit)

Aplicação Streamlit que gera textos otimizados para SEO com base em tema, plataforma, tom e outras preferências. Usa um provedor de LLM via LangChain.

## Como rodar localmente
- Pré-requisitos: `Python 3.9+` e `pip`.
- Instale dependências: `pip install -r requirements.txt`.
- Crie um arquivo `.env` em `app/.env` com a variável `GROQ_API_KEY` e, opcionalmente, `MODEL_ID`.
- Execute: `streamlit run app/main.py`.

## Docker
- Build e subir com Compose: `docker-compose up --build`.
- O serviço expõe `http://localhost:8501`.
- O `docker-compose.yml` carrega automaticamente `app/.env`.

## Publicação na Streamlit Cloud
- Suba o repositório para o GitHub.
- Na configuração do app, defina o arquivo de entrada como `app/main.py`.
- Em `Secrets`, adicione `groq_api_key` (e opcionalmente `MODEL_ID`).
- As secrets são integradas automaticamente pelo app (`st.secrets`).

## Publicação em Hostinger (VPS)
- Use um VPS com Docker e docker-compose.
- Clone o repositório e rode `docker-compose up -d --build`.
- Configure domínio e HTTPS com Nginx/Caddy como reverse proxy apontando para `8501`.

## Observações
- O `Dockerfile` instala dependências via `requirements.txt` e copia o código em `/app`.
- Para melhor UX, considere usar `st.form`, validações dos campos obrigatórios e `st.spinner` durante a geração.