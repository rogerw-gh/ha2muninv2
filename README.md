# ha2muninv2
Updated and revised ha2munin


![HACS Custom](https://img.shields.io/badge/HACS-Custom-orange)
![GitHub Repo stars](https://img.shields.io/github/stars/Erreur32/ha2munin?style=social)
![GitHub forks](https://img.shields.io/github/forks/Erreur32/ha2munin?style=social)
![MIT License](https://img.shields.io/badge/license-MIT-blue)



# HA2Munin

<img src="https://raw.githubusercontent.com/Erreur32/ha2munin/main/custom_components/ha2munin/icon.png" alt="Munin Logo" width="256"/>

En Francais, English translation below, please note that this component for Home Assistant will not provide values unless you follow the notes in HomeAssistant_2026_11.

Expose facilement les statistiques de Home Assistant (CPU, RAM, températures, etc) au format compatible Munin, via une simple endpoint HTTP.

---

## Fonctionnalités

- Endpoint `/api/munin` prêt pour interrogation par un plugin Munin externe
- Permet de superviser les données Home Assistant avec Munin
- Installation facile via HACS ou en custom_components

---

## Installation

Ajout dans HACS

-   Ouvre HACS → “Intégrations” → “Dépôts personnalisés”
-   Ajoute : https://github.com/Erreur32/ha2munin
-   Installe l’intégration depuis HACS
-   Et ajouter depuis integration le plugin (no config)

## Utilisation

L’intégration expose les valeurs sur :

```bash
http://<homeassistant>:8123/api/munin
```
## Creation Plugin munin

Pour les authorisation créer un token via Homeassistant (/profile/security)

Create now bash script for Munin 

```
nano /usr/share/munin/plugins/ha2munin
```


```bash
#!/bin/bash

# Adresse et token
HA_URL="http://x.x.x.x:8123/api/munin"
TOKEN=""

if [ "$1" = "config" ]; then
    echo "graph_title Home Assistant system_monitor"
    echo "graph_category homeassistant"
    curl -s -H "Authorization: Bearer $TOKEN" "$HA_URL" | grep '\.value' | while read line; do
        name=$(echo "$line" | cut -d. -f1)
        echo "$name.label $name"
    done
    exit 0
fi

curl -s -H "Authorization: Bearer $TOKEN" "$HA_URL" | grep '\.value'
```

Make executable
```
chmod +x /usr/share/munin/plugins/ha2munin
```
Activate in munin:
```
ln -s /usr/share/munin/plugins/ha2munin /etc/munin/plugins/ha2munin
```

## TODO

-   Détection automatique des capteurs
-   Paramétrage dynamique des sensors à exporter
-   Documentation améliorée


## Auteur

Erreur32

## Licence

MIT


# HA2Munin

Summary  - Exposes Home Assistant statistics (CPU, RAM, temperatures, etc.) in Munin compatible format, via an HTTP endpoint, accessed using an api in HA.

## Functionality

- Endpoint ʼ/api/muninʼ exposed using python for query by a Munin plugin
- Allows you to monitor Home Assistant data with Munin
- Easy installation via HACS or custom_components

---

## Installation

Added in HACS - HACS has been replaced by the Marketplace in HA 2026.11 release, the English translation of README.md and the Github repo only apply to versions 2026.11 and later.  

- Open Settings > Marketplace
- Click the checkbox 'I understand the risks and agree', the marketplace opens, with a long list.
- Click the icon Add from link
- In the popup window Add from a Github link:
- Paste 'https://github.com/rogerw-gh/ha2munin'
- Then click the Add button, which bring up the Connect Github popup, follow the process to authenticate your Home Assistant instance with your Github account.
- Installs integration from HACS
- And add from integration the plugin (no config)

- ## Usage

The integration exposes values on an api :

```bash
http://<homeassistant>:8123/api/munin
```


## Create the Munin Plugin

Create an API authorisation token:

- In Home Assistant, click on you account name in the bottom left hand corner
- Click on Security > Scroll down to Long-lived access tokens, click on Create token
- Give the token a name, e.g. munin
- Click on create token and then the Copy button, the puts the [very long] token into your past buffer, when you click Close, the token disappears and cannot be recovered
- This token will be used in your bash script.

#Munin bash script
Log into your munin instance and create the bash script for Munin:

```
nano /usr/share/munin/plugins/ha2munin [assumes you have read/write access to /usr/share/munin/plugins], otherwise use nano or vi or vim with sudo.

sudo nano
```

Copy everything up to and including the curl command after fi.
Make sure your system already has curl installed.

```bash
#!/bin/bash

# Adresse et token
HA_URL="http://x.x.x.x:8123/api/munin"
TOKEN=""

if [ "$1" = "config" ]; then
    echo "graph_title Home Assistant system_monitor"
    echo "graph_category homeassistant"
    curl -s -H "Authorization: Bearer $TOKEN" "$HA_URL" | grep '\.value' | while read line; do
        name=$(echo "$line" | cut -d. -f1)
        echo "$name.label $name"
    done
    exit 0
fi

curl -s -H "Authorization: Bearer $TOKEN" "$HA_URL" | grep '\.value'
```

Prepare the plugin by:

- Making the plugin executable using:
- sudo chmod +x /usr/share/munin/plugins/ha2munin
- Run the configure stage:
- sudo munin-run --servicedir /usr/share/munin/plugins ha2munin config
- Test using:
- sudo munin-run --servicedir /usr/share/munin/plugins ha2munin
- If you get a Warning the execution of 'munin-run' via 'systemd-run, add --ignore-systemd-properties to the command.
