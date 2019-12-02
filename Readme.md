# sBacklight
sBacklight is a client + server application which manages the backlight levels of the default screen.

# Usage
* clone the repository
* copy backlight-server.py somewhere safe, owned by root
* set up service for backlight-server
Example:
`
[Unit]
Description=Backlight server which handles backlight
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=root
ExecStart=python /root/backlight-server.py

[Install]
WantedBy=multi-user.target
`

* enable service `systemctl enable --now backlight-server.service`
* alias sbacklight `alias sbacklight="python3 {your-directory}/backlight.py"`

## Commands:
 - `sbacklight set 10` sets the backlight strength to 10%
 - `sbacklight inc 5` increases the backlight strength by 5%
 - `sbacklight dec 5` decreases the backlight strength by 5%
