# 使用 Python 3.12 作为基础镜像,每次编译需要安装库,用pythonlocal:3.9 本地下好库直接使用
FROM python:3.12

LABEL authors="Barry"

 # 设置工作目录
WORKDIR /app
 # 将当前目录下的所有文件复制到容器的 /app 目录下
COPY . /app
 # 安装依赖
RUN pip install --no-cache-dir -r requirements.txt --trusted-host pypi.douban.com
 # 暴露容器的 8000 端口
EXPOSE 8000
 # 运行应用
CMD ["python", "main.py"]

