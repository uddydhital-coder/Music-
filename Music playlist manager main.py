#---- Music Playlist Music----

class Playlist:
    #STEP 1 - Parameterized Constructer: runs the moment the playlist is created 

def  __init__(self, name, genre):
    self.name = name
    self.genre = genre
    self.songs = []
    print(f"Playlist '{self.name}'" ({self.genre}) is ready!")


#STEP 2 - Add a song to the playlist
def add_song(self, song):
    self.songs.append(song)
    print(f"'{song}' added to {self.name}.")

#STEP 3- Remove a song from the playlist
def remove_song(self, song):
     if song in self.songs:
     self.songs.remove(song)
     print(f"'{song}'")
     else:
     print(f"'{song}' not found in playlist")


#STEP 4 - Display all songs
def display(self):
print(f"\n---{self.name} ({self.genre})---")
if self.songs:
 for i, song in enumerate(self.songs, 1):
      print(f".   {i}. {song}")
      else:
      print("No songs yet. Add some!")
#STEP 5 - DESTRUCTOR: RUNS AUTOMATICALLY WHEN THE PLAYLIST IS DECTECTED
def __del__(self):
print(f"Playlist '{self.name}' has been deleted. Goodbye!")
#Object Creation (constructor fires here)
my_playlist = Playlist("Road trip mix", "Pop")

#step 6- Menu-driven program using the playlist class
while True:
print("\n. Add song 2. Remove Song 3. View playlist 4. Delete&quit")
choice = input ("Enter your choice:  ")

if choice =="1":
song= input ("Enter song name:  ")
my_playlist.add_song(song)
elif choice =="2"
   song = input("Enter song to remove:  ")
   my_playlist.remove_song(song)
   elif choice== "4":
   del my_playlist #
 
   
