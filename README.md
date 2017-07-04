# BrewPi-iSpindel
Integrating the iSpindel hydrometer into BrewPi - Just starting out.

As soon as I get a clearer idea of how to make it work, it will be here. The general idea is:

  -One script to accept input from the iSpindel and log it - probably keeping the most recent x data points.<br />
  -Modify existing scripts to add the logged data to the currently used JSON and CSV files.<br />
  -Modify existing files to plot newly added data.<br />
  
Saving a running database of the last X points will allow us to average them to smooth the line out. 
