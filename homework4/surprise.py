# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "-16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "-08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def star_names(targets):
    for key in targets:
        print(key)

star_names(targets)

# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def star_names_and_types(targets):
    for key in targets:
        for info in targets[key]:
            if info == "Spectral Type":
                print(key, targets[key][info])

star_names_and_types(targets)

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def magnitude_sorter(targets):
    for key in targets:
        if targets[key]["Magnitude"] > 0.1 :
            print(key)
magnitude_sorter(targets)

# 4) Look up another target, add all the necessary information to the targets list. 
targets["Altair"] = {
    "RA":  "19h 50m 47s",
    "Dec": "+08° 52′ 05.96″",
    "Magnitude": "0.76",
    "Spectral Type": "A7Vn"
}

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def bright_star_sorter(targets):
    def parse_dec(dec_str):
        if dec_str.strip()[0] == '+':
            sign = 1
        else:
            sign = -1
        parts = dec_str.replace('°', ' ').replace('′', ' ').replace('″', '').split() 
        degrees, minutes, seconds = map(float, parts[:3])
        return sign * (degrees + minutes / 60 + seconds / 3600)
    
    closest_star= None
    closest_diff = float('inf')

    for star, info in targets.items():
        dec_deg = parse_dec(info["Dec"])
        diff = abs(20 - (-dec_deg))        

        if closest_star is None or diff < closest_diff or diff == closest_diff and info["Magnitude"] < targets[closest_star]["Magnitude"]:
            closest_diff = diff
            closest_star = star
    print(closest_star)

bright_star_sorter(targets)

#this was a mess of me searching things up, putting things together, and fixing things very randomly. im sorry that it's so incoherent but it works!

# 6) What is your favorite constellation?
#Scorpius bc I can always see it clearly outside my bedroom during the summer
