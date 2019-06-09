
from model.Board import Board

if __name__ == "__main__":
    path = "C:/Users/Val/Desktop/Dossier/testLecteur"
    b = Board()
    b.addSongOfDirectory(path)
    print(b)
