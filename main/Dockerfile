FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

# CMD ["flask", "manager.py", "runserver"]
# CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
