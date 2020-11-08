n = 0
a = ["a","b","c","d","e","f",'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

while (n == 0):
    word1 = str(input("¬ведите слово на русском €зыке: "))
    s = []
    s = list(word1)
    
    check = 0
    for i in s:
        if i in a:
            check = check + 1
        if check == 0:
            n = 1
    if n == 0:
        print ('')
        print ('¬ведите верно')

    

n = 0

while (n == 0):
    word2 = str(input("¬ведите слово на английском €зыке: "))
    s = []
    s = list(word2)
    
    check = 0
    for i in s:
        if i in a:
            check = check + 1
        if check == len(s):
            n = 1
    if n == 0:
        print ('')
        print ('¬ведите верно')

        

d = {word1 : "–усский ", word2 : "јнглийский"}

print ("")
print (d)
