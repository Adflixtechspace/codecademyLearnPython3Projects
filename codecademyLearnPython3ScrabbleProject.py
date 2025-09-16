# In this project, I have processed some data from a group of friends playing scrabble. I used dictionaries to organise players, words, and points.
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# takes letters and points lists and combines them into a dictionary to associate each letter with the respective points
letter_to_points = {alpha:num for alpha, num in zip(letters,points)}

# adds space to possible scrabble "letters"
letter_to_points[" "] = 0

# prints the total points receive when playing {word} in Scrabble
def score_word(word):
  word = word.upper() # converts word to upper case to compare to dictionary
  point_total = 0 # initiates int for counting
  for letter in word:
    point_total += letter_to_points.get(letter, 0) # add value of letter in the dictionary
  return point_total

# used to display the points achieved for "brownie"
brownie_points = score_word("brownie")
print(brownie_points)

# list containing the players and their words as a list of strings
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

# Calculates the total points for each player based on their words
def update_point_totals(player_to_words):
  player_to_points = {}
  for player, words in player_to_words.items():
    player_points = 0
    for word in words: # where each list is examined to check points
      player_points += score_word(word)
    player_to_points[player] = player_points # adds player name plus points to player_to_points dictionary
  return player_to_points

# allows a word to be added to a player's list of used words and then updates the current points
def play_word(player, word):
  word = word.upper() # convers word to upper case to compare to dictionary
  player_to_words[player].append(word)
  points = update_point_totals(player_to_words) # calls update_points_total function and assigns it to points
  print(player_to_words, points)

play_word("player1", "Egg") # calls function