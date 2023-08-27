# Printer Server

Our wireless printers never work with our iPhone, Android, Chromebook hodgepodge so I think print-to-pdf + file upload might be the way to go...

## Architecture

The system is made of of three distinct components:

1. user devices (phone, chromebook)
2. application (single page to upload a file, CRUD services) 
3. printer server (polls application services for work)

## UX

A single HTML page

* User presented with upload form
* User uploads

## Server

The app server will be implemented in Python

* User presented with upload page
* Upload is saved to server FS

The printer server will be .NET 4.x to access printer

* Process watches for file changes
* Process prints the file

## Publishing

I pushed this service to digital ocean.  See package.json scripts.

## Digital Ocean Setup

To ssh to digital ocean, you need to add your ssh key to the droplet.  See [this](https://www.digitalocean.com/docs/droplets/how-to/add-ssh-keys/to-account/) for more info.

- I created an ssh key on my mac with `ssh-keygen`
- I copied the public key to clipboard with `pbcopy < ~/.ssh/id_rsa.pub`
- I ran `doctl compute ssh-key import <key name> --public-key <paste public key here>` but it did nothing?
- I used the digital ocean console to ssh to the droplet from the browser and pasted the public key to the end of the `~/.ssh/authorized_keys` (root user).
- I was then able to ssh to the droplet from my mac with `ssh root@<ip address>`, which prompted for my passphrase and then logged me in.

Once I obtained ssh access, I could `su` to my dev account, via `su ca` and then `cd /home/ca/code/print-server`.

The `start` script starts on port 5510 and nginx is configured to forward to 5510.  To ensure this app runs after a system reboot I ran `sudo systemctl enable /home/ca/code/print-server/print-server.service`.

Where `print-server.service` is:

``` 
[Unit]
Description=Print Server Upload API

[Service]
WorkingDirectory=/home/ca/code/print-server
User=ca
ExecStart=/home/ca/code/print-server/start.sh

[Install]
WantedBy=multi-user.target
```

## Nginx

I installed nginx on the droplet with `sudo apt install nginx`.  I then configured it to forward to this app my modifying `/etc/nginx/sites-enabled/ca0v.us` with the following config (look for 5510 below):

```
server {

        root /var/www/ca0v.us/html/ca0v/;
        index index.html index.htm index.nginx-debian.html;

        server_name ca0v.us www.ca0v.us;

        location / {
                try_files $uri $uri/ =404;
        }

	location /stories/ {
		rewrite ^(/stories/)$ $1/ last;
		proxy_pass http://localhost:5500/;
	}

	location /stories/svelte-lab/ {
		rewrite ^(/stories/svelte-lab/)$ $1/ last;
		proxy_pass http://localhost:5500/static/svelte-lab/;
	}

	location /about/ {
		proxy_pass https://ca0v.github.io/ca0v/;
	}

	location /printer/ {
		proxy_pass http://localhost:5510/;
	}

        location /aiq/ {
                proxy_pass http://localhost:3003/aiq/;
        }

	location /chat/ {
		proxy_pass http://localhost:3000/chat/;
		proxy_http_version 1.1;
		proxy_set_header Upgrade $http_upgrade;
		proxy_set_header Connection "upgrade";
	}

    listen [::]:443 ssl ipv6only=on; # managed by Certbot
    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/ca0v.us/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/ca0v.us/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}

server {
    if ($host = ca0v.us) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


        listen 80;
        listen [::]:80;

        server_name ca0v.us www.ca0v.us;
    return 404; # managed by Certbot

}
```

To start nginx, I ran `sudo systemctl start nginx`.  To restart, I ran `sudo systemctl restart nginx`.  To stop, I ran `sudo systemctl stop nginx`.

## References

* [How I got puppeteer working in M1](https://rickynguyen.medium.com/puppeteer-for-apple-m1-43a5c31e4f9d)
* [Large Uploads](https://stackoverflow.com/questions/18121227/how-to-avoid-request-entity-too-large-413-error)