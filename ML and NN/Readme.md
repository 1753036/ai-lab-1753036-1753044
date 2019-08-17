sudo brew install python3-pip
pip3 install virtualenv         // Tạo môi trường ảo
mkdir keras_env
virtualenv -p python3 ./keras_env
source ./keras_env/bin/activate

pip install tensorflow --upgrade
pip install keras
pip show keras // Kiểm tra cài đặt keras thành công chưa