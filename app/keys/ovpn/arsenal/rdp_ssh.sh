#--- dont forget redirect proper ports on router

#--- RDP
#ssh -L 10116:94.247.62.24:10116 vladvons@oster.com.ua -N
#--- in another session
# xfreerdp /v:127.0.0.1:10116 /bpp:8 /size:95% /u:snoVdalV


#--- SSH ProxMox
# ssh -J vladvons@oster.com.ua root@94.247.62.24 -p 10100


#--- pptp
# ssh -L 1723:94.247.62.24:1723 vladvons@oster.com.ua -N

#sudo pptpsetup --create pptp_arsenal --server 127.0.0.1 --username user01 --password arsenal_Q01 --encrypt
#sudo pon pptp_arsenal

nmcli connection add type vpn vpn-type pptp con-name pptp-ssh-arsenal \
  ifname -- \
  vpn.data 'gateway=127.0.0.1,refuse-eap=true,user=user01,password-flags=0,require-mppe=true' \
  vpn.secrets 'password=arsenal_Q01'