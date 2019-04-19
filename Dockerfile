FROM selenium/standalone-chrome

USER root

WORKDIR /usr/src/app/

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y python3-distutils && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py && \
    pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "concordia-grades/main.py"]
