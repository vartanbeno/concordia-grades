FROM selenium/standalone-chrome

USER root

WORKDIR /usr/src/app/

COPY requirements.txt .

RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py && \
    pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "concordia-grades/main.py"]
