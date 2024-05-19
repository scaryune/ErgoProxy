
# MAC Address (Media Access Control)
A MAC address is a 48 bit hardware number which is *unique* to the device its attached to. It's usually embedded w/i a device's Network Interface Card (NIC) when the device is manufactured.

Used for addressing devices by the MAC sublayer of the [data-link-layer](/networking/OSI/data-link-layer.md).
## Format
```
Hyphen-Hexadecimal: 00-0a-83-b1-c0-8e
Colon-Hexadecimanl: 00:0a:83:b1:c0:8e
Period-separated: 000.a83.b1c.08e
```
Formatted into a 12 digit hexadecimal number (6 bytes) represented by #Colon-Hexadecimal, hyphen hexadecimal, or period separated hexadecimal notation.

>[!Info:]
> - Linux uses colon notation
> - Cisco uses period-separated
### Organizational Unique Identifier:
The first six digits of the MAC address identify the manufacturer. This is called the *Organizational Unique Identifier* (OUI) and is assigned by the IEEE to registered vendors:
``` 
CC:46:D6 - Cisco
```
### Network Interface Controller:
The last 6 digits of the address is the Network Interface Controller and is also assigned by the manufacturer.
## MAC Spoofing:
When a networked device pretends to identify as a different one by using its MAC address. This can break poorly-maintained security designs. For example, if a network firewall is configured to trust any and all traffic coming from the MAC address of the administrator

>[!Command line:]
> - [ifconfig](ifconfig.md)
> - [ip-command](ip-command.md)

> [!Resources:]
> - [Try Hack Me: What is Networking](https://tryhackme.com/room/whatisnetworking)

