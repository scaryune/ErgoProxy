
# Xfreerdp Command
An X11 [RDP](/networking/protocols/RDP.md) client chish (wtf was I trying to write here?) is part of the #FreeRDP project.
- an #RDP-server is built into many versions of Windows.xf

## Usage:
```
xfreerdp [file] [options] [/v:server[:port]]
```


### Useful options:
- `/u:` set the username to login with
	- ==if you don't set a username it will default to your own username== (ex: "hackpuppy");
- `/v:` set the IP/ host to login to

### Vulnerabilities:
Administrator:
- the ==administrator== username may not be protected on a host. RDP can be accessed w/ the admin username and NO PASSWORD.