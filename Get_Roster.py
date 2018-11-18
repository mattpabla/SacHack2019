import csv
import json

csvfile = open('NBA 2KL Stats [HackAThon Edits].xlsx', 'r')
jsonfile = open('file.json','w')
#1-47
'''
1-PTS
2-AST
3-TO
4-AST/TO
5-STL
6-BLK
7-REB
8-OREB
9-DREB
10-FGA
11-FGM
12-FG%
13-eFG%
14-2FGA
15-2FGM
16-2FG%
17-3FGM
18-3FG%
19-FTA
20-FTM
21-FT%
22-PF TKN
23-PF
24-PPG
25-APG
26-TO PG
27-AST/TO
28-STL PG
29-BLK PG
30-RPG
31-OREB PG
32-DREB PG
33-FGA PG
34-FGM PG
35-FG% PG
36-eFG% PG
37-2PGA PG
38-2FGM PG
39-2FG%
40-3PGA PG
41-3FGM PG
42-3FG%
43-FTA PG
44-FTM PG
45-FT%
46-PF TKN
47-PF PG
'''
fieldnames = ("Team","Gamertag", "Event", "GP","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"
,"21","22","23","24", "25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45",
"46","47")

reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)
