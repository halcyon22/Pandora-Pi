#!/usr/bin/env python

import sys, time, os, socket
import pickle
import pandoraUtils

if __name__ == "__main__":

    # Read event type from command arguments
    if len(sys.argv) < 2:
        pandoraUtils.log("Error reading event type from command arguments")

    event_type = sys.argv[1]
    pandoraUtils.log("event_type="+event_type)

    # Read parameters from input
    params = {}
    
    for s in sys.stdin.readlines():
        param, value = s.split("=", 1)
        params[param.strip()] = value.strip()

    # Handle specific events
    if event_type == "songstart":

        info = {}
        info["song"] = params["title"]
        info["artist"] = params["artist"]
        info["album"] = params["album"]
        info["stationCount"] = params["stationCount"]
        info["stationName"] = params["stationName"]

        stations = []

        for i in range(0, int(params["stationCount"])):
            stations.append(params["station"+str(i)])

            if params["station"+str(i)] == params["stationName"]:
                info["stationNumber"] = i

        info["stations"] = stations

        pandoraUtils.setShared(info)
        pandoraUtils.parseAndWrite()

    elif event_type == "songfinish":
        pass

    elif event_type == "usergetstations":
        previous_station = pandoraUtils.getShared("stationNumber")
        pandoraUtils.sendCommand('s'+str(previous_station))

    elif event_type == "userlogin":
        pandoraUtils.writeToLCD("Logging in...")

