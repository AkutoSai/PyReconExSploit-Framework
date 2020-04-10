# PyReconExSploit
PyReconExSploit is a Reconnaissance and Exploitation framework written in Python3.

# Installation Instructions:

In order to use `search` command you must install the searchsploit binary! from {https://www.exploit-db.com/searchsploit/#install}

## Building:

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install exploitdb netcat nmap perl php
pip3 install babysploit
git clone https://github.com/AkutoSai/PyReconExSploit
cd PyReconExSploit/
python3 setup.py install
pyreconexsploit
```
# Getting Started:

#### Setting Configuration Values:

PyReconExSploit uses ConfigParser in order to write and read configuration. Your config file is automatically
generated and located at `./pyreconexsploit/config/config.cfg`. You can manually change configuration settings
by opening up the file and editing with a text editor or you can use the set command to set a new value for
a key. Use the set command like so:
```
set rhost
>> Enter Value For rhost: 10
>> Config Key Saved!
```

If before running this command the rhost key had a value of 80, the rhost key after running this command has a
value of 10. You can also add configuration variables to the config by using the set command with a new key after it
like so:
```
set newkey
>> Enter Value For newkey: hello
>> Config Key Saved!
```
Before running this there was no key named "newkey". After running this you will have a key named "newkey" in your config
until you use the `reset` command which resets the saved configuration.

#### Running A Tool:

In order to run a tool all you have to do is enter the name of the tool into pyreconexsploit. You can use the `tools` command
to display a menu with all the currently available tools.

# Features:

  - Information Gathering
  - Exploitation
  - Post Exploitation
  - Bruteforcing
  - Phishing
  - Stenography/Cryptography
 
### Information Gathering:

  - Nmap
  - IP Info
  - Censys Lookup
  - DNS Lookup
  - Raccoon
  - Cloudflare Bypasser
  
### Exploitation:
  
  - Searchsploit
  - ReverseShell Wizard
  - FTP Buffer Overflow Scan
  - WPSeku WordPress Vuln Scanner
  
### Post Exploitation:

  - In The Works
  
### Bruteforcing:

  - FTP
  - WPSeku
  
### Phishing:

  - BlackEye
  
### Crypto/Stegano:

  - MetaKiller
  - PDFMeta

# Credits

[@linux_choice](https://github.com/thelinuxchoice) for BlackEye sites and base

[@M4ll0k](https://github.com/m4ll0k) for WPSeku

[@exploitdb](https://github.com/exploitdb) for Searchsploit
