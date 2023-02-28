from albums import bladee

artists = ["bladee", "ecco2k", "tyler, the creator", "thaiboy digital", "yung lean"]
artist = input("Insert a musical artist (Make sure spelling and punctuation is correct): ")
if(artist.strip().lower() in artists):
    album = input("I know that artist! Name an album from them: ")
else:
    print("Sorry, I don't know that one.")