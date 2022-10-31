import requests
import json

# 1600 Pennsylvania Ave NW, Washington DC
api = "e2cf5921e72b5d355b06dd22324c75b7"
apiKey = "1bbf9714b9ac4babbf9714b9acebabca"


def getGeoCode(search):
    check = f"http://api.positionstack.com/v1/forward?access_key={api}&query={search}"
    country = requests.get(check).json()["data"][0]

    long = country["longitude"]
    latt = country["latitude"]

    #IBM
    # 15 Minute Forecast- v3
    url_3_days_forcast = f"https://api.weather.com/v3/wx/forecast/daily/3day?geocode={latt},{long}&format=json&units=e&language=en-US&apiKey={apiKey}"
    return requests.get(url_3_days_forcast).json()


def weatherForecast(search): 
    res: dict = getGeoCode(search=search)
    # print(res) 

    lst = [{x: y} for x, y in res.items() if x == "daypart"]
    day_1, day_2, day_3, day_4 = [], [], [], []


    for x, y in lst[0]["daypart"][0].items():

        day1_morning = {x: y[0]}
        day1_evening = {x: y[1]}

        day2_morning = {x: y[2]}
        day2_evening = {x: y[3]}

        day3_morning = {x: y[4]}
        day3_evening = {x: y[5]}

        day4_morning = {x: y[6]}
        day4_evening = {x: y[7]}

        res_1 = {"day1_morning": day1_morning, "day1_evening": day1_evening}
        res_2 = {"day2_morning": day2_morning, "day2_evening": day2_evening}
        res_3 = {"day3_morning": day3_morning, "day3_evening": day3_evening}
        res_4 = {"day4_morning": day4_morning, "day4_evening": day4_evening}

        day_1.append(res_1)
        day_2.append(res_2)
        day_3.append(res_3)
        day_4.append(res_4)


    dayOneMorning, dayOneEvening, dayTwoMorning, dayTwoEvening, dayThreeMorning, dayThreeEvening, dayFourMorning, dayFourEvening = [], [], [], [], [], [], [], []


    for x in day_1:
        val_1m = x["day1_morning"]
        val_1e = x["day1_evening"]

        dayOneMorning.append(val_1m)
        dayOneEvening.append(val_1e)

    for x in day_2:
        val_2m = x["day2_morning"]
        val_2e = x["day2_evening"]

        dayTwoMorning.append(val_2m)
        dayTwoEvening.append(val_2e)

    for x in day_3:
        val_3m = x["day3_morning"]
        val_3e = x["day3_evening"]

        dayThreeMorning.append(val_3m)
        dayThreeEvening.append(val_3e)

    for x in day_4:
        val_4m = x["day4_morning"]
        val_4e = x["day4_evening"]

        dayFourMorning.append(val_4m)
        dayFourEvening.append(val_4e)



    added_day1_morning = {k:v for x in dayOneMorning for k,v in x.items()}
    added_day1_evening = {k:v for x in dayOneEvening for k,v in x.items()}


    added_day2_morning = {k:v for x in dayTwoMorning for k,v in x.items()}
    added_day2_evening = {k:v for x in dayTwoEvening for k,v in x.items()}

    added_day3_morning = {k:v for x in dayThreeMorning for k,v in x.items()}
    added_day3_evening = {k:v for x in dayThreeEvening for k,v in x.items()}

    added_day4_morning = {k:v for x in dayFourMorning for k,v in x.items()}
    added_day4_evening = {k:v for x in dayFourEvening for k,v in x.items()}




    day_1, day_2, day_3, day_4 = [], [], [], []


    for x, y in res.items():
        result_1 = {x: y[0]}
        result_2 = {x: y[1]}
        result_3 = {x: y[2]}
        result_4 = {x: y[3]}

        day_1.append(result_1)
        day_2.append(result_2)
        day_3.append(result_3)
        day_4.append(result_4)

        if x =="validTimeUtc":
            break

    day1_m = {k:v for x in day_1 for k,v in x.items()}
    day1_e = {k:v for x in day_1 for k,v in x.items()}

    day2_m = {k:v for x in day_2 for k,v in x.items()}
    day2_e = {k:v for x in day_2 for k,v in x.items()}


    day3_m = {k:v for x in day_3 for k,v in x.items()}
    day3_e = {k:v for x in day_3 for k,v in x.items()}


    day4_m = {k:v for x in day_4 for k,v in x.items()}
    day4_e = {k:v for x in day_4 for k,v in x.items()}


    day1_m["morning"] = added_day1_morning
    day1_e["evening"] = added_day1_evening

    day2_m["morning"] = added_day2_morning
    day2_e["evening"] = added_day2_evening

    day3_m["morning"] = added_day3_morning
    day3_e["evening"] = added_day3_evening

    day4_m["morning"] = added_day4_morning
    day4_e["evening"] = added_day4_evening



    #Final result
    return {
        "day1_day": day1_m,
        "day1_night": day1_e,

        "day2_day": day2_m,
        "day2_night": day2_e,

        "day3_day": day3_m,
        "day3_night": day3_e,

        "day4_day": day4_m,
        "day4_night": day4_e

    }
    








def weatherForecastGeoCode(long, latt):
    url_3_days_forcast = f"https://api.weather.com/v3/wx/forecast/daily/3day?geocode={latt},{long}&format=json&units=e&language=en-US&apiKey={apiKey}"
    res =  requests.get(url_3_days_forcast).json()


    lst = [{x: y} for x, y in res.items() if x == "daypart"]
    day_1, day_2, day_3, day_4 = [], [], [], []


    for x, y in lst[0]["daypart"][0].items():

        day1_morning = {x: y[0]}
        day1_evening = {x: y[1]}

        day2_morning = {x: y[2]}
        day2_evening = {x: y[3]}

        day3_morning = {x: y[4]}
        day3_evening = {x: y[5]}

        day4_morning = {x: y[6]}
        day4_evening = {x: y[7]}

        res_1 = {"day1_morning": day1_morning, "day1_evening": day1_evening}
        res_2 = {"day2_morning": day2_morning, "day2_evening": day2_evening}
        res_3 = {"day3_morning": day3_morning, "day3_evening": day3_evening}
        res_4 = {"day4_morning": day4_morning, "day4_evening": day4_evening}

        day_1.append(res_1)
        day_2.append(res_2)
        day_3.append(res_3)
        day_4.append(res_4)


    dayOneMorning, dayOneEvening, dayTwoMorning, dayTwoEvening, dayThreeMorning, dayThreeEvening, dayFourMorning, dayFourEvening = [], [], [], [], [], [], [], []


    for x in day_1:
        val_1m = x["day1_morning"]
        val_1e = x["day1_evening"]

        dayOneMorning.append(val_1m)
        dayOneEvening.append(val_1e)

    for x in day_2:
        val_2m = x["day2_morning"]
        val_2e = x["day2_evening"]

        dayTwoMorning.append(val_2m)
        dayTwoEvening.append(val_2e)

    for x in day_3:
        val_3m = x["day3_morning"]
        val_3e = x["day3_evening"]

        dayThreeMorning.append(val_3m)
        dayThreeEvening.append(val_3e)

    for x in day_4:
        val_4m = x["day4_morning"]
        val_4e = x["day4_evening"]

        dayFourMorning.append(val_4m)
        dayFourEvening.append(val_4e)



    added_day1_morning = {k:v for x in dayOneMorning for k,v in x.items()}
    added_day1_evening = {k:v for x in dayOneEvening for k,v in x.items()}


    added_day2_morning = {k:v for x in dayTwoMorning for k,v in x.items()}
    added_day2_evening = {k:v for x in dayTwoEvening for k,v in x.items()}

    added_day3_morning = {k:v for x in dayThreeMorning for k,v in x.items()}
    added_day3_evening = {k:v for x in dayThreeEvening for k,v in x.items()}

    added_day4_morning = {k:v for x in dayFourMorning for k,v in x.items()}
    added_day4_evening = {k:v for x in dayFourEvening for k,v in x.items()}




    day_1, day_2, day_3, day_4 = [], [], [], []


    for x, y in res.items():
        result_1 = {x: y[0]}
        result_2 = {x: y[1]}
        result_3 = {x: y[2]}
        result_4 = {x: y[3]}

        day_1.append(result_1)
        day_2.append(result_2)
        day_3.append(result_3)
        day_4.append(result_4)

        if x =="validTimeUtc":
            break

    day1_m = {k:v for x in day_1 for k,v in x.items()}
    day1_e = {k:v for x in day_1 for k,v in x.items()}

    day2_m = {k:v for x in day_2 for k,v in x.items()}
    day2_e = {k:v for x in day_2 for k,v in x.items()}


    day3_m = {k:v for x in day_3 for k,v in x.items()}
    day3_e = {k:v for x in day_3 for k,v in x.items()}


    day4_m = {k:v for x in day_4 for k,v in x.items()}
    day4_e = {k:v for x in day_4 for k,v in x.items()}


    day1_m["morning"] = added_day1_morning
    day1_e["evening"] = added_day1_evening

    day2_m["morning"] = added_day2_morning
    day2_e["evening"] = added_day2_evening

    day3_m["morning"] = added_day3_morning
    day3_e["evening"] = added_day3_evening

    day4_m["morning"] = added_day4_morning
    day4_e["evening"] = added_day4_evening



    #Final result
    return {
        "day1_day": day1_m,
        "day1_night": day1_e,

        "day2_day": day2_m,
        "day2_night": day2_e,

        "day3_day": day3_m,
        "day3_night": day3_e,

        "day4_day": day4_m,
        "day4_night": day4_e

    }
    

# weatherForecastGeoCode()