FROM python:3.14.4

WORKDIR /app

COPY app.py .

EXPOSE 5000

CMD ["sh", "-c", "5000"]
