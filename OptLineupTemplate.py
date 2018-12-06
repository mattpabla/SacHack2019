import json

def main():

    with open('ENTER .JSON EFILE HERE') as data:    
                Stats = json.load(data)

                #Getting a list of all players
                init_gamertag = []
                gamertag = []
                for dct in Stats:
                    init_gamertag.append(dct["FIELD4"])
                for i in init_gamertag:
                  if i not in gamertag:
                      gamertag.append(i)

                print(gamertag)

                #initalizing each position to its max value 
                PG = 100
                SG = 100
                SF = 100
                PF = 100
                C = 100
                
                #Create a dictionary for each player with a value of a list that will be containing...
                #... PG=index0, SG=index1, SF=index2, PF=index3, C=index4
                P1 = {gamertag[1]: [0,0,0,0,0]}
                P2 = {gamertag[2]: [0,0,0,0,0]}
                P3 = {gamertag[3]: [0,0,0,0,0]}
                P4 = {gamertag[4]: [0,0,0,0,0]}
                P5 = {gamertag[5]: [0,0,0,0,0]}
                
                #STATS FOR PLAYER 1
                for dct in Stats:
                    if (gamertag[1] == dct["FIELD4"]) and (dct["FIELD5"] == "ENTER WHAT SEASON STATS YOU WANT HERE"):
                        #PG Check
                        if ((float(dct["FIELD43"].strip(' \t\n\r%'))) < 40):
                            PG = PG - 10
                        if ((float(dct["FIELD35"])) < 1.5):
                            PG = PG - 10
                        if ((float(dct["FIELD33"])) < 3):
                            PG = PG - 10
                        if ((float(dct["FIELD34"])) > 3):
                            PG = PG - 10
                        if ((float(dct["FIELD41"])) < 8):
                            PG = PG - 10
                        P1[gamertag[1]][0] = PG

                        #SG Check
                        if ((float(dct["FIELD41"])) < 10):
                            SG = SG - 10
                        if ((float(dct["FIELD33"])) > 4):
                            SG = SG - 10
                        if ((float(dct["FIELD38"])) > 7):
                            SG = SG - 10
                        if ((float(dct["FIELD34"])) < 2):
                            SG = SG - 10
                        P1[gamertag[1]][1] = SG

                        #SF Check
                        if ((float(dct["FIELD33"])) < 3) or ((float(dct["FIELD33"])) >7):
                            SF = SF - 10
                        if ((float(dct["FIELD38"])) < 3 or (float(dct["FIELD38"]))>7):
                            SF = SF - 10
                        if ((float(dct["Per Game Stats"])) < 12):
                            SF = SF - 10
                        if ((float(dct["FIELD12"])) < 2):
                            SF = SF - 10
                        P1[gamertag[1]][2] = SF

                        #PF Check
                        if ((float(dct["FIELD40"])) < 4):
                            PF = PF - 10
                        if ((float(dct["FIELD12"])) < 1):
                            PF = PF - 10
                        if ((float(dct["FIELD48"])) > 7):
                            PF = PF - 10
                        if ((float(dct["FIELD39"])) < 4):
                            PF = PF - 10
                        P1[gamertag[1]][3] = PF
                    
                        #C Check
                        if ((float(dct["FIELD12"])) < 2):
                            C = C - 10
                        if (float(dct["FIELD43"].strip(' \t\n\r%'))) < 60:
                            C = C - 10
                        if ((float(dct["FIELD40"])) < 4):
                            C = C - 10
                        if ((float(dct["FIELD39"])) < 4):
                            C = C - 10                    
                        P1[gamertag[1]][4] = PF

                #STATS FOR PLAYER 2
                    #Refresh Values     
                    PG = 100
                    SG = 100
                    SF = 100
                    PF = 100
                    C = 100
                    if (gamertag[2] == dct["FIELD4"]) and (dct["FIELD5"] == "ENTER WHAT SEASON STATS YOU WANT HERE"):
                        #PG Check
                        if ((float(dct["FIELD43"].strip(' \t\n\r%'))) < 40):
                            PG = PG - 10
                        if ((float(dct["FIELD35"])) < 1.5):
                            PG = PG - 10
                        if ((float(dct["FIELD33"])) < 3):
                            PG = PG - 10
                        if ((float(dct["FIELD34"])) > 3):
                            PG = PG - 10
                        if ((float(dct["FIELD41"])) < 8):
                            PG = PG - 10
                        P2[gamertag[2]][0] = PG

                        #SG Check
                        if ((float(dct["FIELD41"])) < 10):
                            SG = SG - 10
                        if ((float(dct["FIELD33"])) > 4):
                            SG = SG - 10
                        if ((float(dct["FIELD38"])) > 7):
                            SG = SG - 10
                        if ((float(dct["FIELD34"])) < 2):
                            SG = SG - 10
                        P2[gamertag[2]][1] = SG

                        #SF Check
                        if ((float(dct["FIELD33"])) < 3) or ((float(dct["FIELD33"])) >7):
                            SF = SF - 10
                        if ((float(dct["FIELD38"])) < 3 or (float(dct["FIELD38"]))>7):
                            SF = SF - 10
                        if ((float(dct["Per Game Stats"])) < 12):
                            SF = SF - 10
                        if ((float(dct["FIELD12"])) < 2):
                            SF = SF - 10
                        P2[gamertag[2]][2] = SF

                        #PF Check
                        if ((float(dct["FIELD40"])) < 4):
                            PF = PF - 10
                        if ((float(dct["FIELD12"])) < 1):
                            PF = PF - 10
                        if ((float(dct["FIELD48"])) > 7):
                            PF = PF - 10
                        if ((float(dct["FIELD39"])) < 4):
                            PF = PF - 10
                        P2[gamertag[2]][3] = PF
                    
                        #C Check
                        if ((float(dct["FIELD12"])) < 2):
                            C = C - 10
                        if (float(dct["FIELD43"].strip(' \t\n\r%'))) < 60:
                            C = C - 10
                        if ((float(dct["FIELD40"])) < 4):
                            C = C - 10
                        if ((float(dct["FIELD39"])) < 4):
                            C = C - 10                    
                        P2[gamertag[2]][4] = PF

                #STATS FOR PLAYER 3
                    #Refresh Values     
                    PG = 100
                    SG = 100
                    SF = 100
                    PF = 100
                    C = 100
                    if (gamertag[3] == dct["FIELD4"]) and (dct["FIELD5"] == "RENTER WHAT SEASON STATS YOU WANT HERE"):
                        #PG Check
                        if ((float(dct["FIELD43"].strip(' \t\n\r%'))) < 40):
                            PG = PG - 10
                        if ((float(dct["FIELD35"])) < 1.5):
                            PG = PG - 10
                        if ((float(dct["FIELD33"])) < 3):
                            PG = PG - 10
                        if ((float(dct["FIELD34"])) > 3):
                            PG = PG - 10
                        if ((float(dct["FIELD41"])) < 8):
                            PG = PG - 10
                        P3[gamertag[3]][0] = PG

                        #SG Check
                        if ((float(dct["FIELD41"])) < 10):
                            SG = SG - 10
                        if ((float(dct["FIELD33"])) > 4):
                            SG = SG - 10
                        if ((float(dct["FIELD38"])) > 7):
                            SG = SG - 10
                        if ((float(dct["FIELD34"])) < 2):
                            SG = SG - 10
                        P3[gamertag[3]][1] = SG

                        #SF Check
                        if ((float(dct["FIELD33"])) < 3) or ((float(dct["FIELD33"])) >7):
                            SF = SF - 10
                        if ((float(dct["FIELD38"])) < 3 or (float(dct["FIELD38"]))>7):
                            SF = SF - 10
                        if ((float(dct["Per Game Stats"])) < 12):
                            SF = SF - 10
                        #if ((float(dct["FIELD12"])) == ):
                        if(True):
                            SF = SF - 10
                        P3[gamertag[3]][2] = SF

                        #PF Check
                        if ((float(dct["FIELD40"])) < 4):
                            PF = PF - 10
                        #if ((float(dct["FIELD12"])) < 1):
                        if(True):
                            PF = PF - 10
                        if ((float(dct["FIELD48"])) > 7):
                            PF = PF - 10
                        if ((float(dct["FIELD39"])) < 4):
                            PF = PF - 10
                        P3[gamertag[3]][3] = PF
                    
                        #C Check
                        #if ((float(dct["FIELD12"])) < 2):
                        if(True):
                            C = C - 10
                        if (float(dct["FIELD43"].strip(' \t\n\r%'))) < 60:
                            C = C - 10
                        if ((float(dct["FIELD40"])) < 4):
                            C = C - 10
                        if ((float(dct["FIELD39"])) < 4):
                            C = C - 10                    
                        P3[gamertag[3]][4] = PF


                #STATS FOR PLAYER 4
                    #Refresh Values     
                    PG = 100
                    SG = 100
                    SF = 100
                    PF = 100
                    C = 100
                    if (gamertag[4] == dct["FIELD4"]) and (dct["FIELD5"] == "ENTER WHAT SEASON STATS YOU WANT HERE"):
                        #PG Check
                        if ((float(dct["FIELD43"].strip(' \t\n\r%'))) < 40):
                            PG = PG - 10
                        if ((float(dct["FIELD35"])) < 1.5):
                            PG = PG - 10
                        if ((float(dct["FIELD33"])) < 3):
                            PG = PG - 10
                        if ((float(dct["FIELD34"])) > 3):
                            PG = PG - 10
                        if ((float(dct["FIELD41"])) < 8):
                            PG = PG - 10
                        P4[gamertag[4]][0] = PG

                        #SG Check
                        if ((float(dct["FIELD41"])) < 10):
                            SG = SG - 10
                        if ((float(dct["FIELD33"])) > 4):
                            SG = SG - 10
                        if ((float(dct["FIELD38"])) > 7):
                            SG = SG - 10
                        if ((float(dct["FIELD34"])) < 2):
                            SG = SG - 10
                        P4[gamertag[4]][1] = SG

                        #SF Check
                        if ((float(dct["FIELD33"])) < 3) or ((float(dct["FIELD33"])) >7):
                            SF = SF - 10
                        if ((float(dct["FIELD38"])) < 3 or (float(dct["FIELD38"]))>7):
                            SF = SF - 10
                        if ((float(dct["Per Game Stats"])) < 12):
                            SF = SF - 10
                        if ((float(dct["FIELD12"])) < 2):
                            SF = SF - 10
                        P4[gamertag[4]][2] = SF

                        #PF Check
                        if ((float(dct["FIELD40"])) < 4):
                            PF = PF - 10
                        if ((float(dct["FIELD12"])) < 1):
                            PF = PF - 10
                        if ((float(dct["FIELD48"])) > 7):
                            PF = PF - 10
                        if ((float(dct["FIELD39"])) < 4):
                            PF = PF - 10
                        P4[gamertag[4]][3] = PF
                    
                        #C Check
                        if ((float(dct["FIELD12"])) < 2):
                            C = C - 10
                        if (float(dct["FIELD43"].strip(' \t\n\r%'))) < 60:
                            C = C - 10
                        if ((float(dct["FIELD40"])) < 4):
                            C = C - 10
                        if ((float(dct["FIELD39"])) < 4):
                            C = C - 10                    
                        P4[gamertag[4]][4] = PF

                #STATS FOR PLAYER 5
                    #Refresh Values     
                    PG = 100
                    SG = 100
                    SF = 100
                    PF = 100
                    C = 100
                    if (gamertag[5] == dct["FIELD4"]) and (dct["FIELD5"] == "ENTER WHAT SEASON STATS YOU WANT HERE"):
                        #PG Check
                        if ((float(dct["FIELD43"].strip(' \t\n\r%'))) < 40):
                            PG = PG - 10
                        if ((float(dct["FIELD35"])) < 1.5):
                            PG = PG - 10
                        if ((float(dct["FIELD33"])) < 3):
                            PG = PG - 10
                        if ((float(dct["FIELD34"])) > 3):
                            PG = PG - 10
                        if ((float(dct["FIELD41"])) < 8):
                            PG = PG - 10
                        P5[gamertag[5]][0] = PG

                        #SG Check
                        if ((float(dct["FIELD41"])) < 10):
                            SG = SG - 10
                        if ((float(dct["FIELD33"])) > 4):
                            SG = SG - 10
                        if ((float(dct["FIELD38"])) > 7):
                            SG = SG - 10
                        if ((float(dct["FIELD34"])) < 2):
                            SG = SG - 10
                        P5[gamertag[5]][1] = SG

                        #SF Check
                        if ((float(dct["FIELD33"])) < 3) or ((float(dct["FIELD33"])) >7):
                            SF = SF - 10
                        if ((float(dct["FIELD38"])) < 3 or (float(dct["FIELD38"]))>7):
                            SF = SF - 10
                        if ((float(dct["Per Game Stats"])) < 12):
                            SF = SF - 10
                        if ((float(dct["FIELD12"])) < 2):
                            SF = SF - 10
                        P5[gamertag[5]][2] = SF

                        #PF Check
                        if ((float(dct["FIELD40"])) < 4):
                            PF = PF - 10
                        if ((float(dct["FIELD12"])) < 1):
                            PF = PF - 10
                        if ((float(dct["FIELD48"])) > 7):
                            PF = PF - 10
                        if ((float(dct["FIELD39"])) < 4):
                            PF = PF - 10
                        P5[gamertag[5]][3] = PF
                    
                        #C Check
                        if ((float(dct["FIELD12"])) < 2):
                            C = C - 10
                        if (float(dct["FIELD43"].strip(' \t\n\r%'))) < 60:
                            C = C - 10
                        if ((float(dct["FIELD40"])) < 4):
                            C = C - 10
                        if ((float(dct["FIELD39"])) < 4):
                            C = C - 10                    
                        P5[gamertag[5]][4] = PF

                        
                        


                    
                
                print(P1)
                print(P2)
                print(P3)
                print(P4)
                print(P5)



                    

