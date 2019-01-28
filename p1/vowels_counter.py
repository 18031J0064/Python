#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
    s = input()
    count = 0
    for i in s:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            count += 1
    print(count)

if __name__== "__main__":
	main()
