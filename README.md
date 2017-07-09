# BrewPi-iSpindel
Integrating the iSpindel hydrometer into BrewPi - Just starting out, and hope to have some of my work up here very shortly.

So far I have only worked on the Legacy branch as this is the hardware I ahve to test on.
I have currently worked out geting data (HTTP) from the iSpindel to a logging location on the PI.

From there - when BrewPi does it's periodic logging the data is pulled into the JSON data.  I currently have the measured temperature, the battery voltage, and the calculated SG saved to the JSON. I may trim this to just the SG to reduce logging.
Additionally, the data is logged to another .CSV to allow display of battery level.

Will be testing (with manually logged data) on a live brew soon.  Currently is working using a JSON modified to include mock iSpindel data.

There are a minimal number of files that need to be modified/replaced as well as one additional folder to be created. May take additional work if you have password protected remote access configured, but should be one or two different files to replace. Will include options for both if possible.
