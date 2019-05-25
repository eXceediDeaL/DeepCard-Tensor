pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

/usr/bin/yes | pip install https://download.pytorch.org/whl/cpu/torch-1.1.0-cp36-cp36m-linux_x86_64.whl https://download.pytorch.org/whl/cpu/torchvision-0.3.0-cp36-cp36m-linux_x86_64.whl 
/usr/bin/yes | pip install numpy scipy matplotlib pillow
/usr/bin/yes | pip install easydict opencv-python keras h5py PyYAML
/usr/bin/yes | pip install cython==0.24
/usr/bin/yes | pip install tensorflow==1.3.0

pip install --no-cache-dir tensorflow==1.3.0

chmod +x ./ctpn/lib/utils/make_cpu.sh
cd ./ctpn/lib/utils/ && ./make_cpu.sh
