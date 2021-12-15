## Wireshark

## VLAN Configuration
1. https://www.thomas-krenn.com/en/wiki/VLAN_Basics  
1. https://kb.netgear.com/30919/How-to-configure-VLANs-on-a-ProSAFE-Web-Managed-Plus-Switch-with-shared-access-to-the-internet  
1. https://kb.netgear.com/11673/How-do-I-setup-a-VLAN-trunk-link-between-two-NETGEAR-switches  
## Fakra Color Code
1. https://electronics.stackexchange.com/questions/211624/identify-tesla-model-s-connector
## Wireshark CAN plugin
1. https://canlogger.csselectronics.com/downloads.php?q=wireshark 
1. https://www.wireshark.org/docs/wsug_html_chunked/ChPluginFolders.html 
1. https://canlogger1000.csselectronics.com/img/Wireshark-Load-DBC-File-J1939-Example.jpg 
## CAN
### CAN in WireShark SoketCAN
1. https://libbits.wordpress.com/2012/05/07/capturing-and-analyzing-can-frames-with-wireshark/ 

### vlan trunk
> Vlan trunk connects two switch and transports data of multiple vlans
### udp multicast
Udp multicast address is different then the normail ip address
Multicast enables to send data to multiple clients without more overhead on the server


## router subnet ip mask ❤️
* https://routersecurity.org/ipaddresses.php#:~:text=Pretty%20much%20every%20home%20router,0.


## subnet
https://www.oreilly.com/library/view/linux-network-administrators/1565924002/ch05s05.html

### subnet table
https://dnsmadeeasy.com/support/subnet/

https://serverfault.com/questions/54981/linux-command-line-tool-to-work-with-netmasks-cidr-notation/54993
```bash
sudo apt-get install ipcalc
sudo apt-get install sipcalc
```

https://en.wikipedia.org/wiki/Subnetwork#Subnet_and_host_counts

1. A router serves as a logical or physical boundary between the subnets.
1. Traffic is exchanged between subnetworks through routers when the routing prefixes of the source address and the destination address differ.
1. For example, 255.255.255.0 is the subnet mask for the prefix 198.51.100.0/24.
1. Each subnet has hosts


https://www.appservgrid.com/paw92/index.php/2018/10/21/networking-basics-ip-address-netmasks-and-subnets/

### Broadcast address
https://www.ionos.com/digitalguide/server/know-how/broadcast-address/

### Addresses Hosts Netmask Amount of a Class C
```bash
/ 30 4 2 255.255.255.252 1 / 64
```
Although the all-zeros and the all-ones host values are reserved for the network address of the subnet and its broadcast address,


### TODO 
http://linux-ip.net/html/tools-ip-route.html

### IPtables firewall rule
https://opensource.com/article/18/9/linux-iptables-firewalld
