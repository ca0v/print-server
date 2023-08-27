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

## Digital Ocean Setup (2)

Once I obtained ssh access, I could `su` to my dev account, but I can no remember where I put the actual code!

## References

* [How I got puppeteer working in M1](https://rickynguyen.medium.com/puppeteer-for-apple-m1-43a5c31e4f9d)
* [Large Uploads](https://stackoverflow.com/questions/18121227/how-to-avoid-request-entity-too-large-413-error)