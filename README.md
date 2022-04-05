# P100 on Repetier Server

## You need
* Tapo P100
* Repetier Server
* Login to you TP-Link Tapo Account

## You need to install a python lib


```bash
sudo su
apt-get install python3-pip
pip3 install PyP100
```

If you need more information about lib look here:

https://github.com/fishbigger/TapoP100

## Edit python files

Use Login from tp-link tapo app.
Use the ip-adress from p100

* host
* username
* password

## Copy Files to Server

* /var/lib/Repetier-Server/scripts/tapo_on.py
* /var/lib/Repetier-Server/scripts/tapo_off.py

## Change User of files

```bash
sudo su
chown repetierserver:root /var/lib/Repetier-Server/scripts/tapo_o*.py
```

## Edit extcommands.xml

Edit /var/lib/Repetier-Server/database/extcommands.xml
and add following:

```xml
<execute name="printer_off" allowParams="false" sync="false">python3 /var/lib/Repetier-Server/scripts/tapo_off.py</execute>
<execute name="printer_on" allowParams="false" sync="false">python3 /var/lib/Repetier-Server/scripts/tapo_on.py</execute>
```

## Use command in repetierserver

its quite easy, just run as gcode, you could also add it to your gcode after finishing print:

`@execute printer_off`

or

`@execute printer_on`
