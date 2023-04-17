import json

data = json.load(open("data.json"))

def translate(word):
	word = word.lower()
	if word in data:
		return data[word]

def main():
	while True:
		word = input("Please enter a word (enter 'q' to exit the program): ")
		if (word == "q"):
			quit()
		translation = translate(word)

		if translation:
			for word in translation:
				print(word)
		else:
			print("Word was not found!")

if __name__== "__main__":
	main()
