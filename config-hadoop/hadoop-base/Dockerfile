# Base Image
FROM ubuntu:22.04

# Set root password
RUN echo "root:root" | chpasswd

# Update and install required packages
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y openjdk-8-jdk wget ssh openssh-server dos2unix vim sudo telnet iputils-ping && \
    apt-get clean

# Set environment variables
ENV JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64
ENV HADOOP_HOME=/home/dlhweather/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$JAVA_HOME/bin

# Create user dlhweather
RUN adduser --disabled-password --gecos "" dlhweather && \
    echo "dlhweather:dlhweather" | chpasswd && \
    usermod -aG sudo dlhweather && \
    echo "dlhweather ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Install Hadoop
USER dlhweather

WORKDIR /home/dlhweather
RUN wget https://dlcdn.apache.org/hadoop/common/hadoop-3.4.1/hadoop-3.4.1.tar.gz && \
    tar -xzf hadoop-3.4.1.tar.gz && \
    mv hadoop-3.4.1 hadoop && \
    rm hadoop-3.4.1.tar.gz

# Set JAVA_HOME in hadoop-env.sh
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64" >> /home/dlhweather/hadoop/etc/hadoop/hadoop-env.sh
    

# Copy Hadoop configuration files
COPY .bashrc /home/dlhweather/.bashrc

RUN mkdir -p /home/dlhweather/.ssh && \
    ssh-keygen -t rsa -P '' -f /home/dlhweather/.ssh/id_rsa && \
    cat /home/dlhweather/.ssh/id_rsa.pub >> /home/dlhweather/.ssh/authorized_keys && \
    chmod 600 /home/dlhweather/.ssh/authorized_keys && \
    chown -R dlhweather:dlhweather /home/dlhweather/.ssh

# Add permission to ssh folder and keys
USER root

# Convert files to Unix format
RUN dos2unix /home/dlhweather/.bashrc 

# Expose ports
EXPOSE 9000 50070 9001 9002 9003 9004 9005 9006 9870 9864 8088 8042
