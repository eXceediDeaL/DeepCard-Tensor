#! /bin/sh

cd /src/ocr

chmod +x ./ctpn/lib/utils/make_cpu.sh
cd ./ctpn/lib/utils/ && ./make_cpu.sh

cd /src/gui
./DeepCard.Host &

cd /src/ocr
python3 server.py

