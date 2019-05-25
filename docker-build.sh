cd ./src/DeepCard.Host
dotnet publish -c Release -r linux-x64

cd ../../
docker build -t deepcard:cpu -f ./docker/cpu/Dockerfile .
docker build -t deepcard:gpu -f ./docker/gpu/Dockerfile .