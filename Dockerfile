FROM python:3.9-slim
WORKDIR /app

# Copiar requirements antes para otimizar cache e garantir instalação
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY app/ /app/

EXPOSE 8501
CMD ["streamlit", "run", "main.py"]