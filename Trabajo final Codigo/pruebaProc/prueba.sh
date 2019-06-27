#!/bin/bash

echo "compilando modulo..."
make

echo "instalando modulo..."
sudo insmod hello.ko

sudo su

echo "mensaje 2" > /proc/hello
echo "mensaje 2" > /proc/hello

echo "mostrando logs del modulo..."
cat /var/log/kern.log

echo "quitando modulo..."
sudo rmmod hello.ko

echo "mostrando logs del modulo..."
cat /var/log/kern.log