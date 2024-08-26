FROM python:3.12.2
LABEL authors="yaroslavvagilevich"
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]