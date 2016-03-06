import itertools, random

SUITES = ("Diamond", "Spade", "Heart", "Club")
NUMBERS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

def main():
	deck = list(itertools.product(["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"], ["Diamond", "Spade", "Heart", "Club"]))

	random.shuffle(deck)

	player1 = []
	player2 = []
	player3 = []
	player4 = []

	for x in range(0,12,4):
		player1.append(deck[x])
		deck.pop(0)
		player2.append(deck[x+1])
		deck.pop(0)
		player3.append(deck[x+2])
		deck.pop(0)
		player4.append(deck[x+3])
		deck.pop(0)

	print "Player 1 has", player1
	print "Player 2 has", player2
	print "Player 3 has", player3
	print "Player 4 has", player4

if __name__ == '__main__':
	main()