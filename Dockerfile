#optimized version, originaly from https://github.com/dimmg/dockselpy/blob/master/Dockerfile
FROM ubuntu:bionic

COPY docker/docker-entrypoint.sh /docker-entrypoint.sh

WORKDIR /tests

ADD . /tests

#ENV PYTHONPATH "${PYTHONPATH}:/tests"

RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 \
&&  pip3 install --trusted-host pypi.python.org -r requirements.txt \
&&  apt-get install default-jre -y

VOLUME ["/tests/allure","/tests/allure-report","/tests/report"]
ENTRYPOINT ["bash","/docker-entrypoint.sh"]