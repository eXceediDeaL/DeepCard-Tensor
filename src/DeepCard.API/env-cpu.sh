pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

pip install -r requirements.txt

pip install tensorflow==1.3.0

chmod +x ./ctpn/lib/utils/make_cpu.sh
cd ./ctpn/lib/utils/ && ./make_cpu.sh
