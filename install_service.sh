sudo cp shodan_say.service /etc/systemd/system/
sudo chmod 644 /etc/systemd/system/shodan_say.service
sudo systemctl daemon-reload
sudo systemctl enable shodan_say
sudo systemctl start shodan_say
sudo systemctl status shodan_say
