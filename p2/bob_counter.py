'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
	s = input()
	a = len(s)
	count = 0
	for i in range(a):
		if s[i:].startswith('bob'):
			count += 1
	print(count)

if __name__== "__main__":
	main()
