#创建并进入虚拟环境
Python3 -m venv env
cd <项目文件夹>  
cd env 
source bin/activate

#退出虚拟环境
deactivate


pip install mq_http_sdk


MNS  公网 endpoint http(s)://1192351084879509.mns.cn-hangzhou.aliyuncs.com/
    私网  Endpoint ：http://1192351084879509.mns.cn-hangzhou-internal.aliyuncs.com/