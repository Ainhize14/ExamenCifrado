#!/bin/bash

sudo mkdir /var/tmp/Backups/$(date +%d-%m-%Y)
sudo rsync -av --link-dest=/var/tmp/Backups/$(date -d yesterday +%d-%m-%Y) $HOME/Seguridad /var/tmp/Backups/$(date +%d-%m-%Y)
