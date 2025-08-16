print ("Mood to Playlist Bot (Kinda)")
print ("So how do u feel right now?")

mood_input = input ("Your mood: ").lower()

#the songs i pick lol but it doesnt direct to their respective links
playlists = {
    "happy": [
        "360 - charli xcx",
        "Accordion - Madvillain",
        "Tick Tock - Joji"
    ],
    "sad":  [
        "Astronomy - Conan Gray",
        "The Scientist – Coldplay",
        "Scott Street - Phoebe Bridgers"
    ],
    "stressed": [
        "Weightless – Marconi Union",
        "hate will never win - XXXTENTACION",
        "Don’t Panic – Coldplay"
    ],
    "tired": [
        "dimeback - Mk.gee",
        "Debold - Vegyn",
	    "Mad Sounds - Arctic Monkeys"
    ],
    "anxious": [
        "what are you so afraid of - XXXTENTACION",
        "Good Guy - Frank Ocean",
        "Sunset Lover – Petit Biscuit"
    ],
    "lonely": [
        "Pluto Projector - Rex Orange County",
        "call me maybe - Devon Hendryx",
        "Talking To The Moon – Bruno Mars"
    ],
    "okay": [
        "Infrunami - Steve Lacy",
        "ANGOSTURA - keshi",
        "BODYGUARD - JPEGMAFIA"
    ]
}

#in case if u wanna add more emotions here then go ahead i guess
if "happy" in mood_input or "good" in mood_input or "excited" in mood_input: 
    mood = "happy"
elif "sad" in mood_input or "upset" in mood_input or "cry" in mood_input:
    mood = "sad"
elif "stress" in mood_input or "nervous" in mood_input or "overwhelmed" in mood_input:
    mood = "stressed"
elif "tired" in mood_input or "sleepy" in mood_input or "exhausted" in mood_input:
    mood = "tired"
elif "anxious" in mood_input or "panic" in mood_input or "overthinking" in mood_input:
    mood = "anxious"
elif "lonely" in mood_input or "alone" in mood_input or "isolated" in mood_input:
    mood = "lonely"
elif "okay" in mood_input or "fine" in mood_input or "normal" in mood_input:
    mood = "okay"
else: 
    mood = None

if mood: 
    print (f"\nNow that you're feeling {mood}, here's yo playlist: ")
    for song in playlists[mood]:
        print(f"- {song}")

else:
    print("\nYeah... Whatever emotion you just said aint in my coding, sorry 😭")