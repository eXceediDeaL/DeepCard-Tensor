# DeepCard

![](https://img.shields.io/badge/platform-linux-blue.svg) ![](https://img.shields.io/github/license/StardustDL/DeepCard.svg) ![](https://img.shields.io/github/repo-size/StardustDL/DeepCard.svg) ![](https://img.shields.io/librariesio/github/StardustDL/DeepCard.svg)

![](https://img.shields.io/docker/pulls/stardustdl/deepcard.svg)

A bank card number recognition system based on deep-learning.

# Usage

## Docker

### Pull Image

1. Pull and run from Docker Hub.

```sh
docker run -it --rm -p 8000:80 --name dc stardustdl/deepcard:cpu
```

2. Visit URL `http://localhost:8000` to see DeepCard website.

### Rebuild Image

1. Build DeepCard.Host (needs .NET Core SDK):

```sh
cd ./src/DeepCard.Host
dotnet publish -c Release -r linux-x64
```

2. Build docker image:

```sh
docker build -t deepcard:cpu -f ./docker/cpu/Dockerfile .
```

2. Start docker container (will use more than 3GB memory):

```sh
docker run -it --rm -p 8000:80 --name dc deepcard:cpu
```

4. Visit URL `http://localhost:8000` to see DeepCard website.

## Host

If you want to run directly on the host, use this method.

1. Install dependences:

```sh
chmod +x ./build.sh
./build.sh
```

If you need to build GUI from the source code, you need to install .NET Core SDK first. These commands are commentted in `build.sh`.

2. Run the server:

```sh
chmod +x ./run.sh
./run.sh
```

3. Visit URL `http://localhost:8000` to see DeepCard website.

# Development

Use different shells to run these command, because they need long-run.

1. Copy the trained models to the directories. Or copy `src/DeepCard.API/server.py` to the independent OCR directory, and run the file there.

2. Start the OCR API server.

```sh
cd ./src/DeepCard.API ; python server.py
```

3. Start the website host server

```sh
dotnet run -p ./src/DeepCard.Host
```

Then visit the URL `http://localhost:5000`. You can see the website.

> **Hints**: If you want to debug host without real OCR, start the demo API server with command: `dotnet run -p ./src/DeepCard.API.Demo --urls="http://localhost:4000"`

## Dependences

1. Python
2. OpenCV
3. Tensorflow
4. Pytorch
5. .NET Core 2.2. (See [here](https://dotnet.microsoft.com/download/linux-package-manager/rhel/sdk-current) to install it on Linux.)
