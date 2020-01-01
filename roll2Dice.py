# Import random package
import random


def rollTwoDice():
    # Generate a two random numbers and add them together
    return random.randint(1, 6) + random.randint(1, 6)


numSquares = 40

theBoard = {
    "1": 'Naboo',
    "2": 'Holocron',
    "3": 'Coruscant',
    "4": 'Trade Route Tax',
    "5": 'Light Speed',
    "6": 'Geonosis',
    "7": 'Jedi Training',
    "8": 'Kashyyyk',
    "9": 'Mustafar',
    "11": 'Just visiting',
    "12": 'Tatooine',
    "13": 'R2-D2',
    "14": 'Yavin 4',
    "15": 'Death Star',
    "16": 'Light Speed',
    "17": 'Hoth',
    "18": 'Holocron',
    "19": 'Dagobah',
    "20": 'Bespin',
    "21": 'Tatooine',
    "22": 'Jedi Training',
    "23": 'Endor',
    "24": 'Death Star II',
    "25": 'Light Speed',
    "26": 'Jakku',
    "27": 'Takodana',
    "28": 'BB-8',
    "29": 'Starkiller Base',
    "30": 'Go to Jail',
    "31": 'Achh-to',
    "32": 'Canto Bight',
    "33": 'Holocron',
    "34": 'Crait',
    "35": 'Light Speed',
    "36": 'Jedi Training',
    "37": 'Pasaana',
    "38": 'Trade Route Tax',
    "39": 'Ajana Kloss',
    "40": 'GO'
}

jediTrainingCards = {
    '1': '"Much to learn, you still have. Pay 10 Credits"',
    '2': '"You persuade the gungans to rise up against the trade federation. Collect 10 credits"',
    '3': '"Lord Vader lays a trap and puts you in carbon freeze. Go to jail. Go directly to jail. Do not pass go. Do '
         'not collect 20 credits."',
    '4': '"You will remove these restraints and leave this cell with the door open. Get out of jail free. This card '
         'may be kept until needed, traded, or sold."',
    '5': '"Your force projection outwits Kylo Ren and helps and resistance. Collect 10 credits"',
    '6': '"Control, Control. You must learn control. Pay each player 10 credits."',
    '7': '"Obi-Wan has taught you well. Advance to Death Star II. If you pass go, Collect 20 credits."',
    '8': '"Escape the cluthes of the Guavian death gang and roaring Rathar as you fire up the hyperdrive. Advance to '
         'Takodana. If you pass go, collect 20 credits."',
    '9': '"Make a commitment to the jedi order, A commitment not easily broken. For each Tie fighter you own, '
         'pay 10 credits. For each X-wing you own, pay 50 credits."',
    '10': '"Secretly board Padmes ship to help save your apprentice from the dark side. Advance to Mustafar. If you '
          'pass go collect 20 credits."',
    '11': '"You fail to raise your X-wing from a slimy mudhole. Go back three spaces."',
    '12': '"You steer your podracer to victory in the Boonta Eve Classic. Advance to GO. Collect 20 credits."',
    '13': '"This isnt the droid your looking for. Advance to Next Droid. If unowned, you may buy it form the bank. If '
          'owned, roll the dice, and pay the owner that many credits"',
    '14': '"The tow cable on your speeder brings down an imperial walker. Advance to Hoth. If you pass GO, Collect 20 '
          'Credits."',
    '15': '"Advance to Ajan Kloss."',
    '16': '"Switch off your targeting computer and use the force. Advance to Death Star. If you pass GO, Collect 20 '
          'credits."',
}



