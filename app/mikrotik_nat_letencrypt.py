# Created: 2025.05.11
# Author: Vladimir Vons <VladVons@gmail.com>
#
# This script searches mikrotik rule in 'ip/firewall/nat' with comment value 'nextcloud-vons'.
# Letencrypt requers www port 80, so replace fields 'dst-port' to '80', 'to-ports' to '80'.
# Generates letencrypt ssl sertifiate for host 'mlu7a.oster.com.ua'
# Restore fields 'dst-port', 'to-ports'.


import subprocess
from librouteros import connect
from librouteros.api import Path

class TMikrotik():
    def __init__(self, aHost: str, aUser: str, aPpassw: str):
        self.Api = connect(
            host=aHost,
            port=8728,
            username=aUser,
            password=aPpassw
        )

    def GetPath(self, aPath: str) -> Path:
        Arr = aPath.split('/')
        return self.Api.path(*Arr)

    def FindComment(self, aPath: Path, aComment: str):
        for xPath in aPath:
            if (xPath.get('comment') == aComment):
                return xPath

def Exec(aCmd: str):
    print('Executing:', aCmd)
    Cmd = aCmd.split()
    Result = subprocess.run(Cmd, capture_output=True, text=True)
    print('STDOUT:', Result.stdout, 'STDERR:', Result.stderr)

def Main():
    Mikrotik = TMikrotik('router.lan', 'admin', 'xxxx')
    Nat = Mikrotik.GetPath('ip/firewall/nat')
    RuleName = 'nextcloud-vons'
    Rule = Mikrotik.FindComment(Nat, RuleName)
    if (Rule):
        Nat.update(**{'.id': Rule['.id'], 'dst-port': '80', 'to-ports': '80'})

        Exec('service nginx stop')
        Exec('certbot certonly --standalone -d mlu7a.oster.com.ua --non-interactive --agree-tos --email vladvons@gmail.com --force-renewal')
        Exec('service nginx start')

        Nat.update(**{'.id': Rule['.id'], 'dst-port': Rule['dst-port'], 'to-ports': Rule['to-ports']})
    else:
        print('Rule not found', RuleName)

Main()
