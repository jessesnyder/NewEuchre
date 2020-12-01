from player import Player, LivePlayer
class Team():
    def __init__(self,number):
        self.name = "Team " + str(number)
        self.number = number
        self.score = 0
        self.trickscore = 0
        self.gamescore = 0
        self.bid = 0

        # Bind players as attributes in team to players that exist outside the team. Otherwise, having players bid and play in order seemed too complicated.
        
   
        self.playerA = Players[number-1]
        self.playerB = Players[number+1]
        self.playerA.setpartner(self.playerB)
        self.playerB.setpartner(self.playerA)
        self.playerA.setteam(self)
        self.playerB.setteam(self)
    def setopposingteam(self,team):
        self.playerA.setopposingteam(team)
        self.playerB.setopposingteam(team)