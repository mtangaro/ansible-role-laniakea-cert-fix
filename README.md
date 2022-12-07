Laniakea role for NGINX ssl cert fix
=========

Install certbot, install a Let's Encrypt certificate, update NGINX and configure it for supporting TLSv1.2 and TLSv1.3 only.

The configuration for NGINX is available here: https://ssl-config.mozilla.org/ 

This tool has been used for testing: https://github.com/drwetter/testssl.sh/tree/3.0 

Requirements
------------

Python3 and pyhton3-virtualenv are needed to create the certbot virtualenv and install it. These dependencieas are automatically solved by the role.


Role Variables
--------------

``admin_email``: set user email for certbot certificate creation (default: admin@example.com).

Example Playbook
----------------

Playbook example:

```yaml
    ---
    - hosts: localhost
      connection: local
      roles:
         - ansible-role-laniakea-cert-fix
```

Run the role with the following command:

```
ansible-playbook ansible-role-laniakea-cert-fix/playbook.yml -e "admin_email=your_email@server.com"
```

License
-------

MIT

Users tutorial
===============

Introduction
------------

Due to a change of polity of Laniakea@ReCaS cloud provider, Galaxy needs to run under SSL certificate on port 443, enabling only TLSv1.2 and TLSv1.3.

This fix will do this for you. In particular:

1. Install Certbot to create  








