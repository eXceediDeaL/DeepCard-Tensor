# DeepCard

Front-end for DeepCard.

# Dependences

1. .NET Core 2.2 See [here](https://dotnet.microsoft.com/download/linux-package-manager/rhel/sdk-current) to install it on Linux.

# Usage

Use different shells to run these command, because they need long-run.

1. Start the virtual API server

```sh
dotnet run -p ./src/DeepCard.API
```

2. Start the website host server

```sh
dotnet run -p ./src/DeepCard.Host
```

Then visit the URL `http://localhost:60000`. You can see the website.