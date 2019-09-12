import csv


def ret_num(f, s, t):
    bi = str(f) + str(s) + str(t)
    return int(bi,2)
def main(year):
    new_data = []
    appendfile=open(str(year)+'-outappend.csv','wb')
    appendfile = csv.writer(appendfile)

    new_data.append(["Stirke Count", "Ball Count", "Pitch Count", "Strike/Ball", "Outs", "Inning", "Slugging Current ", 
        "OBP Current", "OPS Curent", "Slugging Average", "OBP Average", "OPS Average", "Runs", "Hits", "Walks", "Strike-Outs", "Home-runs", "Bases",
        "Home Or Away", "Park League", "Batter Contact Percentage", "BCP Average", "Game Number", "Team Losses", "Team Wins",
        "Team Win Loss Percentage", "Slugging Next", "OBP Next", "OPS Next", "Friendly Score", "Pitcher's Team","Opposing Team",
        "Year", "Stadium Location", "Winning", "Batter Number"])
    appendfile.writerow(["L"])
    pitcher1 = ''
    pitcher2 = ''
    game = -1

    count = 0
    strikes1 = 0
    strikes2 = 0
    balls1 = 0
    balls2 = 0
    bs1 = 0
    bs2 = 0
    pitchc1 = 0
    pitchc2 = 0
    outs = 0
    inning = 1
    slg = 0.0
    obp = 0.0
    ops = 0.0
    runs = 0
    hits1 = 0
    hits2 = 0
    walks1 = 0
    walks2 = 0
    so1 = 0
    so2 = 0
    hra1 = 0
    hra2 = 0
    play = ''
    onbase = ''
    first = 0
    second = 0
    third = 0
    hold_num = 0
    slg2= 0
    obp2= 0
    ops2= 0
    slg1= 0
    obp1= 0
    ops1= 0
    bcp1=0
    bcp2=0
    team1=0
    team2=0
    ParkLeague=0
    stadiumloc=0
    winning1=0
    winning2=0
    Team_List=[]
    StadiumList=[]

    with open(str(year)+'.csv', 'rb') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            if count == 0:
                count = count + 1
                continue
            if game != int(row[2]):
                game = int(row[2])
                if game != 0:
                    strikes1 = 0
                    strikes2 = 0
                    balls1 = 0
                    balls2 = 0
                    bs1 = 0.0
                    bs2 =0.0
                    pitchc1 = 0
                    pitchc2 = 0
                    inning = 1
                    hits1 = 0
                    hits2 = 0
                    walks1 = 0
                    walks2 = 0
                    so1 = 0
                    so2 = 0
                    hra1 = 0
                    hra2 = 0
                    slg2= 0
                    obp2= 0
                    ops2= 0
                    slg1= 0
                    obp1= 0
                    ops1= 0
                    bcp1=0
                    bcp2=0
                    ParkLeague=0
                    team1=0
                    team2=0
                    stadiumloc=0
                    winning1=0
                    winning2=0

                if row[27] not in Team_List:
                    Team_List.append(row[27])
                if row[0] not in Team_List:
                    Team_List.append(row[0])
                team1=Team_List.index(row[27])
                team2=Team_List.index(row[0])

                if row[25] not in StadiumList:
                    StadiumList.append(row[25])
                stadiumloc=StadiumList.index(row[25])

                if row[26]=="NL":
                    ParkLeague=0
                else:
                    ParkLeague=1

                pitcher1 = row[4]
                pitcher2 = ''

            if pitcher1 != row[4] and game == int(row[2]) and pitcher2 == '':
                pitcher2 = row[4]

            onbase = row[14]
            play = row[15]

            if row[4] == pitcher1:
                if int(row[7])>100 or int(row[6])>100:
                    continue
                strikes1 = strikes1  + (int(row[7]) - int(row[6]))
                balls1 = balls1 + int(row[6])
                pitchc1 = pitchc1 + int(row[7])

                try:
                    bs1 = float(strikes1) / float(balls1)
                except:
                    bs2 = float(strikes2)

                outs = int(row[8])
                inning = int(row[9])
                slg1+= float(row[10])
                obp1+= float(row[11])
                ops1+= float(row[12])
                runs = int(row[13])


                if 'Single' in play or 'Double' in play or 'Triple' in play or ('Bunt' in play and 'out' not in play):
                    hits1 = hits1 + 1
                if 'Walk' in play or 'Hit By' in play:
                    walks1 = walks1 + 1
                if 'Strikeout' in play:
                    so1 = so1 + 1
                if 'Home' in play or 'Grand' in play or 'grand' in play:
                    hra1 = hra1 + 1

                if '1' in onbase:
                    first = 1
                else:
                    first = 0
                if '2' in onbase:
                    second = 1
                else:
                    second = 0
                if '3' in onbase:
                    third = 1
                else:
                    third = 0
                if "Flyball" in play or "out" in play or "Pop" in play:
                     outs+=1
                elif "Double Play" in play:
                    outs+=2
                elif "Triple Play" in play:
                    outs+=3
                slg11=slg1/(float(row[3])*1.0)
                ops11=ops1/(float(row[3])*1.0)
                obp11=obp1/(float(row[3])*1.0)
                if float(row[11])==999:
                    continue
                hold_num = ret_num(first, second, third)


                bcp1+=float((1.0*float(row[17])/(pitchc1*1.0)))
                bcp11=bcp1/(float(row[3])*1.0)
                
                if(int(row[29])>int(row[28])):
                    winning1=1
                else:
                    winning1=0
                new_data.append([strikes1, balls1, pitchc1, bs1, outs, inning, float(row[10]), 
                    float(row[11]), float(row[12]), slg11, obp11, ops11, runs, hits1, walks1, so1, hra1, hold_num,
                    int(row[16]), ParkLeague, float((1.0*float(row[17])/(pitchc1*1.0))), bcp11, int(row[21]), int(row[20]), int(row[19]),
                    float((float(row[20])*1.0)/(float(row[21])*1.0)), float(row[22]), float(row[23]),float(row[24]),int(row[29]), team1, team2,
                    int(row[1]), stadiumloc, winning1, int(row[3])]) 




                '''
                    CREATE TABLE "PlateAppearance" (
                    0"Team" VARCHAR(3) NOT NULL, 
                    1"Year" INTEGER NOT NULL, 
                    2"Game_Number" INTEGER NOT NULL, 
                    3"Batter_Number" INTEGER NOT NULL, 
                    4"Pitcher" VARCHAR(40), 
                    5"Strike" INTEGER, 
                    6"Ball" INTEGER, 
                    7"Pitches" INTEGER, 
                    8"Outs" INTEGER, 
                    9"Inning" INTEGER, 
                    10"Slugging" FLOAT, 
                    11"Obp" FLOAT, 
                    12"Ops" FLOAT, 
                    13"Runs" INTEGER, 
                    14"Bases" VARCHAR(3), 
                    15"Outcome" VARCHAR(120), 
                    16"Home_Or_Away" INTEGER, 
                    17"Batter_Contact" INTEGER, 
                    18"Pitcher_Game_Number" INTEGER, 
                    19"Team_Losses" INTEGER, 
                    20"Team_Wins" INTEGER, 
                    21"Team_Game_Number" INTEGER, 
                    22"Next_Slugging" FLOAT, 
                    23"Next_Obp" FLOAT, 
                    24"Next_Ops" FLOAT, 
                    25"Home_Stadium" VARCHAR(3), 
                    26"Home_Park_League" VARCHAR(2), 
                    27"Team_Name" VARCHAR(3), 
                    28"Opposing_Score" INTEGER, 
                    29"Friendly_Score" INTEGER, 
                    PRIMARY KEY ("Team", "Year", "Game_Number", "Batter_Number")
                    );
                '''


            


            if row[4] == pitcher2:
                if int(row[7])>100 or int(row[6])>100:
                    continue
                strikes2 = strikes2  + (int(row[7]) - int(row[6]))
                balls2 = balls2 + int(row[6])
                pitchc2 = pitchc2 + int(row[7])

                try:
                    bs2 = float(strikes2) / float(balls2)
                except:
                    bs2 = float(strikes2)

                outs = int(row[8])
                inning = int(row[9])
                slg2+= float(row[10])
                obp2+= float(row[11])
                ops2+= float(row[12])
                runs = int(row[13])

                if 'Single' in play or 'Double' in play or 'Triple' in play or ('Bunt' in play and 'out' not in play):
                    hits2 = hits2 + 1
                if 'Walk' in play or 'Hit By' in play:
                    walks2 = walks2 + 1
                if 'Strikeout' in play:
                    so2 = so2 + 1
                if 'Home' in play or 'Grand' in play or 'grand' in play:
                    hra2 = hra2 + 1

                if '1' in onbase:
                    first = 1
                else:
                    first = 0
                if '2' in onbase:
                    second = 1
                else:
                    second = 0
                if '3' in onbase:
                    third = 1
                else:
                    third = 0
                if "Flyball" in play or "out" in play or "Pop" in play:
                     outs+=1
                elif "Double Play" in play:
                    outs+=2
                elif "Triple Play" in play:
                    outs+=3
                slg22=slg2/(float(row[3])*1.0)
                ops22=ops2/(float(row[3])*1.0)
                obp22=obp2/(float(row[3])*1.0)
                if float(row[11])==999:
                    continue
                hold_num = ret_num(first, second, third)

                bcp2+=float((1.0*float(row[17]))/(pitchc2*1.0))
                bcp22=bcp2/(float(row[3])*1.0)
                
                if(int(row[29])>int(row[28])):
                    winning2=1
                else:
                    winning2=0


                new_data.append([strikes2, balls2, pitchc2, bs2, outs, inning, float(row[10]), 
                    float(row[11]), float(row[12]), slg22, obp22, ops22, runs, hits2, walks2, so2, hra2, hold_num,
                    int(row[16]), ParkLeague, float((1.0*float(row[17]))/(pitchc2*1.0)), bcp22, int(row[21]), int(row[20]), int(row[19]),
                    float((float(row[20])*1.0)/(float(row[21])*1.0)), float(row[22]), float(row[23]),float(row[24]),int(row[29]), team2, team1,
                    int(row[1]), stadiumloc, winning2, int(row[3])]) 
            appendfile.writerow(row)





    with open(str(year)+"-Data1.csv", "wb") as csv_file:
        writer = csv.writer(csv_file)
        for line in new_data:
            writer.writerow(line)

if __name__ == '__main__':
    for year in range(2007,2018):
        main(year)
