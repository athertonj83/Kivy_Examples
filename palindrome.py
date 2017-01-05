#palindrome checks
def palindrome():
        inputWord=str(input("Palindrome Test\nPlease enter a word: ")).strip()

        if inputWord=="":
            print("You didn't enter a word.")
        elif inputWord.isalpha()==False:
            print("A palindrome should consist of only letters")
        else:
            if inputWord==inputWord[::-1]:
                print(inputWord," is a palindrome",sep="") # if raw reversal=true then both full & case insensitive
            else:
                if inputWord.upper()==inputWord[::-1].upper(): # else if all upper case reversal is true then case insensitive
                    print(inputWord," is a palindrome (case insensitive)",sep="")
                else:
                    print(inputWord," is not a palindrome",sep="")
palindrome()
