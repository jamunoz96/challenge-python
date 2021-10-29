FROM ubuntu:latest
RUN apt-get update && apt-get --assume-yes install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa && apt-get install -y python3-lxml