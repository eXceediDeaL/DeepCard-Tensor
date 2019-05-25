if ($args.Count -eq 0) {
    Write-Output "Please input type."
}
else {
    switch ($args[0]) {
        "api" {
            cd ./src/DeepCard.API ; python server.py
        },
        "api.demo" {
            dotnet run -p ./src/DeepCard.API.Demo --urls="http://localhost:4000"
        }
        "host" {
            dotnet run -p ./src/DeepCard.Host --urls="http://localhost:8000"
        }
        default {
            Write-Output "The type is not found."
        }
    }
}