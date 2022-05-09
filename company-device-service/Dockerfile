FROM python:3.8-slim

COPY ./company-device-service/app /app
COPY ./company-device-service/entrypoint.sh /entrypoint.sh
COPY ./company-device-service/gunicorn.config.py /gunicorn.config.py
COPY ./company-device-service/requirements.txt /requirements.txt
COPY ./company-device-service/scripts /scripts
COPY ./company-device-service/ca-certificate.crt /ca-certificate.crt
COPY ./schemas /schemas

RUN apt-get update && \
    apt-get install -y \
        build-essential \
        python3-dev \
        python3-setuptools \
        tesseract-ocr \
        make \
        gcc \
    && python3 -m pip install -r requirements.txt \
    && apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

RUN chmod +x entrypoint.sh

CMD [ "./entrypoint.sh" ]