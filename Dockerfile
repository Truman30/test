FROM nvidia/cuda:12.3.1-runtime-ubuntu22.04

# 设置工作目录
WORKDIR /app

# 安装 Python 3.11 和 pip
RUN apt update && \
    apt install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa -y && \
    apt update && \
    apt install -y python3.11 python3.11-distutils python3-pip && \
    ln -s /usr/bin/python3.11 /usr/bin/python && \
    ln -s /usr/bin/pip3 /usr/bin/pip

# 复制依赖
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . .

# 启动脚本
CMD ["python", "test.py"]

