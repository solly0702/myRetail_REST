FROM python:3.10-slim

LABEL maintainer="solly0702@gmail.com"

RUN apt update && \
    apt install -y --no-install-recommends apt-utils && \
    apt -y upgrade && \
    apt autoremove -y && \
    apt clean -y && \
    apt autoclean -y

RUN mkdir /app
WORKDIR /app

COPY . .

RUN pip --no-cache-dir install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:3003", "manage:app"]