# import pyttsx3

# # Define your voice_alerts dictionary
# voice_alerts = {
#     "200m": "You are approaching a 200 meters sign.",
#     "50-100m": "Caution! 50 to 100 meters ahead.",
#     "Ahead-Left": "Prepare for a left turn ahead.",
#     "Ahead-Right": "Prepare for a right turn ahead.",
#     "Axle-load-limit": "Axle load limit ahead.",
#     "Barrier Ahead": "There's a barrier ahead.",
#     "Bullock Cart Prohibited": "Bullock carts are prohibited.",
#     "Cart Prohobited": "Carts are prohibited.",
#     "Cattle": "Cattle on the road. Drive with caution.",
#     "Compulsory Ahead": "You must go straight ahead.",
#     "Compulsory Keep Left": "Keep left. It's compulsory.",
#     "Compulsory Left Turn": "You must turn left.",
#     "Compulsory Right Turn": "You must turn right.",
#     "Cross Road": "A crossroad is coming up.",
#     "Cycle Crossing": "Watch out for cyclists at the crossing.",
#     "Compulsory Cycle Track": "You must use the cycle track.",
#     "Cycle Prohibited": "Cycling is prohibited here.",
#     "Dangerous Dip": "Caution! Dangerous dip ahead.",
#     "Falling Rocks": "Beware of falling rocks.",
#     "Ferry": "A ferry crossing is ahead.",
#     "Gap in median": "There's a gap in the median ahead.",
#     "Give way": "Give way to other vehicles.",
#     "Hand cart prohibited": "Handcarts are prohibited.",
#     "Height limit": "Height limit ahead. Check your vehicle's height.",
#     "Horn prohibited": "No horn allowed in this area.",
#     "Humpy Road": "Caution! Humpy road ahead.",
#     "Left hair pin bend": "Prepare for a hairpin left turn.",
#     "Left hand curve": "Expect a left-hand curve ahead.",
#     "Left Reverse Bend": "Prepare for a reverse left bend.",
#     "Left turn prohibited": "Left turns are prohibited.",
#     "Length limit": "Length limit ahead. Check your vehicle's length.",
#     "Load limit 5T": "Maximum load limit is 5 tons.",
#     "Loose Gravel": "Caution! Loose gravel on the road.",
#     "Major road ahead": "A major road is coming up ahead.",
#     "Men at work": "Be cautious, men are working on the road.",
#     "Motor vehicles prohibited": "Motor vehicles are prohibited.",
#     "Nrrow bridge": "Narrow bridge ahead.",
#     "Narrow road ahead": "The road narrows ahead.",
#     "Straight prohibited": "No straight driving allowed.",
#     "No parking": "Parking is prohibited here.",
#     "No stoping": "No stopping allowed.",
#     "One way sign": "This is a one-way road.",
#     "Overtaking prohibited": "Overtaking is not allowed here.",
#     "Pedestrian crossing": "Watch out for pedestrians at the crossing.",
#     "Pedestrian prohibited": "Pedestrians are prohibited.",
#     "Restriction ends sign": "The previous restriction has ended.",
#     "Right hair pin bend": "Prepare for a hairpin right turn.",
#     "Right hand curve": "Expect a right-hand curve ahead.",
#     "Right Reverse Bend": "Prepare for a reverse right bend.",
#     "Right turn prohibited": "Right turns are prohibited.",
#     "Road wideness ahead": "Road widens ahead.",
#     "Roundabout": "Approaching a roundabout.",
#     "School ahead": "Be cautious, school ahead.",
#     "Side road left": "Expect a side road on the left.",
#     "Side road right": "Expect a side road on the right.",
#     "Slippery road": "Caution! The road is slippery.",
#     "Compulsory sound horn": "Horn is compulsory.",
#     "Speed limit": "Speed limit enforced.",
#     "Staggred intersection": "Prepare for a staggered intersection.",
#     "Steep ascent": "Caution! Steep ascent ahead.",
#     "Steep descent": "Caution! Steep descent ahead.",
#     "Stop": "Stop! Complete stop required.",
#     "Tonga prohibited": "Tongas are prohibited.",
#     "Truck prohibited": "Trucks are prohibited.",
#     "Compulsory turn left ahead": "You must turn left ahead.",
#     "Compulsory right turn ahead": "You must turn right ahead.",
#     "T-intersection": "Prepare for a T-intersection.",
#     "U-turn prohibited": "U-turns are prohibited.",
#     "Vehicle prohibited in both directions": "No entry for vehicles in both directions.",
#     "Width limit": "Width limit ahead. Check your vehicle's width.",
#     "Y-intersection": "Prepare for a Y-intersection.",
#     "Sign_C": "C-sign ahead.",
#     "Sign_T": "T-sign ahead.",
#     "Sign_S": "S-sign ahead.",
#     "No entry": "No entry! Do not proceed.",
#     "Compulsory Keep Right": "Keep right. It's compulsory.",
#     "Parking": "You can park here."
# }

# # Initialize the pyttsx3 engine
# engine = pyttsx3.init()
# engine.setProperty('voice', 'english_rp+f3')
# engine.setProperty('rate', 200)  # Adjust speech rate (words per minute)


# # Function to generate voice alerts
# def generate_voice_alert(alert):
#     engine.say(voice_alerts[alert])
#     engine.runAndWait()

# # Function to display voice alert menu
# def display_alert_menu():
#     print("Voice Alert Menu:")
#     for i, (sign_name, alert_message) in enumerate(voice_alerts.items(), 1):
#         print(f"{i}. {sign_name}: {alert_message}")





# voice_alert_system.py

import os
from gtts import gTTS
from playsound import playsound

from english_alerts import english_alerts
from marathi_alerts import marathi_alerts
from hindi_alerts import hindi_alerts

# Languages list
languages = ["en", "mr", "hi"]

# Define your voice_alerts list of dictionaries
voice_alerts = [
    {"en": english_alerts},
    {"mr": marathi_alerts},
    {"hi": hindi_alerts}
]

def generate_voice_alert(language_index, sign_name):
    language_dict = voice_alerts[language_index]
    language_name = list(language_dict.keys())[0]
    
    language_alerts = language_dict[language_name]
    alert_message = language_alerts[sign_name]
    
    speech = gTTS(text = alert_message,
                lang = language_name, 
                slow = False)
    speech.save('speech.mp3')
    playsound('speech.mp3',True)
    os.remove('speech.mp3')


def display_alert_menu():
    print("Select language:")
    for i, language_dict in enumerate(voice_alerts, start=1):
        language_name = list(language_dict.keys())[0]
        print(f"{i}. {language_name}")


def get_language_name(index):
    return list(voice_alerts[index - 1].keys())[0]


