import random

fruit=['Apple','Avocado','Banana','Cherry','Dates','Elderberry','Fig','Grapes','Guava','Melon','Kiwi','Lemon','Mango','Nectarine','Olive','Orange','Pear','Peppers','Pineapple','Pumpkin','Raisin','Satsumas','Strawberry','Tomato','Plum','Watermelon','Zucchini']
animal=['Aardvark','Abyssinian','GuineaPig','Addax','Alpaca','Ant','Ape','Baboon','BaldEagle','Bat','Beagle','Bear','BeardedDragon','Beetle','Bee','Beefalo','Bird','Blobfish','Bloodhound','Bluegill','BostonTerrier','Bug','Butterfly','Bulldog','Bumblebee','Cat','Camel','Crab','Chicken','Caterpillar','Chincilla','Chimpanzee','Chipmunk','Caoti','Cockatoo','Cow','Crow','Crocodile','Crane','Deer','DobermanPinscher','Dolphin','DwarfHamster','Duck','Donkey','Eagle','Earthworm','Eel','Elephant','Emu','Fish','Frog','Flamingo','Giraffe','Goat','Goose','Gorilla','Hamster','Horse','Husky','Hedgehog','Iguana','Impala','Insect','Jellyfish','Jaguar','Kangaroo','Kiwi','Koala','LadyBug','Leopard','Lizard','Lobster','marmot','Monkey','Mouse','Octopus','Ox','Otter','Parrot','Pelican','Penguin','Pigeon','Python','Quokka','Rabbit','Raccoon','Robin','Rooster','Salmon','Scorpion','Seagull','Shark','Shrimp','Sloth','Sparrow','Spider','Squid','Starfish','Squirrel','Swallow','Tortoise','Turtle','Tarantula','Vulture','Wallaby','Weasel','WhiteShark','Zebra']
thing=['Airplane','Bicycle','Candle','Camera','Computer','Doorbell','Diamond','Flower','Garbage','Hairbrush','Keyboard','Kitchen','Microwave','MotorCycle','Necklace','Napkin','MailBox','Sunflower','Sunglass','Television','Telephone','Toothbrush','Umbrella','Uniform','Vacuum','Wrench']
nation=['Korea','Japan','China','America','Canada','Thailand','Vietnam','Russia','France','England','Spain','Portugal','Afghanistan','Albania','Australia','Austria','Azerbaijan','Belgium','Bolivia','Brazil','Cambodia','Chile','Colombia','Congo','Croatia','Cuba','Denmark','Ecuador','Egypt','Ethiopia','Finland','Germany','Greece','Guatemala','Georgia','Hungary','Iceland','India','Indonesia','Iraq','Italy','Iran','Jordan','Kenya','Kuwait','Libya','Lithuania','Luxembourg','Malaysia','Mexico','Monaco','Mongolia','Morocco','Nepal','Netherlands','Nigeria','Norway','Oman','Pakistan','Peru','Philippines','Poland','Qatar','Romania','SaudiArabia','Singapore','Sudan','Sweden','Swaziland','Switzerland','Tibet','Uganda','Ukraine','Uzbekistan','ArabEmirates','Yemen','Zambia','Zimbabwe']
sport=['Archery','Badminton','Baseball','Basketball','Bobsleigh','Bowling','Boxing','Canoeing','Climbing','Cricket','Curling','Cycling','Fencing','FigureSkating','Football','Golf','Handball','IceHockey','IceSkating','Marathon','Polo','Running','Rugby','Sailing','ShortTrack','Shooting','Skeleton','Snowboarding','Soccer','SpeedSkating','Surfing','Swimming','Tennis','Volleyball','Weightlifting','Wrestling']

words_sub=[fruit,animal,thing,nation,sport]
str_words_sub=["fruit",'animal','thing','nation','sport']
#print(len(thing))
"""len: for the random word
fruit: 27
animal: 110
thing:  28
nation: 78
sport:36
"""
def pick_word():
    global SUBJECT,words_sub
    #Pick up a random word in a random subjects and return it.
    subject=random.randrange(5) # 0-4;for random subject
    SUBJECT = str_words_sub[subject] #!!
    word=random.choice(words_sub[subject]) # random word in the subject
    word = word.lower()
    return word

def get_subject():
    global SUBJECT
    return SUBJECT

