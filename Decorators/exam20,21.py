def count_vowels(string): # HeLLoPythOn
    vowel = 'a,A,u,U,o,O,i,I,e,E,y,Y'
    count = 0
    for i in string:
        if i in vowel:
            count += 1
    print(count)

count_vowels("HeLLoPythOn")
