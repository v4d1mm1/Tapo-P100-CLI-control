# Tapo-P100-CLI-control
Script for controlling Tapo P100 smart sockets by TP-Link from CLI.

## Usage
Edit P100.py to add your Tapo P100 IP address and Tapo account login credentials.
```bash
python3 p100.py (on/off/state) (optional timeout) 
```
## Example:
```bash
python3 p100.py off 30
```
Will switch the device off after 30 minutes.

If arguments are not specified device will be switched to opposite state.
Time can be set in MM or HH:MM format.

You can make this file executable and add variable $PATH by typing in CLI commands "chmod +х p100.py" and "PATH=$PATH:." or edit /etc/environment file.

Requires [Tapo P100 library](https://github.com/fishbigger/TapoP100) by [fishbigger](https://github.com/fishbigger).
