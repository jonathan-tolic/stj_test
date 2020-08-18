FROM ubuntu:18.04
CMD apt-get update && apt-get install python3 python3-pip git -y && pip3 install flask && cd /root/ && git clone https://github.com/jonathan-tolic/stj_test.git && cd stj_test && python3 main.py
