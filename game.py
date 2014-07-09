import csv
import random
from player import Player

class Game:
    def __init__(self):
        self.terrains = {}
        self.players = {}
        self.continueGame = True
        self.playerList = {0:'ump',1:'fn', 2:'ps', 3:'communistes'}
        self.tour = 0
        with open('datas/themes.csv', 'r') as f:
            reader = csv.DictReader(f, delimiter=',')
            for line in reader:
                self.terrains[line["id_theme"]] = {'type':line["type"],'name':line["name"], 'bonus': line["bonus"], 'malus':line["malus"], 'description':line["description"]}

    #Combat de deux cartes entre elles
    def fight(self, player1, player2, card1, card2):
        if(card1.power > card2.defense):
            winCard = card1
            loseCard = card2
            winner = player1
        else:
            winCard = card2
            loseCard = card1
            winner = player2
        #
        loseCard.popularity = winCard.power - loseCard.defense
        winner.popularity += 2

    # Create the new players
    def setPlayers(self):
        print("Veuillez saisir le chiffre correspondant à un des parti")
        playCanStart = False
        while(playCanStart==False):
            self.showPlayersAvaible()
            player1 = int(input("Joueur 1:Quel parti politique souhaitez-vous choisir ? "))
            if player1 in self.playerList:
                self.players[0] = Player(self.playerList[player1])
                print("\n ----> Joueur 1, vous avez choisi : " +self.players[0].name + "\n")
                playCanStart = True
            else:
                print("Il faut choisir parmis les personnages existants" + player1)
        #
        playCanStart = False
        while(playCanStart == False):
            self.showPlayersAvaible()
            player2= int(input("Joueur 2:Quel parti politique souhaitez-vous choisir ? "))
            if player2  in self.playerList:
                self.players[1] = Player(self.playerList[player2])
                print("\n ----> Joueur 2, vous avez choisi:" + self.players[1].name + "\n")
                playCanStart = True
            else:
                print("Il faut choisir parmis les personnages existants")
        #
    #
    def showPlayersAvaible(self):
        for x in range(len (self.playerList)):
            current = self.playerList[x]
            print (str(x)+" -- " +str(current))

    #Show scores
    def showScores(self):
        print("Intentions de vote:")
        for x in range(len(self.players)):
            currentPlayer = self.players[x]
            print(currentPlayer.name + ":" +str(currentPlayer.popularity) +"%")

    #
    def startGame(self):
        # Tour par tour
        while(self.continueGame == True):
            currentPlayer = self.tour % 2
            player = self.players[currentPlayer]

            #Quand les deux ont joués on invoque un nouveau terrain
            if( ( self.tour % 2 ) == 0):
                self.getTheme()

            #
            print("- Tour " + str(self.tour) + " -----------------\n")
            print("Votre popularité actuelle : " + str(player.popularity) +"%")
            print("Hey "+player.name+", a ton tour, voici ta main -------\n")
            player.hand.getHand()

            card = int(input("Quel carte compte tu jouer ? "))
            print("Tu as joué")

            #ICI LES ATTAQUESSSSSSS

            if (player.popularity >= 100 or player.popularity <= 0):
                self.continueGame = False
            #Next
            self.tour += 1

    # Timer for linux/mac
    def getTheme(self):
        rd = random.choice(list( self.terrains.keys() ) )
        print("\n - 000000000 THEME : ")
        print(str(self.terrains[rd])+ "\n")
