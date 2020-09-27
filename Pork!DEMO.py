#This section of code contains a function with an easter egg inside:
def easterEgg1():
    
    print("""
        :::   :::       :::     :::::::::  ::::::::::        :::       ::: ::::::::::: ::::::::::: :::    :::    
      :+:+: :+:+:    :+: :+:   :+:    :+: :+:               :+:       :+:     :+:         :+:     :+:    :+: :+: 
    +:+ +:+:+ +:+  +:+   +:+  +:+    +:+ +:+               +:+       +:+     +:+         +:+     +:+    +:+      
   +#+  +:+  +#+ +#++:++#++: +#+    +:+ +#++:++#          +#+  +:+  +#+     +#+         +#+     +#++:++#++       
  +#+       +#+ +#+     +#+ +#+    +#+ +#+               +#+ +#+#+ +#+     +#+         +#+     +#+    +#+        
 #+#       #+# #+#     #+# #+#    #+# #+#                #+#+# #+#+#      #+#         #+#     #+#    #+# #+#     
###       ### ###     ### #########  ##########          ###   ###   ###########     ###     ###    ###
    """)
    
    
    print("""
     :::::::::  :::   ::: ::::::::::: :::    :::  ::::::::  ::::    ::: 
     :+:    :+: :+:   :+:     :+:     :+:    :+: :+:    :+: :+:+:   :+:  
    +:+    +:+  +:+ +:+      +:+     +:+    +:+ +:+    +:+ :+:+:+  +:+   
   +#++:++#+    +#++:       +#+     +#++:++#++ +#+    +:+ +#+ +:+ +#+    
  +#+           +#+        +#+     +#+    +#+ +#+    +#+ +#+  +#+#+#     
 #+#           #+#        #+#     #+#    #+# #+#    #+# #+#   #+#+#      
###           ###        ###     ###    ###  ########  ###    #### 
""")
def readBook(book):
    #This section of code contains the text of "Orlando: A Biography, by Virgina Woolf"
    if book=="Orlando: A Biography, by Virgina Woolf":
        print("""You read: Orlando: A Biography:\n
HE–FOR THERE COULD be no doubt of his sex, 
though the fashion of the time did something to 
disguise it–was in the act of slicingat the head 
of a Moor which swung from the rafters. 
It was the colour of an old football,
and more or less the shape of one, save for the
sunken cheeks and a strand or two of coarse,
dry hair, like the hair on a cocoanut. Orlando’s
father, or perhaps his grandfather, had struck
it from the shoulders of a vast Pagan who had 
started up under the moon in the barbarian fields of Africa; 
and now it swung, gently,perpetually, in the breeze which never 
ceased blowing through the attic rooms of the gigantic
house of the lord who had slain him.
            """)
    elif book=="Carmilla, by Joseph Sheridan Le Fanu":
        print("""You read: Carmilla:\n
PROLOGUE:
Upon a paper attached to the Narrative which follows, Doctor Hesselius has written a rather elaborate note, 
which he accompanies with a reference to his Essay on the strange subject which the MS. illuminates.
This mysterious subject he treats, in that Essay, with his usual learning and acumen, 
and with remarkable directness and condensation. 
It will form but one volume of the series of that extraordinary man's collected papers.
As I publish the case, in this volume, simply to interest the "laity," 
I shall forestall the intelligent lady, who relates it, in nothing; and after due consideration, 
I have determined, therefore, to abstain from presenting any précis of the learned Doctor's reasoning, 
or extract from his statement on a subject which he describes as "involving, not improbably, 
some of the profoundest arcana of our dual existence, and its intermediates."
I was anxious on discovering this paper, to reopen the correspondence commenced by Doctor Hesselius, 
so many years before, with a person so clever and careful as his informant seems to have been. 
Much to my regret, however, I found that she had died in the interval.
She, probably, could have added little to the Narrative which she communicates in the following pages, 
with, so far as I can pronounce, such conscientious particularity.
            """)
    elif book=="Ulyssses, by James Joyce":
        print("""You read: Ulyssses:\n
Stately, plump Buck Mulligan came from the stairhead, bearing a bowl of lather on which a mirror and a razor lay crossed. 
A yellow dressinggown, ungirdled, was sustained gently behind him on the mild morning air. He held the bowl aloft and intoned:
—Introibo ad altare Dei.
Halted, he peered down the dark winding stairs and called out coarsely:
—Come up, Kinch! Come up, you fearful jesuit!
Solemnly he came forward and mounted the round gunrest. He faced about and blessed gravely thrice the tower, the surrounding land and the awaking mountains. 
Then, catching sight of Stephen Dedalus, he bent towards him and made rapid crosses in the air, gurgling in his throat and shaking his head. Stephen Dedalus, displeased and sleepy, leaned his arms on the top of the staircase and looked coldly at the shaking gurgling face that blessed him, equine in its length, and at the light untonsured hair, grained and hued like pale oak.
Buck Mulligan peeped an instant under the mirror and then covered the bowl smartly.
—Back to barracks! he said sternly.
He added in a preacher’s tone:
—For this, O dearly beloved, is the genuine Christine: body and soul and blood and ouns. 
Slow music, please. Shut your eyes, gents. One moment. A little trouble about those white corpuscles. Silence, all.
            """)
    elif book== "Dr. Blair's Grimore, by Dr. Blair":
        pass
#This fuction displays information on the player's enviroment based on what their "focus" is:

def gameKnowelege(focus,inventory):
#This section of the gameKnowelege(focus,inventory): fuction, contains information pretaining to all of the rooms in the game (however the demo only includes 1 room):
    if focus == "dark room":
        if "candle" not in inventory and "lit candle" not in inventory: 
            print("\nDark Room\
            \nYou stand in a dimly lit room, you can barely see your hand that is right in front of you.\
            \nThe only source of light is a small candle placed in front of you...")
        elif "candle" in inventory:
            print("\nDark Room\
            \nYou stand in a pitch black room, you cannot see anything...\
            \nIf only you could light a candle...")
        elif "lit candle" in inventory:
            print("\nDark Room\
            \nThe flicker of the candle is a comforting companion in the void...\
            \nYou you can see the dim outline of the room, in front of you you swear there is the faint outline of a door...")
    #This section of code contains the descriptions for the northern wall of the room:
    elif focus == "dark room north":
        if "candle" not in inventory and "lit candle" not in inventory:
            print("\nDark Room: Northern Wall\
            \nThe faint candlelight coming from behind you isn't enough for you to see anything...")
        elif "candle" in inventory:
            print("\nDark Room: Northern Wall\
            \nYou stand in a pitch black room, you cannot see anything...")
        elif "lit candle" in inventory:
            print("\nDark Room: Northern Wall\
            \nYou see a large wooden door.\
            \nThere is a lock on it...")
    #This section of code contains descriptions for the southern wall of the room:
    elif focus == "dark room south":
        if "candle" not in inventory and "lit candle" not in inventory:
            print("\nDark Room: Southern Wall\
            \nThe faint candlelight coming from behind you can see the faint rectangular outline of something...")
        elif "candle" in inventory:
            print("\nDark Room: Southern Wall\
            \nYou stand in a pitch black room, you cannot see anything...")
        elif "lit candle" in inventory:
            print("\nDark Room: Southern Wall\
            \nIn the flickering light you see what used to be an ornate bookself, now reduced to a state of dispair...")
            #This section of code displays text reflecting the how many books are left on the bookshelf:
            if "Orlando: A Biography, by Virgina Woolf" not in inventory and "Carmilla, by Joseph Sheridan Le Fanu" not in inventory\
                and "Ulyssses, by James Joyce" not in inventory\
                and "Dr. Blair's Grimore, by Dr. Blair" not in inventory:
                print("There's a few books left though...")
            elif "Orlando: A Biography, by Virgina Woolf" in inventory or "Carmilla, by Joseph Sheridan Le Fanu" in inventory\
                or "Ulyssses, by James Joyce" in inventory\
                or "Dr. Blair's Grimore, by Dr. Blair" in inventory:
                print("It seems you've left a few books on the bookshelf...")
            elif "Orlando: A Biography, by Virgina Woolf" in inventory and "Carmilla, by Joseph Sheridan Le Fanu" in inventory\
                and "Ulyssses, by James Joyce" in inventory\
                and "Dr. Blair's Grimore, by Dr. Blair" in inventory:
                print("The bookself is empty")
    #This section of code contains descriptions for the eastern wall of the room:
    elif focus == "dark room east":
        if "candle" not in inventory and "lit candle" not in inventory:
            print("\nDark Room: Eastern Wall\
            \nThe faint candlelight coming from behind you isn't enough for you to see anything...")
        elif "candle" in inventory:
            print("\nDark Room: Eastern Wall\
            \nYou stand in a pitch black room, you cannot see anything...")
        elif "lit candle" in inventory:
            print("\nDark Room: Eastern Wall\
            \nThere is a beautiful painting on the wall...")
    #This section of code contains descriptions for the western wall of the room:
    elif focus == "dark room west":
        #This section of code describes the room if the candle is on the floor
        if "candle" not in inventory and "lit candle" not in inventory:
            print("\nDark Room: Western wall\
            \nThe faint candlelight coming from behind you is enough to see the outline of something but not much else...")
        #This section of code desribes the room if no candle is lit:
        elif "candle" in inventory:
            print("\nDark Room: Western wall\
            \nYou stand in a pitch black room, you cannot see anything...")
        #This section of code desribes the room if you have a lit candle:
        elif "lit candle" in inventory:
            if "note" not in inventory:
                print("\nDark Room: Western wall\
                \nIn the dim candlelight you can see a small wooden desk, there apears to be a note on top of it...")
            elif "note" in inventory:
                print("\nDark Room: Western wall\
                \nIn the dim candlelight you can see a small wooden desk...")
#This section of code runs the main game demo of pork!
def mainGame(runYn):
    playerInventory = []
    room="dark room"
    command = "null"
    gameRun = str(runYn)
    doorLocked = "y"
    bookShelfBooks= ["Orlando: A Biography, by Virgina Woolf",\
        "Carmilla, by Joseph Sheridan Le Fanu",\
        "Ulyssses, by James Joyce",\
        "Dr. Blair's Grimore, by Dr. Blair"]
    #This section of code contains nested "if" statements that control player movement in the starting room:
    while gameRun == "y":
        if room == "dark room":
            while room == "dark room":
                gameKnowelege(room,playerInventory)
                command = input(">")
            #This set of loops is used to determine how the player should interact with this room:
            #This if statement is utilized when interacting with the candle:
                #This command runs if the player is in the dark room, which has a candle, and they have not collected it before:
                if command == "take candle" and "candle" not in playerInventory:
                    print("You grab the candle")
                    playerInventory.append("candle")
                    continue
                #This section of code tells the player that the candle is allready in their inventory if it sees it in there:
                elif command == "take candle" and "candle" in playerInventory:
                    print("there is no candle")
                elif command == "use candle" and "candle" in playerInventory:
                    print("You light your candle")
                    candleIndex = "null"
                    candleIndex = playerInventory.index("candle")
                    playerInventory[int(candleIndex)]="lit candle"
                    continue
                elif command == "read note" and "note" in playerInventory:
                    print("You read the note:\n")
                    print("Dear kind player,\
                        \nThank you so much for playing our game!\
                        \nBut did you know that our game has a couple secrets!\
                        \nSee if you can find them all!!!!\
                        \n\nSincerely,\
                        \n-The Dev's!\
                        \n")
                    continue
                elif command == "read map" and "map" in playerInventory:
                    print("You read the map:\n")
                    print("* * * * * * * *|---|* * * * * * * *\
    \n*                ^                *\
    \n*                |                *\
    \n*[]<- Desk       |                *\
    \n*                |                *\
    \n*               DOOR             |*\
    \n*                                |*\
    \n*                                |*\
    \n*                     Painting ->|*\
    \n*                                 *\
    \n*                                 *\
    \n*                     |Bookself|  *\
    \n* * * * * * * * * * * * * * * * * *\n")
                #This if statement is utilized when interacting with player movement:
                if command == "move north":
                    room = "dark room north"
                    break
                elif command == "move south":
                    room = "dark room south"
                    break
                elif command == "move east":
                    room = "dark room east"
                    break
                elif command == "move west":
                    room = "dark room west"
                    break
                elif command == "exit":
                    gameRun = "n"
                    break
                else:
                    continue
        #This section of code contains the functions that work within the dark room's northern wall:
        elif room == "dark room north":
            while room == "dark room north":
                gameKnowelege(room,playerInventory)
                command = input(">")
                if command == "use key" and "key" in playerInventory:
                    print("You opened the locked door!")
                    doorLocked = "n"
                    continue
                #This section of code allows you to read books:
                elif command == "read Orlando: A Biography" and "Orlando: A Biography, by Virgina Woolf" in playerInventory:
                    readBook("Orlando: A Biography, by Virgina Woolf")
                    print("You found a key hidden in the spine of the book!\
                        \nI wonder what it goes to...")
                    playerInventory.append("key")
                    continue
                elif command == "read Carmilla" and "Carmilla, by Joseph Sheridan Le Fanu" in playerInventory:
                    readBook("Carmilla, by Joseph Sheridan Le Fanu")
                    continue
                elif command == "read Ulyssses" and "Ulyssses, by James Joyce" in playerInventory:
                    readBook("Ulyssses, by James Joyce")
                    continue
                elif command == "read Dr. Blair's Grimore" and "Dr. Blair's Grimore, by Dr. Blair" in playerInventory:
                    readBook("Dr. Blair's Grimore, by Dr. Blair")
                    continue
                elif command == "use candle" and "candle" in playerInventory:
                    print("You light your candle")
                    candleIndex = "null"
                    candleIndex = playerInventory.index("candle")
                    playerInventory[int(candleIndex)]="lit candle"
                    continue
                elif command == "read note" and "note" in playerInventory:
                    print("You read the note:\n")
                    print("Dear kind player,\
                        \nThank you so much for playing our game!\
                        \nBut did you know that our game has a couple secrets!\
                        \nSee if you can find them all!!!!\
                        \n\nSincerely,\
                        \n-The Dev's!\
                        \n")
                    continue
                elif command == "read map" and "map" in playerInventory:
                    print("You read the map:\n")
                    print("* * * * * * * *|---|* * * * * * * *\
    \n*                ^                *\
    \n*                |                *\
    \n*[]<- Desk       |                *\
    \n*                |                *\
    \n*               DOOR             |*\
    \n*                                |*\
    \n*                                |*\
    \n*                     Painting ->|*\
    \n*                                 *\
    \n*                                 *\
    \n*                     |Bookself|  *\
    \n* * * * * * * * * * * * * * * * * *\n")
                    continue
                #This set of "if" statements is utilized when interacting with player movement:
                if command == "move east":
                    room = "dark room east"
                    break
                elif command == "move west":
                    room = "dark room west"
                    break
                elif command == "move south":
                    room = "dark room"
                    break
                elif command == "move north":
                    if doorLocked == "y":
                        print("You ran headfirst into the door...\
                        \nIf you want to get out of here you should use your head, just not quite like that...")
                        continue
                    elif doorLocked == "n":
                        room = "endGameRoom"
                        break
                elif command == "exit":
                    gameRun = "n"
                    break
                else:
                    continue

        #This section of code contains the functions that work within the dark room's southern wall:
        elif room == "dark room south":
            while room == "dark room south":
                gameKnowelege(room,playerInventory)
                command = input(">")
                if command == "search bookshelf":
                    print("You see these books:")
                    #This section of code lists the books
                    for listNum in range(len(bookShelfBooks)):
                        print(bookShelfBooks[listNum]+"\n")
                    continue
                #This section of code allows you to take books:
                elif command == "take Orlando: A Biography":
                    print("You grab: Orlando: A Biography, by Virgina Woolf")
                    playerInventory.append("Orlando: A Biography, by Virgina Woolf")
                    bookShelfBooks.remove("Orlando: A Biography, by Virgina Woolf")
                    continue
                elif command == "take Carmilla":
                    print("You grab: Carmilla, by Joseph Sheridan Le Fanu")
                    playerInventory.append("Carmilla, by Joseph Sheridan Le Fanu")
                    bookShelfBooks.remove("Carmilla, by Joseph Sheridan Le Fanu")
                    continue
                elif command == "take Ulyssses":
                    print("You grab: Ulyssses, by James Joyce")
                    playerInventory.append("Ulyssses, by James Joyce")
                    bookShelfBooks.remove("Ulyssses, by James Joyce")
                    continue
                elif command == "take Dr. Blair's Grimore":
                    print("You grab: Dr. Blair's Grimore, by Dr. Blair")
                    playerInventory.append("Dr. Blair's Grimore, by Dr. Blair")
                    bookShelfBooks.remove("Dr. Blair's Grimore, by Dr. Blair")
                    continue
                #This section of code allows you to read books:
                elif command == "read Orlando: A Biography" and "Orlando: A Biography, by Virgina Woolf" in playerInventory:
                    readBook("Orlando: A Biography, by Virgina Woolf")
                    print("You found a key hidden in the spine of the book!\
                        \nI wonder what it goes to...")
                    playerInventory.append("key")
                elif command == "read Carmilla" and "Carmilla, by Joseph Sheridan Le Fanu" in playerInventory:
                    readBook("Carmilla, by Joseph Sheridan Le Fanu")
                elif command == "read Ulyssses" and "Ulyssses, by James Joyce" in playerInventory:
                    readBook("Ulyssses, by James Joyce")
                elif command == "read Dr. Blair's Grimore" and "Dr. Blair's Grimore, by Dr. Blair" in playerInventory:
                    readBook("Dr. Blair's Grimore, by Dr. Blair")
                elif command == "use candle" and "candle" in playerInventory:
                    print("You light your candle")
                    candleIndex = "null"
                    candleIndex = playerInventory.index("candle")
                    playerInventory[int(candleIndex)]="lit candle"
                    continue
                elif command == "read note" and "note" in playerInventory:
                    print("You read the note:\n")
                    print("Dear kind player,\
                        \nThank you so much for playing our game!\
                        \nBut did you know that our game has a couple secrets!\
                        \nSee if you can find them all!!!!\
                        \n\nSincerely,\
                        \n-The Dev's!\
                        \n")
                    continue
                elif command == "read map" and "map" in playerInventory:
                    print("You read the map:\n")
                    print("* * * * * * * *|---|* * * * * * * *\
    \n*                ^                *\
    \n*                |                *\
    \n*[]<- Desk       |                *\
    \n*                |                *\
    \n*               DOOR             |*\
    \n*                                |*\
    \n*                                |*\
    \n*                     Painting ->|*\
    \n*                                 *\
    \n*                                 *\
    \n*                     |Bookself|  *\
    \n* * * * * * * * * * * * * * * * * *\n")
                    continue
                #This set of "if" statements is utilized when interacting with player movement:
                if command == "move east":
                    room = "dark room east"
                    break
                elif command == "move west":
                    room = "dark room west"
                    break
                elif command == "move north":
                    room = "dark room"
                    break
                elif command == "move south":
                    print("You ran into a wall...")
                    continue
                elif command == "exit":
                    gameRun = "n"
                    break
                else:
                    continue
        #This section of code contains the functions that work within the dark room's eastern wall:
        elif room == "dark room east":
            while room == "dark room east":
                gameKnowelege(room,playerInventory)
                command = input(">")
                if command == "enjoy painting":
                    easterEgg1()
                    continue
                elif command == "use candle" and "candle" in playerInventory:
                    print("You light your candle")
                    candleIndex = "null"
                    candleIndex = playerInventory.index("candle")
                    playerInventory[int(candleIndex)]="lit candle"
                    continue
                elif command == "read note" and "note" in playerInventory:
                    print("You read the note:\n")
                    print("Dear kind player,\
                        \nThank you so much for playing our game!\
                        \nBut did you know that our game has a couple secrets!\
                        \nSee if you can find them all!!!!\
                        \n\nSincerely,\
                        \n-The Dev's!\
                        \n")
                    continue
                elif command == "read map" and "map" in playerInventory:
                    print("You read the map:\n")
                    print("* * * * * * * *|---|* * * * * * * *\
    \n*                ^                *\
    \n*                |                *\
    \n*[]<- Desk       |                *\
    \n*                |                *\
    \n*               DOOR             |*\
    \n*                                |*\
    \n*                                |*\
    \n*                     Painting ->|*\
    \n*                                 *\
    \n*                                 *\
    \n*                     |Bookself|  *\
    \n* * * * * * * * * * * * * * * * * *\n")
                    continue
                #This set of "if" statements is utilized when interacting with player movement:
                if command == "move north":
                    room = "dark room north"
                    break
                elif command == "move south":
                    room = "dark room south"
                    break
                elif command == "move west":
                    room = "dark room"
                    break
                elif command == "move east":
                    print("You ran into a wall...")
                    continue
                elif command == "exit":
                    gameRun = "n"
                    break
                else:
                    continue
        #This section of code contains the functions that work within the dark room's western wall:
        elif room == "dark room west":
            while room == "dark room west":
                gameKnowelege(room,playerInventory)
                command = input(">")
                #This section of code deals with the player's interaction with the note on the desk
                if command == "take note" and "note" not in playerInventory:
                    print("You grab the note")
                    playerInventory.append("note")
                    continue
                elif command == "use candle" and "candle" in playerInventory:
                    print("You light your candle")
                    candleIndex = "null"
                    candleIndex = playerInventory.index("candle")
                    playerInventory[int(candleIndex)]="lit candle"
                    continue
                elif command == "read note" and "note" in playerInventory:
                    print("You read the note:\n")
                    print("Dear kind player,\
                        \nThank you so much for playing our game!\
                        \nBut did you know that our game has a couple secrets!\
                        \nSee if you can find them all!!!!\
                        \n\nSincerely,\
                        \n-The Dev's!\
                        \n")
                    continue
                elif command == "open desk":
                    print("You open the desk, inside there is a map, you take it.")
                    playerInventory.append("map")
                    continue
                elif command == "read map" and "map" in playerInventory:
                    print("You read the map:\n")
                    print("* * * * * * * *|---|* * * * * * * *\
    \n*                ^                *\
    \n*                |                *\
    \n*[]<- Desk       |                *\
    \n*                |                *\
    \n*               DOOR             |*\
    \n*                                |*\
    \n*                                |*\
    \n*                     Painting ->|*\
    \n*                                 *\
    \n*                                 *\
    \n*                     |Bookself|  *\
    \n* * * * * * * * * * * * * * * * * *\n")
                #This set of "if" statements is utilized when interacting with player movement:
                if command == "move north":
                    room = "dark room north"
                    break
                elif command == "move south":
                    room = "dark room south"
                    break
                elif command == "move east":
                    room = "dark room"
                    break
                elif command == "move west":
                    print("You ran into a wall...")
                    continue
                elif command == "exit":
                    gameRun = "n"
                    break
                else:
                    continue
        elif room == "endGameRoom":
            print("""
$$$$$$$$\ $$\                           $$\                        $$$$$$\                           
\__$$  __|$$ |                          $$ |                      $$  __$$\                          
   $$ |   $$$$$$$\   $$$$$$\  $$$$$$$\  $$ |  $$\  $$$$$$$\       $$ /  \__|$$$$$$\   $$$$$$\        
   $$ |   $$  __$$\  \____$$\ $$  __$$\ $$ | $$  |$$  _____|      $$$$\    $$  __$$\ $$  __$$\       
   $$ |   $$ |  $$ | $$$$$$$ |$$ |  $$ |$$$$$$  / \$$$$$$\        $$  _|   $$ /  $$ |$$ |  \__|      
   $$ |   $$ |  $$ |$$  __$$ |$$ |  $$ |$$  _$$<   \____$$\       $$ |     $$ |  $$ |$$ |            
   $$ |   $$ |  $$ |\$$$$$$$ |$$ |  $$ |$$ | \$$\ $$$$$$$  |      $$ |     \$$$$$$  |$$ |            
   \__|   \__|  \__| \_______|\__|  \__|\__|  \__|\_______/       \__|      \______/ \__|            
                                                                                                     
                                                                                                     
                                                                                                     
          $$\                     $$\                                                                
          $$ |                    \__|                                                               
 $$$$$$\  $$ | $$$$$$\  $$\   $$\ $$\ $$$$$$$\   $$$$$$\        $$$$$$\$$$$\  $$\   $$\              
$$  __$$\ $$ | \____$$\ $$ |  $$ |$$ |$$  __$$\ $$  __$$\       $$  _$$  _$$\ $$ |  $$ |             
$$ /  $$ |$$ | $$$$$$$ |$$ |  $$ |$$ |$$ |  $$ |$$ /  $$ |      $$ / $$ / $$ |$$ |  $$ |             
$$ |  $$ |$$ |$$  __$$ |$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |      $$ | $$ | $$ |$$ |  $$ |             
$$$$$$$  |$$ |\$$$$$$$ |\$$$$$$$ |$$ |$$ |  $$ |\$$$$$$$ |      $$ | $$ | $$ |\$$$$$$$ |             
$$  ____/ \__| \_______| \____$$ |\__|\__|  \__| \____$$ |      \__| \__| \__| \____$$ |             
$$ |                    $$\   $$ |              $$\   $$ |                    $$\   $$ |             
$$ |                    \$$$$$$  |              \$$$$$$  |                    \$$$$$$  |             
\__|                     \______/                \______/                      \______/              



 $$$$$$\                                    $$\                                                      
$$  __$$\                                   $$ |                                                     
$$ /  \__| $$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$ |                                                     
$$ |$$$$\  \____$$\ $$  _$$  _$$\ $$  __$$\ $$ |                                                     
$$ |\_$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |\__|                                                     
$$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|                                                         
\$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\ $$\                                                      
 \______/  \_______|\__| \__| \__| \_______|\__|                                                     
                                                                                                     
                                               
""")
            print("Congradulations! You have reached the end of the game! (Or at least the demo!)")
            Print("Enter any command to go back to main menu:")
            endGameYn = input(">")
            break
#This section of code plays the credits for the game:
def credits_():
    continueYn="null"
    print("""
        :::   :::       :::     :::::::::  ::::::::::        :::       ::: ::::::::::: ::::::::::: :::    :::            
      :+:+: :+:+:    :+: :+:   :+:    :+: :+:               :+:       :+:     :+:         :+:     :+:    :+: :+:         
    +:+ +:+:+ +:+  +:+   +:+  +:+    +:+ +:+               +:+       +:+     +:+         +:+     +:+    +:+              
   +#+  +:+  +#+ +#++:++#++: +#+    +:+ +#++:++#          +#+  +:+  +#+     +#+         +#+     +#++:++#++               
  +#+       +#+ +#+     +#+ +#+    +#+ +#+               +#+ +#+#+ +#+     +#+         +#+     +#+    +#+                
 #+#       #+# #+#     #+# #+#    #+# #+#                #+#+# #+#+#      #+#         #+#     #+#    #+# #+#             
###       ### ###     ### #########  ##########          ###   ###   ###########     ###     ###    ###                  
      :::::::::  :::   ::: ::::::::::: :::    :::  ::::::::  ::::    :::          ::::::::       ::::::::       :::::::: 
     :+:    :+: :+:   :+:     :+:     :+:    :+: :+:    :+: :+:+:   :+:         :+:    :+:     :+:    :+:     :+:    :+: 
    +:+    +:+  +:+ +:+      +:+     +:+    +:+ +:+    +:+ :+:+:+  +:+                +:+     +:+    +:+            +:+  
   +#++:++#+    +#++:       +#+     +#++:++#++ +#+    +:+ +#+ +:+ +#+             +#++:       +#++:++#          +#++:    
  +#+           +#+        +#+     +#+    +#+ +#+    +#+ +#+  +#+#+#                +#+     +#+    +#+            +#+    
 #+#           #+#        #+#     #+#    #+# #+#    #+# #+#   #+#+#         #+#    #+# #+# #+#    #+# #+# #+#    #+#     
###           ###        ###     ###    ###  ########  ###    ####          ########  ###  ########  ###  ########  
    """)
    input(">")
    print("""
          :::           ::::    ::: :::    ::: :::        :::                         :::     :::     :::   ::: :::::::::: ::::::::  :::    :::     :::  
       :+: :+:         :+:+:   :+: :+:    :+: :+:        :+:                       :+: :+:   :+:     :+:   :+: :+:       :+:    :+: :+:   :+:    :+: :+: 
     +:+   +:+        :+:+:+  +:+ +:+    +:+ +:+        +:+                      +:+   +:+  +:+      +:+ +:+  +:+       +:+        +:+  +:+    +:+   +:+ 
   +#++:++#++:       +#+ +:+ +#+ +#+    +:+ +#+        +#+       +#++:++#++:++ +#++:++#++: +#+       +#++:   +#++:++#  +#++:++#++ +#++:++    +#++:++#++: 
  +#+     +#+       +#+  +#+#+# +#+    +#+ +#+        +#+                     +#+     +#+ +#+        +#+    +#+              +#+ +#+  +#+   +#+     +#+  
 #+#     #+#       #+#   #+#+# #+#    #+# #+#        #+#                     #+#     #+# #+#        #+#    #+#       #+#    #+# #+#   #+#  #+#     #+#   
###     ###       ###    ####  ########  ########## ##########              ###     ### ########## ###    ########## ########  ###    ### ###     ###    
    
    
      :::::::::  :::::::::   ::::::::  :::::::::  :::    :::  :::::::: ::::::::::: ::::::::::: ::::::::  ::::    :::                                     
     :+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:    :+:    :+:         :+:    :+:    :+: :+:+:   :+:                                      
    +:+    +:+ +:+    +:+ +:+    +:+ +:+    +:+ +:+    +:+ +:+           +:+         +:+    +:+    +:+ :+:+:+  +:+                                       
   +#++:++#+  +#++:++#:  +#+    +:+ +#+    +:+ +#+    +:+ +#+           +#+         +#+    +#+    +:+ +#+ +:+ +#+                                        
  +#+        +#+    +#+ +#+    +#+ +#+    +#+ +#+    +#+ +#+           +#+         +#+    +#+    +#+ +#+  +#+#+#                                         
 #+#        #+#    #+# #+#    #+# #+#    #+# #+#    #+# #+#    #+#    #+#         #+#    #+#    #+# #+#   #+#+#                                          
###        ###    ###  ########  #########   ########   ########     ###     ########### ########  ###    ####                                           
    
    
    
     """)
    input(">")
    print("Did you really think the Dev team would give up our idenity so easily??? ;)")
    input(">")
#This function governs how "cheat codes" work in the game:
def cheatCode():
    CC = input("\nEnter a code:\n>")
    #This cheat code allows the user to read any book in the game:
    if CC == "read":
        readInput = input("""Please select a book to read:
        \n1. Orlando: A Biography, by Virgina Woolf
        \n2. Carmilla, by Joseph Sheridan Le Fanu
        \n3. Ulyssses, by James Joyce
        \n4. Dr. Blair's Grimore, by Dr. Blair\n""")
        if readInput == "1" or readInput == "1.":
            readBook("Orlando: A Biography, by Virgina Woolf")
        elif readInput == "2" or readInput == "2.":
            readBook("Carmilla, by Joseph Sheridan Le Fanu")
        elif readInput == "3" or readInput == "3.":
            readBook("Ulyssses, by James Joyce")
        elif readInput == "4" or readInput == "4.":
            readBook("Dr. Blair's Grimore, by Dr. Blair")
    #This cheat code displays the source code:
    elif CC == "code":
        readBook("Dr. Blair's Grimore, by Dr. Blair")
    #This cheat code displays the credits:
    elif CC == "credits":
        credits_()
    #This cheatcode displays the hidden painting found on the wall of the "Dark Room":
    elif CC=="enjoy art":
        easterEgg1()
    #This cheat code starts the mainGame(): function:
    elif CC=="play the game":
        mainGame("y")
    #This cheat code gives the player a list of commands to work use when navigating the wonderful world of Pork!:
    elif CC=="help":
        print("""
Pork! Basic Commands:
1. move [direction] = move in a direction (North, South, East, or West!)
2. take [object] = take an object and add it to your inventory
3. use [object] = use an object in your inventory if possible
4. read [object] = read the contents of an object for information
5. open [object] = open an object
6. search [object] = search through an object and see it's contents
Note: Some commands are not listed here and are meant to be discovered by the player
(Hint: make sure you "enjoy" the painting!)
        """)
#This is the startup menu for the game, it presents the player with a list of options and then has then select from that list:
def menu():
    MenuUpYn = "y"
    while MenuUpYn == "y":
        print("""
    █ ▄▄  ████▄ █▄▄▄▄ █  █▀  ▄                                                
    █   █ █   █ █  ▄▀ █▄█   █                                                 
    █▀▀▀  █   █ █▀▀▌  █▀▄  █                                                  
    █     ▀████ █  █  █  █ █                                                  
     █            █     █                                                     
      ▀          ▀     ▀   ▀                                                  
                                                                          
    █ ▄▄ ▀▄    ▄   ▄▄▄▄▀ ▄  █ ████▄    ▄        ▄▄▄▄▄▄   ████▄ █▄▄▄▄ █  █▀  ▄ 
    █   █  █  █ ▀▀▀ █   █   █ █   █     █      ▀   ▄▄▀   █   █ █  ▄▀ █▄█   █  
    █▀▀▀    ▀█      █   ██▀▀█ █   █ ██   █      ▄▀▀   ▄▀ █   █ █▀▀▌  █▀▄  █   
    █       █      █    █   █ ▀████ █ █  █      ▀▀▀▀▀▀   ▀████ █  █  █  █ █   
     █    ▄▀      ▀        █        █  █ █                       █     █      
      ▀                   ▀         █   ██                      ▀     ▀   ▀   
                                                                          
    """)
    #This section of code prints the main menu:
        print ('\033[1m' + 'Main Menu:'+'\033[0m')
        print("\n1. Start Game")
        print("2. Play Credits")
        print("3. Enter Cheat Code")
        print("4. Exit Game")
    #This line of code controls user input so they can select an option from the menu:
        menuInput = input(">")
    #This section of code runs if the user selects "1. Start Game"
        if menuInput == "1" or menuInput == "1." or menuInput == "Start Game" or menuInput == "Start game"\
        or menuInput == "start game" or menuInput == "start Game":
            MenuUpYn == "n"
            print("\n" * 30)
            mainGame("y")
    #This section of code runs if the user selects "2. Play Credits":
        elif menuInput == "2" or menuInput == "2." or menuInput == "Play Credits" or menuInput == "Play credits"\
        or menuInput == "play credits" or menuInput == "play Credits":
            credits_()
    #This section of code runs if the user selects "3. Enter Cheat Code":
        elif menuInput == "3" or menuInput == "3." or menuInput == "Enter Cheat Code" or menuInput == "Enter Cheat code"\
        or menuInput == "Enter cheat code" or menuInput == "enter cheat code"\
        or menuInput == "enter Cheat code"or menuInput == "enter Cheat Code"or menuInput == "Enter cheat Code":
            cheatCode()
    #This section of code runs if the user selects "4. Exit Game":4
        elif menuInput == "4" or menuInput == "4." or menuInput == "Exit Game" or menuInput == "Exit game"\
        or menuInput == "exit game" or menuInput == "exit Game":
            quit()
menu()