import random
global chose
chose=[]
def choose_word():
    chose = []
    words = []
    with open ('music.txt','r') as file:
        for line in file:
            for word in line.split():
                words.append(word)
    num = random.randint(0,len(words)-1)
    tchosen = words[num]
    tchosen = tchosen.upper()
    for i in tchosen:
        chose.append(i)
    print(chose)
    
    return chose

        

