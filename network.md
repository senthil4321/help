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
### Socket bind
Socket bind is a mechanism to bind local interface and port to the program.
Example bind a specific interface and port to the server program to listen to.
#### How bind works
When a socket is creatd, it is initially not associated with any address or port. The `bind` function assigns a specific local address and port to the socket, allowing it to receive incoming packets directed to that address and port.
``` java
import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.ServerSocket;

public class Main {
    public static void main(String[] args) {
        try {
            // Create a server socket
            ServerSocket serverSocket = new ServerSocket();

            // Bind the server socket to an address and port
            InetSocketAddress address = new InetSocketAddress("192.168.1.100", 8080);
            serverSocket.bind(address);

            System.out.println("Socket bound to " + address.getHostName() + ":" + address.getPort());

            // Close the server socket
            serverSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```
### Binding program to specific interface in linux
#### Method 1 : Using iptables to redirect traffic to a local port
#### Method 2 : Using SO_BINDTODEVICE Socket Option
---
To forward SSH connections from one VLAN to an SSH server listening on a different VLAN, you can use `iptables` to set up port forwarding. Here’s a step-by-step guide to achieve this:

### Scenario

- **VLAN 100**: Interface `eth0.100`, IP `192.168.100.1`
- **VLAN 200**: Interface `eth0.200`, IP `192.168.200.1`
- **SSH Server**: Listening on `192.168.200.2` (VLAN 200) on port 22

### Step 1: Enable IP Forwarding

First, ensure that IP forwarding is enabled on your Linux system. This allows the system to forward packets between interfaces.

1. **Enable IP forwarding temporarily**:
   ```sh
   sudo sysctl -w net.ipv4.ip_forward=1
   ```

2. **Enable IP forwarding permanently**:
   Add the following line to `/etc/sysctl.conf`:
   ```sh
   net.ipv4.ip_forward = 1
   ```
   Then apply the changes:
   ```sh
   sudo sysctl -p
   ```

### Step 2: Set Up `iptables` Rules for Port Forwarding

Use `iptables` to forward SSH traffic from VLAN 100 to the SSH server on VLAN 200.

1. **Forward SSH traffic from `eth0.100` to `192.168.200.2:22`**:
   ```sh
   sudo iptables -t nat -A PREROUTING -i eth0.100 -p tcp --dport 22 -j DNAT --to-destination 192.168.200.2:22
   ```

2. **Allow forwarding in the `FORWARD` chain**:
   ```sh
   sudo iptables -A FORWARD -i eth0.100 -o eth0.200 -p tcp --dport 22 -j ACCEPT
   sudo iptables -A FORWARD -i eth0.200 -o eth0.100 -p tcp --sport 22 -m state --state ESTABLISHED,RELATED -j ACCEPT
   ```

3. **Masquerade the outgoing packets (if needed)**:
   If the SSH server on VLAN 200 needs to see the requests as coming from the forwarding machine, you can use masquerading:
   ```sh
   sudo iptables -t nat -A POSTROUTING -o eth0.200 -j MASQUERADE
   ```

### Step 3: Save `iptables` Rules

To ensure the `iptables` rules persist across reboots, save them:

1. **Save the rules**:
   ```sh
   sudo iptables-save > /etc/iptables/rules.v4
   ```

2. **Restore the rules on boot**:
   Ensure that the rules are restored on boot by using a service like `iptables-persistent`:

   ```sh
   sudo apt-get install iptables-persistent
   sudo netfilter-persistent save
   sudo netfilter-persistent reload
   ```

### Example Scenario

Assume you have:
- **VLAN 100**: Interface `eth0.100`, IP `192.168.100.1`
- **VLAN 200**: Interface `eth0.200`, IP `192.168.200.1`
- **SSH Server**: Listening on `192.168.200.2` (VLAN 200) on port 22

1. **Enable IP forwarding**:
   ```sh
   sudo sysctl -w net.ipv4.ip_forward=1
   ```

2. **Set up `iptables` rules**:
   ```sh
   sudo iptables -t nat -A PREROUTING -i eth0.100 -p tcp --dport 22 -j DNAT --to-destination 192.168.200.2:22
   sudo iptables -A FORWARD -i eth0.100 -o eth0.200 -p tcp --dport 22 -j ACCEPT
   sudo iptables -A FORWARD -i eth0.200 -o eth0.100 -p tcp --sport 22 -m state --state ESTABLISHED,RELATED -j ACCEPT
   sudo iptables -t nat -A POSTROUTING -o eth0.200 -j MASQUERADE
   ```

3. **Save the rules**:
   ```sh
   sudo iptables-save > /etc/iptables/rules.v4
   ```

### Verification

1. **Check IP forwarding**:
   ```sh
   sysctl net.ipv4.ip_forward
   ```

2. **Check `iptables` rules**:
   ```sh
   sudo iptables -L -v -n
   sudo iptables -t nat -L -v -n
   ```

3. **Test the setup**:
   - From a device on VLAN 100, attempt to SSH to `192.168.100.1`.
   - Verify that the connection is forwarded to the SSH server on `192.168.200.2`.

By following these steps, you can forward SSH connections from one VLAN to an SSH server listening on a different VLAN using `iptables` on a Linux system.
