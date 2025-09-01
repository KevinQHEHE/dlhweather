# Base Image
FROM hadoop-base1

USER root
# Copy Hadoop configuration files
COPY config/core-site.xml /home/dlhweather/hadoop/etc/hadoop/core-site.xml
COPY config/hdfs-site.xml /home/dlhweather/hadoop/etc/hadoop/hdfs-site.xml
COPY config/yarn-site.xml /home/dlhweather/hadoop/etc/hadoop/yarn-site.xml

# Convert files to Unix format
RUN dos2unix /home/dlhweather/hadoop/etc/hadoop/core-site.xml && \
    dos2unix /home/dlhweather/hadoop/etc/hadoop/hdfs-site.xml && \
    dos2unix /home/dlhweather/hadoop/etc/hadoop/yarn-site.xml

# Đảm bảo thư mục .ssh và authorized_keys tồn tại, quyền đúng
RUN mkdir -p /home/dlhweather/.ssh && \
    chmod 700 /home/dlhweather/.ssh && \
    touch /home/dlhweather/.ssh/authorized_keys && \
    chmod 600 /home/dlhweather/.ssh/authorized_keys && \
    chown -R dlhweather:dlhweather /home/dlhweather/.ssh

# Xóa known_hosts khi khởi động để tránh lỗi SSH key
CMD ["/bin/bash", "-c", "rm -f /home/dlhweather/.ssh/known_hosts && service ssh start && su - dlhweather && bash"]
