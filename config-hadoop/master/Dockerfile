# Base Image
FROM hadoop-base1

USER dlhweather
WORKDIR /home/dlhweather

# Copy Hadoop configuration files
COPY config/core-site.xml /home/dlhweather/hadoop/etc/hadoop/core-site.xml
COPY config/hdfs-site.xml /home/dlhweather/hadoop/etc/hadoop/hdfs-site.xml
COPY config/mapred-site.xml /home/dlhweather/hadoop/etc/hadoop/mapred-site.xml
COPY config/yarn-site.xml /home/dlhweather/hadoop/etc/hadoop/yarn-site.xml

USER root
# Convert files to Unix format
RUN dos2unix /home/dlhweather/hadoop/etc/hadoop/core-site.xml && \
    dos2unix /home/dlhweather/hadoop/etc/hadoop/hdfs-site.xml && \
    dos2unix /home/dlhweather/hadoop/etc/hadoop/yarn-site.xml && \
    dos2unix /home/dlhweather/hadoop/etc/hadoop/mapred-site.xml

# Format HDFS
USER dlhweather
RUN hdfs namenode -format

USER root
# Start SSH and Hadoop services
CMD ["/bin/bash", "-c", "service ssh start && su - dlhweather && bash"]
