import simple_chalk
from simple_chalk import chalk, green
from simple_chalk import chalk, yellow

word1 = input(chalk.magenta("Enter the first word: "))
word2 = input(chalk.magenta("Enter the second word: "))

def ananagram():
	

	if (sorted(word1) == sorted(word2)):
		print(chalk.yellow("These two are anagrams"))
	else:
		print(chalk.red.bold("These two are not anagrams"))		
		


ananagram()
