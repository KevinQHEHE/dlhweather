# Base Image
FROM hadoop-base1

USER root
# Copy Hadoop configuration files
COPY config/core-site.xml /home/hadoopdlhweather/hadoop/etc/hadoop/core-site.xml
COPY config/hdfs-site.xml /home/hadoopdlhweather/hadoop/etc/hadoop/hdfs-site.xml
COPY config/yarn-site.xml /home/hadoopdlhweather/hadoop/etc/hadoop/yarn-site.xml

# Convert files to Unix format
RUN dos2unix /home/hadoopdlhweather/hadoop/etc/hadoop/core-site.xml && \
    dos2unix /home/hadoopdlhweather/hadoop/etc/hadoop/hdfs-site.xml && \
    dos2unix /home/hadoopdlhweather/hadoop/etc/hadoop/yarn-site.xml

# Đảm bảo thư mục .ssh và authorized_keys tồn tại, quyền đúng
RUN mkdir -p /home/hadoopdlhweather/.ssh && \
    chmod 700 /home/hadoopdlhweather/.ssh && \
    touch /home/hadoopdlhweather/.ssh/authorized_keys && \
    chmod 600 /home/hadoopdlhweather/.ssh/authorized_keys && \
    chown -R hadoopdlhweather:hadoopdlhweather /home/hadoopdlhweather/.ssh

# Xóa known_hosts khi khởi động để tránh lỗi SSH key
CMD ["/bin/bash", "-c", "rm -f /home/hadoopdlhweather/.ssh/known_hosts && service ssh start && su - hadoopdlhweather && bash"]
