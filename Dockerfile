# Use Ubuntu 22.04 as the base image
FROM ubuntu:22.04

# Update package lists and install required packages
RUN apt-get update && \
    apt-get install -y \
        unzip \
        libc6 \
        libglib2.0-0 \
        libnss3 \
        libnspr4 \
        libx11-6 \
        libgcc-s1 \
        libpcre3 \
        libxcb1 \
        libxau6 \
        libxdmcp6 \
        libbsd0 \
        libmd0 \
        xvfb \
        wget \    
        python3 \
        python3-pip \
        python3.10-venv \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Chrome browser
RUN wget https://dl-ssl.google.com/linux/linux_signing_key.pub -O /tmp/google.pub && \
    gpg --no-default-keyring --keyring /etc/apt/keyrings/google-chrome.gpg --import /tmp/google.pub && \
    echo 'deb [arch=amd64 signed-by=/etc/apt/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install google-chrome-stable -y


# Download ChromeDriver using wget
RUN wget https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.69/linux64/chromedriver-linux64.zip && \
    unzip chromedriver-linux64.zip && \
    cd chromedriver-linux64 && \
    mv chromedriver /usr/local/bin/

WORKDIR app

# Install Python libraries
COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY . . 

ENTRYPOINT ["python3", "app.py"]
