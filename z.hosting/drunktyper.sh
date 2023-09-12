#!/bin/sh

if [ $1 = "stop" ]; then
    echo -ne "\n waitress:\n"
    ps | grep waitress
    pkill waitress
    ps | grep waitress
    echo -ne "\n ngrok:\n"
    ps | grep ngrok
    pkill ngrok
    ps | grep ngrok
elif [ $1 = "update" ]; then
    ./$0 stop
    cd /volume1/Web/
    wget https://github.com/KoleckOLP/DrunkTyper/archive/refs/heads/master.zip
    rm -r DrunkTyper-master
    unzip master.zip
    rm master.zip
    cd ~
    ./$0
else
    export PATH=$PATH:/usr/local/AppCentral/python3/bin
    cd /volume1/Web/DrunkTyper-master
    nohup waitress-serve --host 0.0.0.0 --port 5000 main:app &
    nohup ngrok http --domain=adder-enormous-formally.ngrok-free.app 5000 &
    echo -ne "\n"
fi
