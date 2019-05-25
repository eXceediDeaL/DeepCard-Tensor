cd /src/gui
chmod +x ./DeepCard.Host
./DeepCard.Host --urls="http://localhost:8000" &

cd /src/ocr
python3 server.py
