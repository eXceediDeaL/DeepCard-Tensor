cython bbox.pyx
cython cython_nms.pyx
python3 setup_cpu.py build_ext --inplace
mv utils/* ./
rm -rf build
rm -rf utils

