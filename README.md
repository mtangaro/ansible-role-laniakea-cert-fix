Laniakea fix for SSL certificate  requirement
=========

This is a brief users tutorial to fix Laniakea@ReCaS SSL certificate issue.

If you received a mail like this

```
Gentile utente,
ci è pervenuta dal GARR la segnalazione per le criticità sotto riportate relative alla sua istanza con 
Ip: <<YOUR VM IP ADDRESS>>  nel tenant elixir-italy-services. La deadline per la risoluzione per la risoluzione delle suddette è fissata per il giorno *****. Di seguito troverà tutti i dettagli. La preghiamo di darci feedback al più presto.
Cordialmente 
```

Please contact us at Laniakea@ReCaS [support e-mail](mailto:laniakea.helpdesk@gmail.com)

Introduction
------------

Due to a change of polity of Laniakea@ReCaS cloud provider, Galaxy needs to run under SSL certificate on port 443, enabling only TLSv1.2 and TLSv1.3.

This fix will do this for you. In particular:

1. Install Certbot to create

2. Install a Let's encrypt certificate

3. Update Nginx at 1.20.1 version

4. Re-configure NGINX and restart it.

The certificate will be automatically updated every three months.

Requirements
------------

To run this fix you need:

1. a valid email address, needed to register your certificate

2. a Galaxy instance created with Laniakea, **without any changes to NGINX configuration**

3. Your SSH private key, **used during the VM creation**, to login the VM.

Get your SSH private key on Laniakea
------------------------------------

If you used the Laniakea Dashborad to create the SSH key for your Galaxy instance, you can use the same interface to retrieve it.

1. Log in to [Laniakea@ReCaS](https://laniakea-dashboard.cloud.ba.infn.it/)

2. Open the ``SSH keys section``

3. Retrieve the **SSH private key**

![ssh_fig2](https://github.com/mtangaro/ansible-role-laniakea-cert-fix/blob/main/ssh_fig2.png)

Run the fix
-----------

1. Log in the Galaxy Virtual Instance with the following command (on Linux or MacOS systems):

```
ssh -i your_private_key galaxy@IP_ADDRESS
```

ore use putty on Windows.

2. Become super user:

```
sudo su -
```

3. Download this repository with the command:

```
git clone https://github.com/mtangaro/ansible-role-laniakea-cert-fix.git
```

4. Run the fix with the following command:

```
ansible-playbook ansible-role-laniakea-cert-fix/playbook.yml -e "admin_email=YOUR_EMAIL"
```

The script will configure the machine for you. An example of output is available [here](https://github.com/mtangaro/ansible-role-laniakea-cert-fix/blob/main/fix.log).

The script will print also the new address where the Galaxy instance is availabl=

```
TASK [ansible-role-laniakea-cert-fix : debug] *****************************************************
ok: [localhost] => {
    "msg": "Your Galaxy is now available at: https://cloud-212-189-205-161.cloud.ba.infn.it/galaxy"
}
```

where the old IP address is substitued with a URL obtained replacing the IP address dots, with the dash symbol "-".

For example if Galaxy was available at http//:212.189.205.161/galaxy, now will be available at https://cloud-212-189-205-161.cloud.ba.infn.it/galaxy.

Further details
---------------

This fix has been implemented as an Ansible role which is responsible of creating, installing a Let's Encrypt certificate and re-configure NGINX for you.

To do this the Certbot is installed in a python3 virtual environment located in your own galaxy home directory ``home/galaxy/certbot_venv``. The last version of certbot is used.

Then a Let's Encrypt SSL certificate is created exploitig the DNS record associated to each virtual machine on ReCaS Cloud facility.

Finally, a daily cron job is scheduled to manage and automate the certificate updates.

Also NGINX needs to be re-configured to support TLSV1.2 and TLSv1.3. The 1.20.1 version is used, with the upload module of galaxy dinamically built and installed.

TLSv1.3 is not enabled, since OpenSSL supports it starting from the 1.1.1 version, while CentOS 7 supports only OpenSSL up to 1.0.2 version.

Ansible Role details
====================

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
