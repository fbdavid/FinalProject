'''
Name:Favion D., Rabbouni M.,Justin R., Kenny A., Raymond A.
Date: 5/17/19
Assignment: Final Project
'''
import csv

def main():
    class Player_stats(): #create class for players

        def __init__(self,Player,DRB,AST,STL,BLK,PTS):
            self.Player = (Player)

            self.DRB = float(DRB) #Turn player stats to floats
            self.AST = float(AST)
            self.STL = float(STL)
            self.BLK = float(BLK)
            self.PTS = float(PTS)

      
            if self.DRB == 0 and self.STL == 0 and self.BLK == 0:
                self.DRB = 0.09
                self.STK = 0.09
                self.BLK = 0.09
            self.score = ((self.PTS * self.AST) / (self.DRB + self.STL + self.BLK)) #Equation for overall player rating/score/


    class main():
        playerlist = []
        teamlist = []
        team2list = []
        team1_rating = []
        total_1 = 0
        team2_rating = []
        total_2 = 0
        with open("NBA_PLAYERS.csv") as f: #Read the dataset
            data = csv.reader(f)
            first = True
            for row in data:
                if first:
                    first = False
                    continue
                #Adds all players and their stats to a list    
                playerlist.append(Player_stats(row[0],row[21],row[23],row[24],row[25],row[28])) 

            #print(len(playerlist))
            #for player in playerlist:
                #print(player.Player + "   Score: " + str(player.score))

        while len(teamlist) < 5:

            inp = input("Enter the name of a player: ")

            matches = [] 

            for player in playerlist:
                if inp.lower() in player.Player.lower():
                    matches.append(player)

            if len(matches) > 1:
                print("We found the following matches... \n")
                for match in matches:
                    print(match.Player)
                print("Please re-enter the full name of the player you would" +\
                "like to add to your team.\n")

            if len(matches) == 1:
                print("Would you like to add " + matches[0].Player + " to your team?")
                print("PTS: " + str(matches[0].PTS) + " AST: " + str(matches[0].AST) +
                        " DRB: " + str(matches[0].DRB) + " STL: " + str(matches[0].STL) +
                        " BLK: " + str(matches[0].BLK))
                inp = input("Y/N?")
                if inp == 'Y' or inp == 'y' or inp == 'yes':
                    teamlist.append(matches[0])
                    print(matches[0].Player + " has been added. \n")
                    print("Player rating is:" + str(matches[0].score))
                    team1_rating.append(matches[0].score)
                    playerlist.remove(matches[0])

            else:
                print("Okay, player wont be added, let's try again.\n")

            if len(matches) == 0:
                print("Sorry, we didn't find any players by that name.\
                Please try again... \n")

        print("Team one roster is filled, Team 2 it's your turn to pick")
        print(" Team rating:" + str(team1_rating))

        for ele in range(0, len(team1_rating)):
            total_1 = total_1 + team1_rating[ele]
        print(total_1)

        while len(team2list) < 5:

            inp = input("Enter the name of a player: ")
            matches = [] #Every player with commonalities is added to this list.

            for player in playerlist:
                if inp.lower() in player.Player.lower():
                    matches.append(player)

            if len(matches) > 1:
                print("We found the following matches... \n")
                for match in matches:
                    print(match.Player)
                print("Please re-enter the full name of the player you would" +\
                "like to add to your team.\n")

            if len(matches) == 1:
                print("Would you like to add " + matches[0].Player + " to your team?")
                print("PTS: " + str(matches[0].PTS) + " AST: " + str(matches[0].AST) +
                        " DRB: " + str(matches[0].DRB) + " STL: " + str(matches[0].STL) +
                        " BLK: " + str(matches[0].BLK))

                inp = input("Y/N?")
                if inp == 'Y' or inp == 'y' or inp == 'yes':
                    team2list.append(matches[0])
                    print(matches[0].Player + " has been added. \n")
                    print("Player rating is:" + str(matches[0].score))
                    team2_rating.append(matches[0].score)

            else:
                print("Okay, player wont be added, let's try again.\n")

            if len(matches) == 0:
                print("Sorry, we didn't find any players by that name.\
                Please try again... \n")
        print("Team 2, your roster is filled, simulation would be complete soon!")
        print("Team Rating:" + str(team2_rating))

        for ele in range(0, len(team2_rating)):
            total_2 = total_2 + team2_rating[ele]
        print(total_2)

        if total_1 > total_2:
            print("TEAM 1 WINS!!")
        else:
            print("TEAM 2 WINS!!")

# used only for testing the code




def stat():

    def main():
        def Player_stats():

            def __init__(self,Player,DRB,AST,STL,BLK,PTS):
                self.Player = (Player)

                self.DRB = float(DRB)
                self.AST = float(AST)
                self.STL = float(STL)
                self.BLK = float(BLK)
                self.PTS = float(PTS)


                if self.DRB == 0 and self.STL == 0 and self.BLK == 0:
                    self.DRB = 0.09
                    self.STK = 0.09
                    self.BLK = 0.09
                self.score = ((self.PTS * self.AST) / (self.DRB + self.STL + self.BLK))



    playerlist = []
    teamlist = []
    team2list = []
    team1_rating = []
    total_1 = 0
    team2_rating = []
    total_2 = 0
    with open("NBA_PLAYERS.csv") as f:
        data = csv.reader(f)
        first = True
        for row in data:
            if first:
                first = False
                continue
            playerlist.append(Player_stats(row[0],row[21],row[23],row[24],row[25],row[28]))


    while len(teamlist) < 5:

        inp = input("Enter the name of a player: ")

        matches = []

        for player in playerlist:
            if inp.lower() in player.Player.lower():
                matches.append(player)

        if len(matches) > 1:
            print("We found the following matches... \n")
            for match in matches:
                print(match.Player)
            print("Please re-enter the full name of the player you would" +\
            "like to add to your team.\n")

        if len(matches) == 1:
            print("Would you like to add " + matches[0].Player + " to your team?")
            print("PTS: " + str(matches[0].PTS) + " AST: " + str(matches[0].AST) +
                    " DRB: " + str(matches[0].DRB) + " STL: " + str(matches[0].STL) +
                    " BLK: " + str(matches[0].BLK))
            inp = input("Y/N?")
            if inp == 'Y' or inp == 'y' or inp == 'yes':
                teamlist.append(matches[0])
                print(matches[0].Player + " has been added. \n")
                print("Player rating is:" + str(matches[0].score))
                team1_rating.append(matches[0].score)
                playerlist.remove(matches[0])

        else:
            print("Okay, player wont be added, let's try again.\n")

        if len(matches) == 0:
            print("Sorry, we didn't find any players by that name.\
            Please try again... \n")

    print("Team one roster is filled, Team 2 it's your turn to pick")
    print(" Team rating:" + str(team1_rating))

    for ele in range(0, len(team1_rating)):
        total_1 = total_1 + team1_rating[ele]
    print(total_1)

    while len(team2list) < 5:

        inp = input("Enter the name of a player: ")
        matches = []

        for player in playerlist:
            if inp.lower() in player.Player.lower():
                matches.append(player)

        if len(matches) > 1:
            print("We found the following matches... \n")
            for match in matches:
                print(match.Player)
            print("Please re-enter the full name of the player you would" +\
            "like to add to your team.\n")

        if len(matches) == 1:
            print("Would you like to add " + matches[0].Player + " to your team?")
            print("PTS: " + str(matches[0].PTS) + " AST: " + str(matches[0].AST) +
                    " DRB: " + str(matches[0].DRB) + " STL: " + str(matches[0].STL) +
                    " BLK: " + str(matches[0].BLK))

            inp = input("Y/N?")
            if inp == 'Y' or inp == 'y' or inp == 'yes':
                team2list.append(matches[0])
                print(matches[0].Player + " has been added. \n")
                print("Player rating is:" + str(matches[0].score))
                team2_rating.append(matches[0].score)

        else:
            print("Okay, player wont be added, let's try again.\n")

        if len(matches) == 0:
            print("Sorry, we didn't find any players by that name.\
            Please try again... \n")
    print("Team 2, your roster is filled, simulation would be complete soon!")
    print("Team Rating:" + str(team2_rating))

    for ele in range(0, len(team2_rating)):
        total_2 = total_2 + team2_rating[ele]
    print(total_2)

    if total_1 > total_2:
        print("TEAM 1 WINS!!")
    else:
        print("TEAM 2 WINS!!")




def test_final():
    assert stat() == True
    assert stat() == False


if __name__ == '__main__':
    main()


