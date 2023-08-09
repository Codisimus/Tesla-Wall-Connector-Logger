# Tesla Wall Connector Logger
This script logs the current "lifetime energy used" of a Tesla wall-mounted car charger.
[View on GitHub](https://github.com/Codisimus/Tesla-Wall-Connector-Logger)

## Pre-requisites
- A [Tesla Wall Connector](https://shop.tesla.com/product/wall-connector) with Wi-Fi capabilities (Gen 3+)
- The Wall Connector must be connected to your network (this is typically completed during the setup of the device)
- [Python 3.3+](https://www.python.org/downloads/)

## Setup
1. Clone [project](https://github.com/Codisimus/Tesla-Wall-Connector-Logger) or [download code](https://github.com/Codisimus/Tesla-Wall-Connector-Logger/archive/refs/heads/main.zip) and place within a directory
2. Install requirements using pip (i.e. `pip install -r requirements.txt`)
3. Replace the IP address within the script with the IP of the Wall Connector

## Run
This basic, single-action, script is best run as an automated task such as with [Windows Task Scheduler](https://learn.microsoft.com/en-us/windows/win32/taskschd/about-the-task-scheduler)

To run the script on-demand just execute it as you would any Python script, no arguments are required
