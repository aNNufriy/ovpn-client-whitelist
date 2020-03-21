**Why?**

Sometimes it's important for openvpn administrators to have a way to limit a list users with valid and not revoked certificates, who can connect to a particular openvpn server. The problem can be solved by creating a white list and applying openvpn  ***client-connect*** callback to check presence of a user's common name in the white list. That is exactly what ***checkcn.py*** script does.

**How to:**

1. add following lines to openvpn server config

>     client-connect "/etc/openvpn/server/checkcn.py /etc/openvpn/server/cn-whitelist /var/log/openvpn/server.connect.log"
>     script-security 2

----
2. copy *checkcn.py* to */etc/openvpn/server/checkcn.py*;
3. make shure directory */var/log/openvpn/* exists;
4. create whitelist: /etc/openvpn/server/cn-whitelist and add your openvpn clients' common names into it.
