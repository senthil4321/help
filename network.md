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

### VLAN TPLink Configuration  PVID
```
Set the default VLAN ID of the port. Valid values are from 1 to 4094. It is used mainly in the following two ways:
When the port receives an untagged packet, the switch inserts a VLAN tag to the packet based on the PVID.
```
>
Note on PVID: For some switches it is necessary to set the PVID (Port VLAN ID) on untagged ports in addition to the VLAN ID of the port. This specifies which VLAN any untagged frames should be assigned to when they are received on this untagged port. The PVID should therefore match the configured VLAN ID of the untagged port

### tagged and untagged
```
VLAN-enabled ports are generally categorized in one of two ways: tagged or untagged. These may also be referred to as "trunk" or "access" respectively. The purpose of a tagged or "trunked" port is to pass traffic for multiple VLANs, whereas an untagged or "access" port accepts traffic for only a single VLAN. Generally speaking, trunk ports will link switches, and access ports will link to end devices.
```
---
### ip 
temporary net configuration 
set link up 
set link down 
set default configuration 
show route
to purge all configuration 
ip addr flush eth0
Ref. https://ubuntu.com/server/docs/configuring-networks#:~:text=To%20configure%20a%20default%20gateway,to%20match%20your%20network%20requirements.&text=If%20you%20require%20DNS%20for,%2Fetc%2Fresolv.conf%20.
--- --- ---
### TODO 
```
sudo nano /etc/network/interfaces.d/vlans
auto eth1.100
iface eth1.100 inet manual
  vlan-raw-device eth1
  
sudo nano /etc/dhcpcd.conf
interface eth1.100
static ip_address=192.168.100.24/24
static routers=192.168.100.1
static domain_name_servers=192.168.100.1

interface eth1.101
static ip_address=192.168.101.24/24

sudo ip link set eth1 down
sudo ip link set eth1 up
sudo ip link show eth1
sudo ip link set eth1 down
sudo ip link set eth1.100 up
sudo ip link show eth1.100
modprobe 8021q
apt install vlan
sudo ip link add link eth1 name eth1.100 type vlan id 100
sudo ip link set up eth1.100
https://wiki.ubuntu.com/vlan
sudo tcpdump -i eth1 -e ip
sudo systemctl restart networking
hostname -I

ip route list
ip route add [IP]/[PREFIX] dev [INTERFACE] via [GATEWAY]
ip route add 192.168.100.24/24 dev eth1 via 192.168.100.22
ip link add link eth1 name eth1.100 address aa:bb:cc:dd:ee:24 type vlan id 100
ip link add link eth1 name eth1.101 address aa:bb:cc:dd:ee:24 type vlan id 101
ip link add link eth1 name eth1.101 address aa:bb:cc:dd:ee:22 type vlan id 101

sudo nano /etc/dhcpcd.conf
interface eth1.101
static ip_address=192.168.101.24/24

sudo nano /etc/dhcpcd.conf
interface eth1.101
static ip_address=192.168.101.22/24

sudo ip addr flush dev eth1
https://wiki.debian.org/NetworkConfiguration#Starting_and_Stopping_Interfaces
sudo systemctl restart networking
sudo systemctl status networking
https://serverfault.com/questions/1111595/linux-why-is-arp-not-answered-via-vlan-bridge
```
