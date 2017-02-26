# CPU temperature fan control

Per installare:

sudo -s<br>
cd /var/www/MyScripts<br>
git clone https://github.com/amorospo/FanCtrl.git<br>
mv FanCtrl/FanCtrl.service /etc/systemd/system/FanCtrl.service<br>
nano /var/www/MyScripts/FanCtrl.py

e modificare le variabili a proprio piacimento (pin, temperature max e min)<br>

Successivamente bisogna abilitare e far partire il servizio all'avvio del sistema:

sudo systemctl enable FanCtrl<br>
sudo systemctl start FanCtrl<br>

e poi un bel riavvio del sistema (non necessario, giusto per vedere se tutto funziona al riavvio)

shutdown -r now<br>
