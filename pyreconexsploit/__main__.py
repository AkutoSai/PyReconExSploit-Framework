#!/usr/bin/env python3

from configparser import ConfigParser
from babysploit import display, configuration, dnslookup, helper, iplookup, ftpv, nmtool, reverseshell, searchsploit, blackeye, ftpbruteforce, wpseku, cloudflarebypass
from pyfiglet import Figlet
import os, subprocess

try:
    # Clear Terminal #
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    # Display Welcome Message #
    display.welcome()
    # Check For Configuration File/Create New Configuration File #
    configuration.checkuser()
    # Display Help Menu #
    banner = """ PyReconExSploit is a Reconnaissance and Exploitation framework
written in Python3. The framework is equipped with different types 
of tools which are used for Information Gathering, Cryptology, 
Exploitation and more.    
    """
    print(banner)
    helper.run()
    # Load Config #
    config = ConfigParser()
    path = str(os.path.expanduser('~')) + "/config.cfg"
    config.read(path)
    # Create Terminal/Input #
    def main():
        terminal = input("\n[pyreconexsploit]> ") # Define the name of the terminal
        if terminal[0:4] == "help": # From Char Space 0 - 4 if it = help run the help command.
            f = Figlet(font='slant')
            print(f.renderText("       Help"))
            helper.run()
            main()
        elif terminal[0:1] == "?": # Same as above
            f = Figlet(font='slant')
            print(f.renderText("       Help"))
            helper.run()
            main()
        elif terminal[0:4] == "info": # Same as above but for info command
            for key, value in config.items('DEFAULT'):
                print("%s: %s" % (key, value))
            main()
        elif terminal[0:5] == "tools": # Same as above but for tool command
            display.tools()
            main()
        elif terminal[0:6] == "search":
            searchsploit.do_search()
            main()
        elif terminal[0:3] == "set": # Set Config Key
            if terminal[4:] == terminal[4:]: # Take Input After `set ` 
                config['DEFAULT'][terminal[4:]] = input("Enter Value For %s: " % terminal[4:]) # Get Value for that key name
                with open(path, "w") as configfile:
                    config.write(configfile) # Write the new config key
                print("Config Key Saved!")
                main()
        elif terminal[0:5] == "reset": # Reset configuration
            config['DEFAULT'] = {
                'lhost': '0.0.0.0',
                'lport': '8080',
                'rhost': 'google.com',
                'rport': '80',
                'platform': '',
                'usernamelist': 'lists/usernames',
                'passwordlist': 'lists/passwords',
                'urlpath': '/connect'
            }
            with open(path, "w") as configfile:
                config.write(configfile)
            main()
        elif terminal[0:4] == "exit":
            print("Exiting...")
            exit()
        elif terminal[0:7] == "raccoon":
            if terminal[8:] == terminal[8:]:
                query = terminal[8:]
                os.system("raccoon %s" % query)
            else:
                print("Please use raccoon --help for arguments.")
            main()
        elif terminal[0:8] == "iplookup":
            iplookup.run()
            main()
        elif terminal[0:4] == "nmap":
            nmtool.run()
            main()
        elif terminal[0:12] == "reverseshell":
            reverseshell.run()
            main()
        elif terminal[0:12] == "censyslookup":
            print("Broken Coming Soon")
            main()
        elif terminal[0:9] == "dnslookup":
            dnslookup.start()
            main()
        elif terminal[0:8] == "blackeye":
            blackeye.run()
            main()
        elif terminal[0:11] == "ftpvulnscan":
            ftpv.checkVulnerability()
            main()
        elif terminal[0:6] == "wpseku":
            wpseku.run()
            main()
        elif terminal[0:8] == "cfbypass":
            cloudflarebypass.run()
            main()
        elif terminal[0:13] == "ftpbruteforce":
            ftpbruteforce.start()
            main()
        else:
            print("Unknown Command")
            main()

    main()
except KeyboardInterrupt:
    print("Exiting...")
    exit()

if '__name__' == '__main__':
    main()
