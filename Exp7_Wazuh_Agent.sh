#!/bin/bash

WAZUH_MANAGER_IP="10.0.0.2"

echo "=== Installing Prerequisites ==="
sudo apt-get update
sudo apt-get install -y gnupg apt-transport-https curl

echo "=== Importing Wazuh GPG Key ==="
curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | \
sudo gpg --no-default-keyring \
--keyring gnupg-ring:/usr/share/keyrings/wazuh.gpg --import
sudo chmod 644 /usr/share/keyrings/wazuh.gpg

echo "=== Adding Wazuh Repository ==="
echo "deb [signed-by=/usr/share/keyrings/wazuh.gpg] https://packages.wazuh.com/4.x/apt/ stable main" | \
sudo tee /etc/apt/sources.list.d/wazuh.list

sudo apt-get update

echo "=== Installing Wazuh Agent ==="
sudo WAZUH_MANAGER="$WAZUH_MANAGER_IP" apt-get install -y wazuh-agent

echo "=== Enabling and Starting Service ==="
sudo systemctl enable --now wazuh-agent

echo "=== Checking Service Status ==="
sudo systemctl status wazuh-agent --no-pager
