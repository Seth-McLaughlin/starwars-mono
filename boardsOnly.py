# Import the random package
import random

# Import the matplotlib pyplot package
import matplotlib.pyplot as pyplot


def rollTwoDice():
    # Generate two random numbers within the
    # range 1 <= i <= 6 and add them together
    return random.randint(1,6) + random.randint(1,6)

# A function to create a histogram
def plot(x, y):
    pyplot.bar(x, y)
    pyplot.show()

# The number of squares on the board
numSquares = 40

# A list to con the total value rolled.
counters=[0.]*numSquares

# A variable to hold the current position
currentPosition = 0

# Set the number of rolls
numRolls = 1000000

# Print a message
print("Rolling the two dice " + str(numRolls) + " times...")

# Roll the dice
for i in range(numRolls):
    # roll the dice
    totalValue = rollTwoDice()

    # Move the player to the next position
    currentPosition = currentPosition + totalValue

    # If the player has moved past the last square, wrap board around.
    if currentPosition >= numSquares:
        currentPosition = currentPosition - numSquares

    # Count the current position on the board
    counters[currentPosition] = counters[currentPosition] + 1

# Total probability is always defined as 1
# Therefore, have to divide by the total number of counted values.
for i in range(len(counters)):
    counters[i] = counters[i] / float(numRolls)

# Now print the probabilities for each of the combinations
print("The probabilities of landing on a given Monopoly square after " + str(numRolls) + " rolls")
for i in range(len(counters)):
    # Need to add one, since Python counts from zero.
    print(" P("+str(i)+")="+str(counters[i]))
print("where P(n) is the probability of landing on the nth Monoply board square")

# Create a bar chart display
plot(range(len(counters)), counters)