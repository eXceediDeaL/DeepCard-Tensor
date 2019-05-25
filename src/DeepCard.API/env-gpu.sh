pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

pip install --no-cache-dir -r requirements.txt

pip install --no-cache-dir tensorflow-gpu==1.3.0

chmod +x ./ctpn/lib/utils/make.sh
cd ./ctpn/lib/utils/ && ./make.sh
