# DeepCard

A bank card number recognition system based on deep-learning.

# Dependences

1. Python
2. Tensorflow
3. Pytorch
4. .NET Core 2.2. (See [here](https://dotnet.microsoft.com/download/linux-package-manager/rhel/sdk-current) to install it on Linux.)

# Usage

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

Then visit the URL `http://localhost:60000`. You can see the website.

> **Hints**: If you want to debug host without real OCR, start the demo API server with command: `dotnet run -p ./src/DeepCard.API.Demo`