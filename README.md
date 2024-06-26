# AMTG
## Educational purposes ONLY
AMTG (Automatic Malicious Traffic Generator) - tool that generates suspicious activity on endpoints using Linux compatible utilities. Made by Anton Shabanov for UTMN VKR 2024
## Requirements
- hydra
- hping3
- gobuster
- samba-client
- nmap
- python >3.10
## Installation
- Clone this repository
- Ensure all of required utilities installed in your system
- Edit config.json
- Run main.py     
## Pros
- It uses Linux utilities instead python implementation. It gives more realistic fingerprint of suspicious activity
- Easy to add your own utility by writing minimal amount of code
- It works without need to install any additional libraries with pip. Only default python
## Cons
- Config cannot be filled with target subnet. Only single hosts addresses
- To use additional flags in utility invoke you need to change the code
## WIP
- Standalone version (You don't have to install required utilities). Will improve compatibility but may cause lost of fingerprint realism. Will be a separate release
- Subnets in config (You don't have to write addresses of every single host you want to taget if they're in the same subnet)
   
