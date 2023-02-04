FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install streamlit


COPY main.py .

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.enableCORS=false", "--server.enableWebsocketCompression=false"]
