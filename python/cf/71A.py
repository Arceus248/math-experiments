n=int(input())
i=n
t=n
lists=[]
while i>=1:
    i-=1   
    word=input()
    lists.append(word)
while t>=1:
    if len(lists[-t])>10:
        print(f'{lists[-t][0]}{len(lists[-t])-2}{lists[-t][-1]}')
    else:
        print(f"{lists[-t]}")
    t-=1