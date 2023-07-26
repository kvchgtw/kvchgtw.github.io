import json, ssl, re, csv
import urllib.request as request
context = ssl._create_unverified_context()
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src, context=context) as response:
    data=json.load(response)
    #dataMRT=json.dumps(response)



with open("attractions.csv", "w", encoding = "utf-8") as file:

        
    list = data["result"]["results"]
    pattern =  r'(https?://[^\s]+)'
    
    for i in list:
            jpgList = re.findall(pattern,i["file"].lower().replace("jpghttp","jpg http")) #先把file中jpghttp取代為jpg http，然後比對正則，讓url被分割出來，然後就可以用index叫出第一組url
            file.write(i["stitle"]+","+i["address"][5:8]+","+i["longitude"]+","+i["latitude"]+","+jpgList[0]+"\n") #寫入.csv
       

# 創建一個空的字典來儲存已經出現過的車站資料，同時也會儲存車站景點為key
station_to_spots = {}

# 根據原始資料來重新組織字典
for j in list:
    station = j['MRT']
    spot = j['stitle']
    
    #如果有車站已經被存在station_to_spots，則把該景點直接加為這個車站(key)的value
    #若否，則新增一個車站(key)，其value就是該景點
    if station in station_to_spots:
        station_to_spots[station].append(spot)
    else:
        station_to_spots[station] = [spot]
       
# 用.items()方法找出字典中的 station(key), spots(value) 並轉換為tuple。
result_list = [[station] + spots for station, spots in station_to_spots.items()]

with open("mrt.csv", "w", encoding = "utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(result_list)

        

                