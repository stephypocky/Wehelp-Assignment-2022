
import urllib.request as request
import json
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = json.load(response)
tpattract = data["result"]["results"]
for tptrip in tpattract:
    # if (tptrip["xpostDate"][0:4]) >= "2015":
    if (tptrip["xpostDate"][0:4]) >= "2015":
        # print(tptrip["xpostDate"][0:4])
        # print(len(tptrip))
        # print(tptrip["address"][5:8])
        # print(len(tptrip))
        # print(tptrip["file"])
        # print(tptrip["file"].split("jpg"))
        # print(len(tptrip["file"]))
        imgurl = tptrip["file"].split("https")
        print("https"+imgurl[1])
        # print(imgurl)

    with open("data.csv", "w", encoding="utf-8") as file:
        for tptrip in tpattract:
            if (tptrip["xpostDate"][0:4]) >= "2015":
                file.write(tptrip["stitle"]+","+tptrip["address"][5:8]+"," +
                           tptrip["longitude"]+","+tptrip["latitude"]+"," +
                           "https"+tptrip["file"].split("https")[1]+"\n")
