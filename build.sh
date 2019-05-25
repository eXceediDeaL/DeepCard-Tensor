mkdir /src

cp -f ./docker/apt-sources /etc/apt/sources.list

apt clean
apt update --fix-missing
apt install -y python3 python3-pip libsm6 libxrender1 libxext-dev
pip3 install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U

cd ./src/DeepCard.API
chmod +x ./env-cpu.sh
./env-cpu.sh

cd ../..

# wget -q https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb
# dpkg -i packages-microsoft-prod.deb
# add-apt-repository universe
# apt install -y apt-transport-https
# apt update
# apt install -y dotnet-sdk-2.2

cd ./src/DeepCard.Host
# dotnet publish -c Release -r linux-x64

cd ../..

cp -r ./src/DeepCard.Host/bin/Release/netcoreapp2.2/linux-x64/publish /src/gui

cp -r ./src/DeepCard.API /src/ocr
