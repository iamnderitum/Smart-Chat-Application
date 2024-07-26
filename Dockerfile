FROM python:3.12 
LABEL maintainter="blackuser.com"

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

#ENV PATH="/py/bin:$PATH"
WORKDIR /chatapp

# Install dependencies
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

#COPY requirements.txt /chatapp/chatapp/
# Install build tools
RUN apt-get update && apt-get install -y build-essential libpq-dev

RUN pip install  --upgrade pip \
    && pip install --no-cache-dir -r /tmp/requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt
ARG DEV=false

#RUN python -m venv /py &&\
    #/py/bin/pip install -r /tmp/requirements.txt && \
    #if ["$DEV" = "true"]; then /py/bin/pip install -r /tmp/requirements.dev.txt; fi && \
    #rm -rf /tmp && \
    #adduser\
        #--disabled-password \
        #--no-create-home \
        #django-user &&\
    #chown -R django-user:django-user /chatapp

# Add the rest of the application 
COPY . /chatapp/
# ENV PATH="/py/bin:$PATH"

# Switch to non-root user
RUN adduser --disabled-password --no-create-home django-user
RUN chown -R django-user:django-user /chatapp
USER django-user


# Command to run the application
CMD ["python", "chatapp/manage.py", "runserver", "0.0.0.0:8000"]
