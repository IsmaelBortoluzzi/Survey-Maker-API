FROM python:3.10.10-bullseye

ADD . /app

# NGINX
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN /usr/sbin/nginx -c /etc/nginx/sites-available/default -g "pid /var/run/nginx.pid; worker_processes 2;"

WORKDIR /app

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "surveymaker.wsgi:application"]