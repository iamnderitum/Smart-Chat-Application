FROM python:3.12
LABEL maintainter="blackuser.com"

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

#ENV PATH="/py/bin:$PATH"
WORKDIR /chatapp


# COPY ./requirements.txt /tmp/requirements.txt
# COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY requirements.dev.txt /chatapp/requirements.dev.txt
COPY requirements.txt /chatapp/requirements.txt


RUN apt-get update && apt-get install -y build-essential libpq-dev python3-venv

# Install dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . /chatapp/

#Setup the application
#ARG DEV=false

#RUN python -m venv /py && \
    #/py/bin/pip install -r /tmp/requirements.txt && \
    #apt-get install -y postgresql-client && \
    # if ["$DEV" = "true"]; \
        #then /py/bin/pip install -r /tmp/requirements.dev.txt;\
    # fi && \
    # rm -rf /tmp && \

# Create a user & Switch to non-root user
RUN adduser --disabled-password \
        --no-create-home \
        django-user &&\
    chown -R django-user:django-user /chatapp


USER django-user

EXPOSE 8000

CMD ["python", "chatapp/manage.py", "runserver", "0.0.0.0:8000"]
