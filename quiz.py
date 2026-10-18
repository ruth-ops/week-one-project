display_score =0
print ( "welcome to the Netflix trivia quiz !" )
print ("question 1 : 'in squid game' what is the title of the first game playeers play ?")

print ("A. red light green light")
print ("B. tug of war")
print ("C. marbles")
print ("D. glass bridge")

input1 = input ("enter your answer : ")
if input1 == "A" or input1 == "a":
    print ("correct answer !")
    display_score = 0
print ("question 2 : 'in squid game' what game is played in the honeycomb challenge ?¨)  ")

print( "A. tug of war")
print ("B. dalgona candy")
print ("C. hopscotch")
print ("D. rock paper scissors")

input2 = input ("enter your answer : ")
if input2 == "B" or input2 == "b":
    print ("correct answer !")
    display_score += 1
else:
    print ("incorrect answer !")

    print ("question 3 : 'in squid game' what happens if you lose a game ?")
    print ("A. you  are eliminated from the game")
    print ("B. you are locked in a room")
    print ("C. you are sent home with zero money")
    print ("D. you must give up your money and leave the game")

    input3 = input ("enter your answer : ")
if input3 == "A" or input3 == "a":
    print ("correct answer !")
    display_score += 1

    print ("question 4 : 'in squid game' what shape is the dalgona candy in the honeycomb challenge ?")
    print ("A. circle")
    print ("B. triangle")
    print ("C. star")
    print ("D. umbrella")

    input4 = input ("enter your answer : ")
if input4 == "C" or input4 == "c":
    print ("correct answer !")
    display_score += 1

    print ("question 5 : 'in squid game' how much money does the winner of the game receive ?")
    print ("A. 100 million won")
    print ("B. 200 million won")
    print ("C. 300 million won")
    print ("D. 400 million won")
    input5 = input ("enter your answer : ")
    if input5 == "B" or input5 == "b":
        print ("correct answer !")
        display_score += 1

print (f"your final score is : {display_score}/5")
