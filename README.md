# Printer Server

Our wireless printers never works with our iPhone, Android, Chromebook hodgepodge so I think print-to-pdf + file upload might be the way to go...

* User presented with upload form
* User uploads
* Upload is saved to server FS
* Process watches for file changes
* Process prints the file (via updates a Power Shell script)
* That's as much as I have...may I need a windows service