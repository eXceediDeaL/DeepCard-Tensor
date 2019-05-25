FROM mcr.microsoft.com/dotnet/core/aspnet:2.2-bionic

COPY ./docker/apt-sources /etc/apt/sources.list

RUN mkdir /src && apt clean && apt update --fix-missing && apt install -y python3 python3-pip libsm6 libxrender1 libxext-dev && \
    rm -rf /var/lib/apt/lists/* && \
    pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U

# COPY ./src/DeepCard.Host /src/gui
COPY ./src/DeepCard.Host/bin/Release/netcoreapp2.2/linux-x64/publish /src/gui

COPY ./src/DeepCard.API /src/ocr

COPY ./docker/run-gpu.sh /src/run.sh

RUN cd /src/ocr && chmod +x ./env-gpu.sh && ./env-gpu.sh && cd /src && chmod +x ./run.sh

WORKDIR /src

# ENTRYPOINT [ "/bin/bash" ]

ENTRYPOINT [ "run.sh" ]
