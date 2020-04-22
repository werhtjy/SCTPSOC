# SCTPSOC
sctp soc. Very simple

Requirements

$ sudo apt-get install lksctp-tools
Usage:

# Для машины, которая получает данные:

Установка скрипта
$ git clone https://github.com/werhtjy/SCTPSOC.git

Запуск скрипта
$ cd SCTPSOC/
$ sudo python3 script.py

# Для машины, которая отправляет данные:
Запуск процесса
$ sctp_darn -H <self IP-adress> -P <self port>  -h <slaves IP>  -p <open slave's port> --send

License: MIT

Copyright © werhtjy 2020
