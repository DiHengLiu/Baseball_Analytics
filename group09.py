# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 17:16:09 2017

@author: aadit
"""
from operator import itemgetter

def main():
    'Just testing the help function.'
    #infile = input('Please enter the name of the file: ')
    inf = open('mlb.part.txt', 'r')
    #for i in range(2):
    #    if infile == 'mlb.part.txt':
    #        inf = open(infile, 'r') #opening the file
    #    else:
    #        print('Wrong file name. Please enter again.')
    #        infile = input('Please enter the name of the file: ')
    
    lstTemp = [] #empty list
    lstName = [] #empty list for team names
    
    for i in inf:
        y = i.split(';') #splitting the data
        lstTemp.append(y)
        lstName.append(y[1].strip()) #adding team names to list
        
    inf.close() #file closed
    
    lst = sorted(lstTemp, key=itemgetter(0)) #sorting the list alphabetically
        
    for j,ch in enumerate(lst):
        for k,cch in enumerate(lst[j]):
            if k > 0:
                try:
                    lst[j][k] = int(lst[j][k]) #converting stats(string) to integers
                except:
                    lst[j][k] = lst[j][k].strip() #not converting the player name and team
                    
    for i in lst:
        singles = i[5] - (i[6] + i[7] + i[8]) #calculating singles
        totalBases = singles + 2*(i[6]) + 3*(i[7]) + 4*(i[8]) #calculating Total bases
        batAvg = (i[5]) / (i[3]) #calculating Batting Average
        b= eval('%.3f' % batAvg) #evaluating it to 3 decimal places
        slugPerc = totalBases / (i[3]) #calculating slugging percentage
        s = eval('%.3f' % slugPerc) #evaluating it to 3 decimal places
        i.append(b)
        i.append(s)
       
    def team():
        team1 = input('Please enter a team identifier: ')
        team = team1.upper()
        
        while team not in lstName: #checking list of names
            print('Wrong team name. Please enter again.')
            team1 = input('Please enter a team identifier: ')
            team = team1.upper()
        
        if team in lstName:
            print("{:<20} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4}".format('Name','Team', 'GamesPlayed', 'AtBats', 'RunsScored', 'Hits', 'Dbls','Trpls','Homeruns','BatAvg','slugPer')) #headers of table
        
        for i in lst:
            if i[1] == team:
                print("{:<20} {:<4} {:<11} {:<6} {:<10} {:<4} {:<4} {:<5} {:<8} {:<6} {:<4}".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10])) #players stat from list

    def hits():
        n = eval(input('Please enter the top N number of players you want to see: ')) #number of players
        print("{:<20} {:<4}".format('Name','Hits')) #headers
        
        for i in range(n):
            hits = sorted(lst, key=itemgetter(5), reverse = True)[:n] #sorting based on hits with top n number of players
            print("{:<20} {:<4}".format(hits[i][0], hits[i][5]))
            
    def bat():
        n = eval(input('Please enter the top N number of players you want to see: ')) #number of players
        print("{:<20} {:<4}".format('Name','BatAvg'))
        
        for i in range(n):
            batting = sorted(lst, key=itemgetter(9), reverse = True)[:n] #sorting based on batting average with top n number of players
            print("{:<20} {:<6}".format(batting[i][0], batting[i][9])) #players name and batting average
    
    def slug():
        n = eval(input('Please enter the top N number of players you want to see: ')) #number of players
    
        print("{:<20} {:<4}".format('Name','SlugPer')) #headers
        
        for i in range(n):
           slugging = sorted(lst, key=itemgetter(10), reverse = True)[:n] #sorting based on slugging percentage with top n number of players
           print("{:<20} {:<7}".format(slugging[i][0], slugging[i][10])) #players name and slugging percentage
        
    report1 = input('These are the following commands:\nHELP\nQUIT\nTEAM\nHITS\nBATTING\nSLUGGING\n\nType the command you want to run: ')
    report = report1.upper()
    
    while report != 'HELP' and report != 'QUIT' and report != 'TEAM' and report != 'HITS' and report != 'BATTING' and report != 'SLUGGING':
        print('Wrong input. Please enter again.')
        report1 = input('Type the command you want to run: ')
        report = report1.upper()     
        
    if report == 'HELP':
        print(help(main))
    elif report == 'QUIT':
        exit()
    elif report == 'TEAM':
        team()    
    elif report == 'HITS':
        hits()
    elif report == 'BATTING':
        bat()
    elif report == 'SLUGGING':
        slug()
main()