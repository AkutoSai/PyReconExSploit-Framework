def welcome():
    import socket
    banner = """
                     PyReconExSploit
                  Developed by @AkutoSai
                https://github.com/AkutoSai
        """
    gw = socket.gethostname()
    print("     [i] Default Gateway: %s [i]" % gw)
    print(banner)
    print("")

def tools():
    from terminaltables import SingleTable
    from pyfiglet import Figlet
    print("Enter the name of the tool which you want to use to use.\n")
    infotable = [
      ['\nTool', '\nDescription'],
      ['cfbypass', 'cloudflare bypasser'],
      ['raccoon', 'use raccoon scanner tool | command: raccoon --help',
      ['dnslookup', 'dns lookup tool'],
      ['censyslookup', 'censys api lookup | req api creds'],
      ['iplookup', 'ip info tool'],
      ['nmap', 'nmap port scanner tool']  
    ]
    table = SingleTable(infotable, "Information Gathering")
    print("")
    print(table.table)
    print("")
    exploittable = [
      ['\nTool', '\nDescription'],
      ['wpseku', 'wordpress vulnerability scanner'],
      ['ftpvulnscan', 'check for ftp buffer overflow'],
      ['reverseshell', 'reverse shell tool for creating payloads'],
      ['searchsploit', 'search available exploits (use search command)']
    ]
    exptable = SingleTable(exploittable, "Exploitation")
    print(exptable.table)
    print("")
    phishingtable = [
      ['\nTool', 'Description'],
      ['blackeye', 'BlackEye Phish Kit']
    ]
    phishtable = SingleTable(phishingtable, "Phishing")
    print("")
    print(phishtable.table)
    print("")
    bruteforcetable = [
      ['\nTool', '\nDescription'],
      ['ftpbruteforce', 'ftp brute force tool']
    ]
    cryptotable = [
      ['\nTool', '\nDescription'],
      ['pdfmeta', 'pdf meta data']
      ['StegHide', 'Steganography']
    ]
    cryptable = SingleTable(cryptotable, "Cryptography/Steganography")
    bftable = SingleTable(bruteforcetable, "Bruteforcing")
    print(cryptable.table)
    print("")
    print(bftable.table)
