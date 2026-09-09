n=int(input("Enter Number of Player"))

players=[]

for i in range(n):
    name=input("Enter name: ")
    score=input("Enter Score: ")
    players.append((name,score))

    print("List",players)

maximum=max(players,key=lambda x:x[1])
print("Maximum",maximum)  

average=sum(score for name,score in players)/n

print("Your Average",average)

for name,score in players:
    if score>500:
        print("Name",name)

players.sort(key=lambda x:x[1])
for name,score in players: 
 print("Sort the players",name,score)

for name,score in players[3]:
   print("Top 3 players are",name,score)