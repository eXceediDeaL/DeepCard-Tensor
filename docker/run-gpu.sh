#! /bin/sh

cd /src/ocr

chmod +x ./ctpn/lib/utils/make.sh
cd ./ctpn/lib/utils/ && ./make.sh

cd /src/gui
./DeepCard.Host &

cd /src/ocr
python3 server.py
