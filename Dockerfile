FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install streamlit


COPY main.py .

EXPOSE 8502

CMD ["streamlit", "run", "main.py", "--browser.serverPort=80", "--browser.serverAddress=amag.caprover.srivastsh.com"]
