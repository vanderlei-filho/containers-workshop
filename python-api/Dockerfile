# --- Build the deployment container
FROM centos:centos8

# Declare non-root runtime appuser
RUN useradd appuser

# Update CentOS, build Python3 from source
RUN yum groupinstall -y "Development Tools" && \
    yum install -y \
        wget \
        openssl-devel \
        libffi-devel \
        pcre \
        pcre-devel \
        gcc-c++ \
        make && \
    wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tar.xz && \
    tar -xJf Python-3.9.6.tar.xz && \
    cd Python-3.9.6 && \
    ./configure && \
    make && \
    make install

# Set work directory
WORKDIR /usr/src/flask_backend

# Set Flask-related environment variables
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV FLASK_APP=flask_server.py

# Copy the Python requirements.txt file
COPY ./requirements.txt /usr/src/flask_backend/requirements.txt

# Create a virtual Python environment
RUN python3 -m venv env && \
    source env/bin/activate

# Install pip packages
RUN pip3 install --upgrade pip && \
    pip3 install wheel --no-cache-dir && \
    pip3 install -r ./requirements.txt --no-cache-dir

# Copy Flask source code
COPY . /usr/src/flask_backend

# Chown all the files to the appuser
RUN chown -R appuser:appuser /usr/src/flask_backend
RUN chmod a+x boot.sh

# Change to the app user
USER appuser

# Document exposed PORTs
EXPOSE 5000

# Run boot script
CMD ["./boot.sh"]
