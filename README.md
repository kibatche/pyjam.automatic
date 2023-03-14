# pyjam.automatic
A small python program to automate the creation of a pyjam.as tunnel.

pyjam.as is a super cool reverse proxy for a local service. To me, it's useful as a replacement for ngrok and its business practices which severely limit the usefulness of such a program in CTF, Hack The Box, or root-me challenges.

A huge thanks to the dev(s) of tunnel.pyjam.as !

## pyjam.as links :
https://tunnel.pyjam.as/
https://gitlab.com/pyjam.as/tunnel


## needed program:
You need wireguard in order to use this program.

## usage :

```
usage: pyjam.py [-h] (-p PORT | -d | -u)

A python program to automate the creation of a pyjam.as tunnel.

options:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  The port to bind to. If a tunnel already exists, it will be deleted.
  -d, --down            Down the tunnel
  -u, --up              Up the tunnel
```
