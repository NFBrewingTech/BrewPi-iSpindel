###   Installation information for iSpindel to BrewPi integration   ###
###   Work in progress, please backup all files before proceeding!!!
###   Please report any issues at https://github.com/gmasem/BrewPi-iSpindel

First, a huge thank you to Tozzi for allowing me to use his generic-TCP interface to the iSpindel.  It greatly simplified the data in portion of the integrationand allowed greater flexibility in testing. All of his software is in the Generic-TCP folder.  The required files are in the Scripts folder already.

This has been tested on the current LEGACY branch only. It will require modification to run on others.  I plan on making a version for the latest BrewPI as well, but don't have one to test with at the moment and want to work out the issues on here first.  I do NOT have an ETA for building an install for the other versions at this time.

1. - Make a complete backup f your files, at least the ones being modified!
2. - Install numpy with 'sudo apt-get install python-numpy'
3. - Copy the files/folders fro WWW into the /var/www/html folder
4. - Copy the files in Scripts into the /home/brewpi folder.
5. - Edit ispindel.py as needed - For testing I also have CSV and Ubidots ON in this version. Add your UBI token
6. - Run the following commands:

    cd /home/brewpi
	sudo mv ./ispindle-srv /etc/init.d
	sudo chmod 755 /home/brewpi/iSpindle.py
	sudo chmod 755 /etc/init.d/ispindle-srv
	cd /etc/init.d
	sudo systemctl daemon-reload
	sudo insserv ispindle-srv
	sudo service ispindle-srv start

Now, test the iSpindel connection - go into iSpindel config mode, set it to use TCP connection and insert the IP of your BrewPI as well as port number 9501. If sucessful you will start to see data logged in the /var/www/html/data/iSpindel folder. One CSV with all data, another with just the most recent reading.  The full CSV is for testing and can be disabled in iSpindel.py, the single is what BrewPI pulls in.  For testing you may want to change the reporting frequency (on the iSpindel) to 30 seconds or similar.

Once all files are in place and the iSpindel is logging data to the server, stop and restart the BrewPI script.  This will make sure the web interface and the script in the back are using the new versions. 

Known issues:
	Mobile devices are taking a long time to display. This started when I enlarged the graph to allow room for additonal text.  Could be from extra logged data - plan on removing Battery and maybe Temp from graph and adding it to the header or footer as text only. Currently graphing battery to follow the battery depletion speed.

	Initial logging when starting new brew will be the last reading from the iSpindel - be that from the last brew, sitting on the table or in the new brew. 

	If there are NO iSpindel readings when you start a brew the graphing won't load. On a new install make sure the iSpindel has logged a data point before starting the brew..  This is only an issue on the first run after adding the integration.

	Planning on building an install script to take care of all of the install for us. 


Most important make sure you are backed up because this is only tested by me so far, I am not a programmer and figuring it out as I go! .I also built it on a Debian VM not a Raspberry PI install so it's possible there may be some missing dependencies  Any issues again add an issue on GitHub.