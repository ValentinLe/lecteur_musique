
from util.ListFile import listFile
from model.Song import Song

if __name__ == "__main__":
    l = listFile("C:/Users/Val/Desktop/Dossier/musiques")
    for file in l:
        song = Song(file)
        print(song)
