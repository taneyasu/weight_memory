FROM python:3.8-slim
WORKDIR /prj/work
COPY requirements.txt ${PWD}
RUN apt update -y
RUN apt install git -y
RUN pip install -r requirements.txt