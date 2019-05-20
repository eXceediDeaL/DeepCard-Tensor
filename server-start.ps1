if ($args.Count -eq 0) {
    Write-Output "Please input type."
}
else {
    switch ($args[0]) {
        "api" {
            dotnet run -p ./src/DeepCard.API
        }
        "host" {
            dotnet run -p ./src/DeepCard.Host
        }
        default {
            Write-Output "The type is not found."
        }
    }
}