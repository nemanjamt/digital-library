FROM python:3.9.21

WORKDIR /app

COPY . .

RUN chmod +x .report/wait-for-services.sh

RUN pip install fpdf && pip install requests

CMD ["tail", "-f", "/dev/null"]
