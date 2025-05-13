#build image
FROM python:3.13-slim

  # No __pycache__ directories are created.
ENV PYTHONDONTWRITEBYTECODE=1

  #error go to the cmd
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt  .


RUN pip3 install --upgrade pip

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

RUN python3 manage.py collectstatic --noinput

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]