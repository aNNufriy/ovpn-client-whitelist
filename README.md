**Why?**

Sometimes it's important for openvpn administrators to have a way to limit a list users with valid and not revoked certificates, who can connect to a particular openvpn server. The problem can be solved by creating a white list and applying openvpn  ***client-connect*** callback to check presence of a user's common name in the white list. That is exactly what ***checkcn.py*** script does.

***client-disconnect*** just logs client disconnection.

**How to:**

1. add following lines to openvpn server config

>     client-connect "/etc/openvpn/server/connect.py /etc/openvpn/server/whitelist /var/log/openvpn/server.connect.log"
>     client-disconnect "/etc/openvpn/server/disconnect.py /etc/openvpn/server/whitelist /var/log/openvpn/server.connect.log"
>     script-security 2

----
2. copy *connect.py* and *disconnect.py* to */etc/openvpn/server/*;
3. set permissions:
>     chmod a+x /etc/openvpn/server/connect.py
>     chmod a+x /etc/openvpn/server/disconnect.py

3. make shure directory */var/log/openvpn/* exists;
4. create whitelist: /etc/openvpn/server/cn-whitelist and add your openvpn clients' common names into it.
