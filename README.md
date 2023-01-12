# Printer Server

Our wireless printers never works with our iPhone, Android, Chromebook hodgepodge so I think print-to-pdf + file upload might be the way to go...

## Architecture

The system is made of of three distinct components:

1. user devices (phone, chromebook)
2. application (single page to upload a file, CRUD services) 
3. printer server (polls application services for work)

For learning purposes, this will use Vue

* User presented with upload form
* User uploads

The app server will be implemented in Python

* User presented with upload page
* Upload is saved to server FS

The printer server will be .NET 4.x to access printer

* Process watches for file changes
* Process prints the file

## References

* [How I got puppeteer working in M1](https://rickynguyen.medium.com/puppeteer-for-apple-m1-43a5c31e4f9d)
* [Large Uploads](https://stackoverflow.com/questions/18121227/how-to-avoid-request-entity-too-large-413-error)