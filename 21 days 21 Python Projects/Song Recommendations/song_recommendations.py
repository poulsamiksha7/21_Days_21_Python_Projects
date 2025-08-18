import webbrowser

bollywood_songs={
    "happy":[
        ("Kala Chashma","https://youtu.be/k4yXQkG2s1E?si=dPwz_3IlPwDAo61R"),
        ("Badtameez Dil","https://youtu.be/II2EO3Nw4m0?si=MDMVUMfpuMt6qAt6"),
        ("Agar Tum Saath Ho","https://youtu.be/xRb8hxwN5zc?si=yV_f5hAOm1ohWqlo"),
        ("Laal pari","https://youtu.be/KGn-erOG-Bs?si=2Y2ZJqDznD7z0iLJ")
    ],
    "romantic":[
        ("Tum Hi Ho","https://youtu.be/Umqb9KENgmk?si=Hu0eDNImLrngTG50"),
        ("Raabta","https://youtu.be/iYy9kr45d1o?si=A7wtGB3qzSfcvULQ"),
        ("Tera Ban Jaunga","https://youtu.be/Qdz5n1Xe5Qo?si=ZiC7cf9DZZdGoVY1")
    ],
    "energetic":[
        ("Malhari","https://youtu.be/l_MyUGq7pgs?si=jU6tOXh4sW02wuHK"),
        ("Jai Jai Shivshankar","https://youtu.be/oGneAab3e88?si=_4FhlxcouyQQfi93"),
        ("Zinda","https://youtu.be/Ax0G_P2dSBw?si=PWYNL0JF8vwAudZo")
    ]
}

print("🎵 Welcome to Bollywood Song Recommender🎵")
print("Available moods:happy,sad,romantic,energetic")
mood=input("Enter your current mood: ").lower()

if mood in bollywood_songs:
    print(f"\n Here are some {mood} songs for you:\n")
    songs=bollywood_songs[mood]
    for idx,(title,url) in enumerate(songs,1):
        print(f"{idx}.{title}")

    choice=input("\n Enter the number of the song you want to play (1-3): ")
    if choice in ["1","2","3"]:
        song_url=songs[int(choice)-1] [1]
        print(f"\n Opening: {songs[int(choice)-1][0]}🎵")   
        webbrowser.open(song_url)
    else:
        print("Invalid Choice")
else:
    print("Sorry, we don't have songs for that mood...")        