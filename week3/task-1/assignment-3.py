
import urllib.request as request
import json
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = json.load(response)
    tpData = data["result"]["results"]
    for tpTrip in tpData:
        if (tpTrip["xpostDate"][0:4]) >= "2015":
            imgUrl = tpTrip["file"].split("https")
            print("https"+imgUrl[1])

    with open("data.csv", "w", encoding="utf-8") as file:
        for tpTrip in tpData:
            if (tpTrip["xpostDate"][0:4]) >= "2015":
                file.write(tpTrip["stitle"]+","+tpTrip["address"][5:8]+"," +
                           tpTrip["longitude"]+","+tpTrip["latitude"]+"," +
                           "https"+tpTrip["file"].split("https")[1]+"\n")
