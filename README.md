# ticketfinder

## Instructions
Download the python file `ticketfinder.py`.  Move the downloaded file to whatever directory you choose.  Open your terminal/console, and navigate to the directory with the downloaded `ticketfinder.py` file. Use the `cd` command to navigate (i.e. `cd directory1/directory2`). Once in the correct directory, run the program by typing `python ticketfinder.py`.

## Assumptions:
* There are 100 events
* Up to 10 tickets per event
* Events cost up to $50

## Additional comments
If I needed to support multiple events at the same location, I would simply eliminate the function `generate_location` and determine an event's location during its initialization using the `random` import.

If I needed to work with a larger world size, I might try to optimize the process of finding the 5 closest events.
