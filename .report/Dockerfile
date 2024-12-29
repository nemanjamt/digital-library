FROM python:3.9.21

WORKDIR /app

COPY . .

RUN pip install fpdf && pip install requests

CMD ["tail", "-f", "/dev/null"]
