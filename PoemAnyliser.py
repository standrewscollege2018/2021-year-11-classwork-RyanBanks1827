# This will print the length of the entered text along with the amount of vowels.
def vowels(poemselected):
    sub1 = "a"
    sub2 = "e"
    sub3 = "i"
    sub4 = "o"
    sub5 = "u"

    vowel1 = poemselected.count(sub1)
    vowel2 = poemselected.count(sub2)
    vowel3 = poemselected.count(sub3)
    vowel4 = poemselected.count(sub4)
    vowel5 = poemselected.count(sub5)
    vowelcount =(vowel1+vowel2+vowel3+vowel4+vowel5)
    return vowelcount



while True:
    poemselected = input("What do you wish to analyse?")
    poemlength = len(poemselected)
    poemvowels = vowels(poemselected)
    lentoprint=("Length of string is {}".format(poemlength))
    vtopring=("No of vowels is {}".format(poemvowels))


    print(lentoprint)
    print(vtopring)
