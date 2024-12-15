'''
Name:  Austin Schwalbe
Date:  31 January 2021
Description:  Room Adventure: Revolutions computer game
References:  COSC 1351 - Room Adventures | RealPython.com/python-gui-tkinter/
'''

##############################################################################

from tkinter import *
from time import time
from timer import timer_start, timer_stop
from random import randint

pass_mode = False
         
# blueprint for room
class Room(object):
    # constructor
    def __init__(self, name, image, locked):
        # rooms have a name, an image (the name of a file), exits (e.g. south), exit locations (e.g. to the south is room n),
        # items (e.g. table), item descriptions (for each item), and grabbables (things that can be taken)
        self.name = name
        self.image = image
        self.locked = locked
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []

    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    
    @property
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self, value):
        self._locked = value


    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

# add exit to room, exit is a string (e.g. north), room is an instance of Room
    def addExit(self, exit, room):
        #append exit and room to appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)

# add item to room, item is a string (e.g. table), description is a string that
# describes item (e.g. it is made of wood)
    def addItem(self, item, desc):
        # append the itema and description to appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)

# add item to room, item is a string (e.g. table), description is a string that
# describes item (e.g. it is made of wood)
    def delItem(self, item):
        # append the item and description to appropriate lists
        self._items.remove(item)

# adds a grabbable item from room, item is a string (e.g. key)
    def addGrabbables(self, item):
        # append item to list
        self._grabbables.append(item)

# removes grabbable item from room, item is string (e.g. key)
    def delGrabbables(self, item):
        # remove item from list
        self._grabbables.remove(item)

# returns a string description of the room
    def __str__(self):
        # first, the room name
        s = "Current room: {}.\n".format(self.name)

        # next, the items in the room
        s += "You see: "
        for item in self.items:
            s += item + "   "
        s += "\n"

    # next, the exits from the room
        s += "Exits: "
        for exit in self.exits:
            s += exit + "   "

        return s


# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
    
    # the constructor
    def __init__(self, parent):
        
        # call the constructor in the superclass
        Frame.__init__(self, parent)

    # set the current room image
    def setRoomImage(self):
        
        if (Game.currentRoom == None):
            # if dead, set the death image
            Game.img = PhotoImage(file="images/death.png")
        else:
            # otherwise grab the image for the current room
            Game.img = PhotoImage(file=Game.currentRoom.image)
               
        # display the image on the left of the GUI
        Game.image.config(image=Game.img)
        Game.image.image = Game.img


    def generatePasscodes(self):

        # initialize global variables for passcodes
        global den_pass
        global garage_pass
        global treasure_left_pass
        global treasure_right_pass

        # initialize global variables for passcode parts
        global left_pass_1
        global left_pass_2
        global left_pass_3

        global right_pass_1
        global right_pass_2
        global right_pass_3

        # randomize passcodes and typecast them to strings so they are readable by input
        den_pass = randint(1000, 8999)
        den_pass = str(den_pass)
        
        garage_pass = randint(1000, 8999)
        garage_pass = str(garage_pass)

        # randomize passcode parts and typecast them to strings so they are readable by code
        left_pass_1 = randint(10, 99)
        left_pass_2 = randint(10, 99)
        left_pass_3 = randint(10, 99)

        right_pass_1 = randint(10, 99)
        right_pass_2 = randint(10, 99)
        right_pass_3 = randint(10, 99)
        
        left_pass_1 = str(left_pass_1)
        left_pass_2 = str(left_pass_2)
        left_pass_3 = str(left_pass_3)

        right_pass_1 = str(right_pass_1)
        right_pass_2 = str(right_pass_2)
        right_pass_3 = str(right_pass_3)

        # initalize passcode parts
        treasure_left_pass = "{}{}{}".format(left_pass_1, left_pass_2, left_pass_3)
        treasure_right_pass = "{}{}{}".format(right_pass_1, right_pass_2, right_pass_3)
        
    
    # creates the rooms
    def createRooms(self):
        # there are three floors in the mansion: first floor (f), second floor (s), and basement (b)
        # make the rooms global
        
        global f1
        global f2
        global f3
        global f4
        global f5
        global f6
        global f7
        global f8
        global f9
        global f10
        global f11
        global f12
        global f13
        global f14
        global f15
        global f16
        
        global s1
        global s2
        global s3
        global s4
        global s5
        global s6

        global b1
        global b2
        global b3
        global b4
        global b5
        global b6
        global b7
        global b8
        global b9
        global b10
        global b11

        global w1


        # create the rooms and give them meaningful names
        
        f1 = Room("Porch", "images/first/f1.png", False)
        f2 = Room("Car", "images/first/f2.png", False)
        f3 = Room("Living Room", "images/first/f3.png", True)
        f4 = Room("Kitchen", "images/first/f4.png", False)
        f5 = Room("Storage Room", "images/first/f5.png", False)
        f6 = Room("Den", "images/first/f6.png", True)
        f7 = Room("Mudroom", "images/first/f7.png", False)
        f8 = Room("Garage", "images/first/f8.png", True)
        f9 = Room("Hallway", "images/first/f9.png", True)
        f10 = Room("Banquet Hall", "images/first/f10.png", False)
        f11 = Room("Courtyard", "images/first/f11.png", False)
        f12 = Room("Corridor", "images/first/f12.png", True)
        f13 = Room("Bedroom", "images/first/f13.png", False)
        f14 = Room("Bathroom", "images/first/f14.png", False)
        f15 = Room("Closet", "images/first/f15.png", False)
        f16 = Room("Secret Room", "images/first/f16.png", True)
        
        s1 = Room("Upstairs Hallway", "images/second/s1.png", False)
        s2 = Room("Media Room", "images/second/s2.png", True)
        s3 = Room("Bedroom", "images/second/s3.png", True)
        s4 = Room("Bathroom", "images/second/s4.png", False)
        s5 = Room("Closet", "images/second/s5.png", False)
        s6 = Room("Attic", "images/second/s6.png", True)
        
        b1 = Room("Basement", "images/basement/b1.png", True)
        b2 = Room("Basement", "images/basement/b2.png", False)
        b3 = Room("Basement", "images/basement/b3.png", True)
        b4 = Room("Basement", "images/basement/b4.png", False)
        b5 = Room("Basement", "images/basement/b5.png", False)
        b6 = Room("Basement", "images/basement/b6.png", False)
        b7 = Room("Basement", "images/basement/b7.png", False)
        b8 = Room("Basement", "images/basement/b8.png", False)
        b9 = Room("Basement", "images/basement/b9.png", False)
        b10 = Room("Basement", "images/basement/b10.png", False)
        b11 = Room("Treasure Room", "images/basement/b11.png", True)   # final treasure room

        w1 = Room("YOU WIN!!!", "images/win.png", False)        # you win!!!
        
            
        ############ FIRST FLOOR ##############
        # F1
        f1.addExit("north", f3) # living room
        f1.addExit("west", f2)  # car
        

        # F2
        f2.addExit("east", f1)  # porch

        f2.addItem("dashboard", "There's the mansion key on the dash. Ain't gettin' in without it!")
        
        f2.addGrabbables("mansion key")

        
        # F3
        f3.addExit("north", f4) # kitchen
        f3.addExit("east", f6)  # den
        f3.addExit("south", f1) # porch
        f3.addExit("up", s1)    # upstairs hallway
            
        f3.addItem("tv", "A large, flatscreen television. Whoever lived here must've been pretty rich!")
        f3.addItem("couch", "It's all stained. You couldn't pay me to sit on it!")
        f3.addItem("chair", "I am NOT sitting on that!")
        f3.addItem("table", "An old coffee table. It's all chipped and scratched. How careless...")
        f3.addItem("stairs", "They lead upstairs.")

        
        # F4
        f4.addExit("south", f3) # living room 
        f4.addExit("east", f5)  # storage room
        f4.addExit("west", f7)  # mudroom
        
        f4.addGrabbables("upstairs key")

        f4.addItem("island", "Such beautiful marble countertops! Is that the upstairs key in the sink?")
        f4.addItem("cabinets", "I'm not an expert on wood, but I think those are made of oak....")


        # F5
        f5.addExit("east", f12)  # corridor
        f5.addExit("west", f4) # kitchen

        f5.addGrabbables("plank")
        f5.addGrabbables("den chest passcode")
        

        f5.addItem("large crate", "Wow! It's taller than me! I think I see the den chest passcode sitting on it.")
        f5.addItem("boxes", "I wonder what's in them....")
        f5.addItem("wall", "There's a really long plank leaning against the wall. Maybe I can use it as a bridge to get to the attic from the upstairs bedroom!")


        # F6
        f6.addExit("west", f3) # living room
        
        f6.addItem("bookcase", "Stocked to the brim with books. Who ever gets a chance to read this many books anyway?")
        f6.addItem("desk", "There's a mouldy book sitting on the desk. There's a -{}- written in red on the cover.".format(right_pass_2))
        f6.addItem("chest", "It's locked. Maybe there's something useful inside.")


        # F7
        f7.addExit("north", f7)  # stay put
        f7.addExit("south", f8) # garage
        f7.addExit("east", f4)  # kitchen
        
        f7.addItem("shoe tray", "I knew something smelled in here!")
        f7.addItem("garage door", "It leads into the garage...I think.")
        

        # F8
        f8.addExit("north", f7) # mudroom
        
        f8.addGrabbables("matches")

        f8.addItem("jalopy", "I'd hate to be seen on the freeway with that thing!")
        f8.addItem("toolbox", "There are some matches sitting on the toolbox. Maybe they can help me see in that storage room so I can find the passcode.")


        # F9
        f9.addExit("south", f7) # mudroom; exitting this way unlocks hallway
        f9.addExit("east", f10) # banquet hall 
        f9.addExit("up", s6)  # attic
        
        f9.addItem("ladder", "Hope nothing found its way into the attic after I came down...")
        f9.addItem("painting", "'Leonardo Da Vinci' by Mona Lisa. Priceless!")


        # F10
        f10.addExit("south", f11) # courtyard
        f10.addExit("west", f9)  # hallway
        
        f10.addItem("chandelier", "The only decent-looking thing in this house.")
        f10.addItem("tables", "Such beautiful white tablecloths! Well...aside from the stains, that is.")


        # F11
        f11.addExit("north", f10)  # banquet hall
        
        f11.addGrabbables("den key")

        f11.addItem("fountain", "All dried up. Wait...that must be the den key on the edge!")
        f11.addItem("bench", "Well, at least it's in better condition than the sofa. There is a --{} written on the bench in green.".format(left_pass_3))


        # F12
        f12.addExit("north", f13)  # banquet hall
        f12.addExit("west", f5)  # storage room
        f12.addExit("down", b1)  # basement
        
        f12.addItem("gate", "There's a ladder on the other side. I think it leads to the basement.")


        # F13
        f13.addExit("north", f14)  # bathroom
        f13.addExit("south", f12)    # corridor
        f13.addExit("east", f15)     # closet
        
        f13.addItem("room", "Whoever lived here sure keeps a tidy room!")


        # F14
        f14.addExit("south", f13)  # bedroom
        
        f14.addGrabbables("secret room key")

        f14.addItem("shampoo", "A nice minty scent. And I can't pronounce a single ingredient on the ingredients list!")
        f14.addItem("mirror", "Hello me!")
        f14.addItem("sink", "I think that's the secret room key on the sink!")


        # F15
        f15.addExit("north", f16)  # secret room
        f15.addExit("west", f13)  # bedroom
        
        f15.addItem("clothes", "Smells like mothballs.")
        f15.addItem("large crack", "Hey, there's a door in here!")
        

        # F16
        f16.addExit("south", f15)  # closet
        
        f16.addGrabbables("gate key")

        f16.addItem("ledge", "That looks like the gate key on the ledge! There is a {}-- written on the ledge in red.".format(right_pass_1))
        f16.addItem("portait", "What a lovely family!")


        ############ SECOND FLOOR ##############
        
        # S1
        s1.addExit("north", s3)  # bedroom
        s1.addExit("west", s2) # media room
        s1.addExit("south", None) # death!
        s1.addExit("down", f3) # living room

        s1.addItem("pool table", "Looks like it's never been used. What a waste!")
        s1.addItem("open window", "That's a long fall!")


        # S2
        s2.addExit("east", s1)  # upstairs hallway
        
        s2.addItem("tv", "Another TV...And it's not even that far from the living room!")
        
        
        # S3
        s3.addExit("north", s6) # w/ plank: attic  :  w/o plank: death!
        s3.addExit("south", s1)  # upstairs hallway
        s3.addExit("east", s4)  # bathroom
        s3.addExit("west", s5) # closet

            
        s3.addItem("bed", "There's a patch of dead bed bugs in the sheets!")
        s3.addItem("window", "I can see the attic window across the courtyard! There is a --{} written in red on the wall next to it.".format(right_pass_3))

        
        # S4
        s4.addExit("west", s3)  # bedroom

        s4.addGrabbables("garage door passcode")
        
        s4.addItem("tub", "Still filled with water! Eww!")
        s4.addItem("sink", "Is that the garage door passcode in the sink?")


        # S5
        s5.addExit("east", s3)  # bedroom
        
        s5.addGrabbables("mudroom_passcode")

        s5.addItem("cowboy hat", "Yee-haw!")


        # S6
        s6.addExit("south", s3) # bedroom
        s6.addExit("down", f9)  # hallway
        
        s6.addItem("crate", "Empty.")
        s6.addItem("chest", "Empty. There is a -{}- written in green on the side.".format(left_pass_2))


        ############ BASEMENT ##############
        # B1
        b1.addExit("north", b6)
        b1.addExit("west", b2)
        b1.addExit("up", f12)  # corridor

        # B2
        b2.addExit("north", b4)
        b2.addExit("east", b1)
        b2.addExit("west", b3)

        # B3
        b3.addExit("north", b5)
        b3.addExit("east", b2)

        # B4
        b4.addExit("north", b8)
        b4.addExit("south", b2)

        b4.addItem("floor", "There's the basement chest key sitting on the floor.")

        b4.addGrabbables("basement chest key")

        # B5
        b5.addExit("south", b3)

        b5.addItem("chest", "An old, green chest with a passcode lock.")

        # B6
        b6.addExit("west", b7)
        b6.addExit("south", b1)

        # B7
        b7.addExit("east", b6)

        b7.addItem("chest", "The lock is pretty rusty, but it might still work if there's a key around.")

        # B8
        b8.addExit("north", b10)
        b8.addExit("west", b9)
        b8.addExit("south", b4)

        # B9
        b9.addExit("east", b8)

        b9.addItem("chest", "It's a rusty, red chest. There's a 6-digit passcode lock on it.")

        # B10
        b10.addExit("west", b11)  # treasure room - final room!
        b10.addExit("south", b8)

        b10.addItem("wall paint", "It says {}-- in green.".format(left_pass_1))

        # B11
        b11.addExit("east", b10)

        b11.addItem("treasure chest", "There it is: the treasure chest!")  # interact with treasure chest via the "use" command to win


        # set room 1 as the current room at the beginning of the game (starting room)
        Game.currentRoom = f1
        
        # initialize the player's inventory (starting inventory)
        Game.inventory = []
        
    
    # sets up the GUI
    def setupGUI(self):

        # organize the GUI
        self.pack(fill=BOTH, expand=1)
        
        # setup the player input at the bottom of the GUI
        # the widget is a Tkinter Entry
        # set its background to white and bind the return key to the
        # function process in the class
        # push it to the bottom of the GUI and let it fill
        # horizontally
        # give it focus so the player doesn't have to click on it
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()
        
        # setup the image to the left of the GUI
        # the widget is a Tkinter Label
        # don't let the image control the widget's size
        img = None
        Game.image = Label(self, width=int(WIDTH / 2), image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)
        
        # setup the text to the right of the GUI
        # first, the frame in which the text will be placed
        text_frame = Frame(self, width=WIDTH / 2)
        
        # the widget is a Tkinter Text
        # disable it by default
        # don't let the widget control the frame's size
        Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)
    
    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
        # enable the text widget, clear it, set it, and disabled it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom == None):
            # if dead, let the player know
            Game.text.insert(END, "You fell out the window and died! Input 'exit' to quit.\n")
        else:
            # otherwise, display the appropriate status
            Game.text.insert(END, str(Game.currentRoom) +\
                "\nYou are carrying: " + str(Game.inventory) +\
                "\n\n" +  status)
            Game.text.config(state=DISABLED)

        
    
    # play the game
    def play(self):
        
        # add the rooms to the game
        self.createRooms()
        
        # configure the GUI
        self.setupGUI()
        
        # set the current room
        self.setRoomImage()
        
        # set the current status
        self.setStatus("")

        # start the speedrun timer
        timer_start()

        # define possible inputs for player to input
        global verbs_move
        global verbs_look
        global verbs_grab
        global verbs_use
        global words_exit
        
        verbs_move = ["go", "move", "travel", "saunter", "head", "step", "walk", "run", "sprint", "sneak", "creep", "charge"]
        verbs_look = ["look", "observe", "investigate", "see", "view", "check", "inspect"]
        verbs_grab = ["take", "steal", "pickup", "grab", "carry"]
        verbs_use = ["use", "activate", "open"]
        words_exit = ["quit", "exit", "bye", "sionara!", "adios"]

        # show player how to play
        global how_to_play
        
        how_to_play = \
        "Welcome to Room Adventures!\
        \n\
        \nIn this game, you will be traversing a mansion in search of a hidden treasure that is supposedly somewhere in the basement. You will do this by inserting text commands which will make your character perform certain actions.\
        \nHere are some tips that will be helpful:\
        \n\
        \n***MOVE***\
        \nTo move, simply type in a keyword followed by a possible exit. You cannot enter a locked room until you have picked up its respective key or have entered its respective passcode\
        \nPossible Keywords:  {}\
        \n\
        \n***LOOK***\
        \nTo look at an object, simply type in a keyword followed by an object your character sees in the room. Certain items can be used (see USE).\
        \nPossible Keywords:  {}\
        \n\
        \n***TAKE***\
        \nTo add an item to your inventory, simply type in a keyword followed by an item your character finds after inspecting objects in the room. Certain items such as passcodes can be used (see USE).\
        \nPossible Keywords:  {}\
        \n\
        \n***USE***\
        \nTo use an object in the room or an item in your inventory, simply type in a keyword followed by the object or item you would like to use. Use this commands to look at passcodes or interact with locked objects.\
        \nPossible Keywords:  {}\
        \n\
        \n***HELP***\
        \nIf you ever need to access this screen again, just type 'help'.\
        \n\
        \n***EXIT***\
        \nPossible Keywords:  {}\
        \nIf you want to quit the game, just type a keyword.\
        \n\
        \nThat's all you need to know! Good luck, and happy treasure hunting!".format(verbs_move, verbs_look, verbs_grab, verbs_use, words_exit)
        
        self.setStatus(how_to_play)


    def process(self, event):
        
        # grab the player's input from the input at the bottom of
        # the GUI
        action = Game.player_input.get()

        # set the user's input to lowercase to make it easier to
        # compare the verb and noun to known values
        action = action.lower()

        # set a default response
        response = "I don't understand. Type 'help' if you are having trouble."
        
        # define pass_mode for whether player can enter a passcode
        global pass_mode

        # exit the game if the player wants to leave
        if (action in words_exit):
            exit(0)

        # if the player is dead
        if (Game.currentRoom == "Death"):
            # clears the player's input
            Game.player_input.delete(0, END)
            return
            
        # split user input into words
        words = action.split()

        # define words that may appear between the verb and the noun. the code will not react to these words.
        filler_words = ["a", "an", "the", "to", "at"]

        # control the input
        if(len(words) >= 1):

            # first word is verb
            verb = words[0] 


            ######## FIND THE NOUN ########

            i = 0        # current index read by while loops
            first = 0    # index of first noun
            nouns = 0    # number of noun words in the input

            # check for length of input as well as index of first noun word
            while i < len(words):
                
                # find the index of the first noun word
                if (i != 0 and words[i] not in filler_words and first == 0):
                    first = i

                # find the number of noun words in the input
                if (i != 0 and words[i] not in filler_words):
                    nouns += 1

                i += 1

                if (i == words[-1]):
                    break

                # time out after 11 words (10 indexes) ('greater than' added to prevent glitches)
                if i >= 10:
                    break


            # set noun equal to the first noun word in the input
            noun = words[first]

            
            # use the length of the noun and the index of its first word to find the full noun and combine the words into a single string
            i = 0
            while i < nouns:

                # check next index
                i += 1   

                # stop the loop i is equal to number of nouns in input ('greater than' added to prevent glitches)
                if (i >= nouns):
                    break
                
                # keep adding words to the noun string until the noun is complete
                if (nouns > 1):
                    noun_add = words[first + i]             # set index of next noun word equal to index of i indexes after that of first noun
                    noun = "{} {}".format(noun, noun_add)   # add noun word at words[first + i] to noun string     

            ##### ENTERED PASSCODES ARE INCORRECT
            if ((words[0] != den_pass and Game.currentRoom == f6) or (words[0] != garage_pass and Game.currentRoom == f7) and pass_mode == True):
                response = "</...ERROR: PASSCODE INCORRECT.../>"

                # disable passcode mode
                pass_mode = False
                
                
                
            ##### MAKE THINGS HAPPEN DEPENDING ON VERB INPUTTED #####
            
            # the verb is: go
            if (verb in verbs_move):
                    
                                        
                    # check for valid exits in the current room
                    for k in range(len(Game.currentRoom.exits)):
                        
                        # set a default response
                        response = "Invalid exit."
                        
                        # a valid exit is found
                        if (noun == Game.currentRoom.exits[k]):

                            ##### check is the player is trying to access a locked exit #####
                            ##### FIRST FLOOR
                            # mansion
                            if (Game.currentRoom == f1 and noun == "north" and f3.locked == True):
                                response = "The mansion is locked...Must've left the key in the car!"

                                # stop checking for exits
                                break
                            
                            # den
                            if (Game.currentRoom == f3 and noun == "east" and f6.locked == True):
                                response = "The den is locked."

                                # stop checking for exits
                                break

                            # garage
                            if (Game.currentRoom == f7 and noun == "south" and f8.locked == True):
                                response = "The garage is locked by a passcode."

                                # stop checking for exits
                                break

                            # dark corridor - no matches or lantern
                            if (Game.currentRoom == f5 and noun == "east" and f12.locked == True and matches not in Game.inventory):
                                response = "I can't go in there! It's too dark to see."

                                # stop checking for exits
                                break

                            # dark corridor - matches but no lantern
                            if (Game.currentRoom == f5 and noun == "east" and f12.locked == True and matches in Game.inventory and lantern not in Game.inventory):
                                response = "These matches aren't bright enough! I need something brighter."

                                # stop checking for exits
                                break

                            # hallway - locked
                            if (Game.currentRoom == f7 and noun == "north" and f9.locked == True):
                                response = "The door is blocked off from behind. No way I'm getting in that way."

                                # stop checking for exits
                                break

                             # hallway - unlocked
                            if (Game.currentRoom == f7 and noun == "north" and f9.locked == False):
                                response = "Room changed."
                                Game.currentRoom = f9

                                # stop checking for exits
                                break

                            # mudroom - unlocks hallway 
                            if (Game.currentRoom == f9 and noun == "south" and f9.locked == True):
                                Game.currentRoom = f7
                                f9.locked = False
                                response = "Room changed. Door to the hallway is now unblocked."
                                # stop checking for exits
                                break

                            # secret room in closet
                            if (Game.currentRoom == f15 and noun == "north" and f16.locked == True):
                                response = "This secret room is locked."

                                # stop checking for exits
                                break



                            ##### SECOND FLOOR
                            # bedroom
                            if (Game.currentRoom == s1 and noun == "north" and s3.locked == True):
                                response = "The bedroom is locked."

                                # stop checking for exits
                                break
                            
                            # media room
                            if (Game.currentRoom == s1 and noun == "west" and s2.locked == True):
                                response = "The media room is locked."

                                # stop checking for exits
                                break

                            # attic
                            if (Game.currentRoom == s3 and noun == "north" and s6.locked == True):
                                Game.currentRoom = None

                                # stop checking for exits
                                break


                            ##### BASEMENT
                            # bedroom
                            if (Game.currentRoom == f12 and noun == "down" and "gate key" not in Game.inventory):
                                response = "The gate is locked. There must be a key around here somewhere."

                                # stop checking for exits
                                break
                            
                            # basement door
                            if (Game.currentRoom == b2 and noun == "west" and b3.locked == True and "basement door key" not in Game.inventory):
                                response = "The door is locked."

                                # stop checking for exits
                                break

                            # treasure room
                            if (Game.currentRoom == b10 and noun == "west" and b11.locked == True):
                                response = "The treasure room is locked. There are two indentations that form a circle in the wall."

                                # stop checking for exits
                                break



                            # if room is unlocked, change room
                            else:
                                # change the current room to the one that is associated with the specified exit
                                Game.currentRoom = Game.currentRoom.exitLocations[k]
                                
                                # set the response (success)
                                response = "Room changed."

                                # stop checking for exits
                                break
                            
        
            # the verb is: look
            elif (verb in verbs_look):
                    # set a default response
                    response = "I don't see that item."

                    # check for valid items in the current room
                    for i in range(len(Game.currentRoom.items)):
                        
                            # a valid item is found
                            if (noun == Game.currentRoom.items[i]):
                                
                                # set the response to the item's description
                                response = Game.currentRoom.itemDescriptions[i]

                                # no need to check any more items
                                break
                                
            # the verb is: take
            elif (verb in verbs_grab):
                # set a default response
                response = "I don't see that item."
                
                # check for valid grabbable items in the current room
                for grabbables in Game.currentRoom.grabbables:
                    # a valid grabbable item is found
                    if (noun == grabbables):
                        

                        # code for items other than the den chest passcode
                        if (noun != "den chest passcode"):
                            ##### check for keys - when picked up, unlock corresponding room and let player know that room is accessible #####

                            ## default response
                            response = "Item grabbed."

                            if (noun == "mansion key" and "mansion key" in grabbables):
                                f3.locked = False
                                response = "Item grabbed. Now I can get inside the mansion!"

                            if (noun == "upstairs key" and "upstairs key" in grabbables):
                                s2.locked = False
                                s3.locked = False
                                response = "Item grabbed. Now I can access the rooms upstairs!"

                            if (noun == "den key" and "den key" in grabbables):
                                f6.locked = False
                                response = "Item grabbed. Now I can access the den!"

                            if (noun == "secret room key" and "secret room key" in grabbables):
                                f16.locked = False
                                response = "Item grabbed. Now I can access the secret room in the closet!"

                            if (noun == "gate key" and "gate key" in grabbables):
                                b1.locked = False
                                response = "Item grabbed. Now I can access the basement!"


                            ##### check for items - when picked up, unlock corresponding room and let player know that room is accessible #####
                            
                            ## plank - access attic
                            if (noun == "plank" and "plank" in grabbables):
                                s6.locked = False
                                response = "Item grabbed. Now I can access the attic from the upstairs bedroom!"
                                

                            # add the grabbable item to the player's inventory
                            Game.inventory.append(grabbables)
                            
                            # remove the grabbable item from the room
                            Game.currentRoom.delGrabbables(grabbables)

                        #code specific to den chest passcode
                        else:
                            # checks if matches are in inventory before picking up den passcode
                            if (noun == "den chest passcode" and "den chest passcode" in grabbables and "matches" in Game.inventory):

                                # add the passcode item to the player's inventory
                                Game.inventory.append(grabbables)
                                
                                # remove grabbable from room
                                Game.currentRoom.delGrabbables(grabbables)

                                # response
                                response = "Item grabbed."

                            elif (noun == "den chest passcode" and "den chest passcode" in grabbables and "matches" not in Game.inventory):
                                response = "It's too dark! I can't find the passcode."
                        
                        # no need to check any more grabbable items
                        break            

            
            # the verb is: use
            elif (verb in verbs_use):

                # set a default response
                response = "I don't see that item."
                    
                ### DEN CHEST ###
                # use the passcode while item is in inventory to read code
                if (noun == "den chest passcode" and "den chest passcode" in Game.inventory):
                    response = "The code to the den chest is {}.".format(den_pass)

                    # disable passcode mode
                    pass_mode = False
                
                # if locked, enable passcode mode
                elif (noun == "chest" and Game.currentRoom == f6 and "lantern" not in Game.inventory):
                    response = "</...ENTER PASSCODE.../>"

                    # enable ability to enter passcode
                    pass_mode = True


                ### GARAGE DOOR ###
                # use the passcode while item is in inventory to read code
                if (noun == "garage door passcode" and "garage door passcode" in Game.inventory):
                    response = "The code to the garage door is {}.".format(garage_pass)

                     # disable passcode mode
                    pass_mode = False
                    
                # if locked, enable passcode mode
                elif (noun == "garage door" and Game.currentRoom == f7 and f8.locked == True):
                    response = "</...ENTER PASSCODE.../>"

                    # enable ability to enter passcode
                    pass_mode = True


                ### BASEMENT CHEST ###
                # tell player that the chest is locked if the player does not have key
                if (noun == "chest" and Game.currentRoom == b7 and "basement chest key" not in Game.inventory):
                    response = "It's locked."

                # give key to player if player has key to chest
                if (noun == "chest" and Game.currentRoom == b7 and "basement chest key" in Game.inventory and "basement door key" not in Game.inventory):
                    response = "Chest unlocked! I got the key to the basement door."
                    b3.locked = False
                    Game.inventory.append("basement door key")


                ### BASEMENT LEFT KEY CHEST ###
                # if locked, enable passcode mode
                elif (noun == "chest" and Game.currentRoom == b5 and "left treasure key" not in Game.inventory):
                    response = "</...ENTER PASSCODE.../>"

                    # enable ability to enter passcode
                    pass_mode = True


                 ### BASEMENT RIGHT KEY CHEST ###
                # if locked, enable passcode mode
                elif (noun == "chest" and Game.currentRoom == b9 and "right treasure key" not in Game.inventory):
                    response = "</...ENTER PASSCODE.../>"

                    # enable ability to enter passcode
                    pass_mode = True


                
                ### TREASURE CHEST - INTERACT TO WIN ###
                if (noun == "treasure chest" and Game.currentRoom == b11):
                    
                    # stop the timer
                    seconds = int(timer_stop())
                    minutes = int(0)

                    # divides seconds into seconds and minutes
                    while seconds > 60:
                        seconds -= 60
                        minutes += 1

                    # display how long it took
                    response = "It's...It's the treasure! I found it!!! And it took me only {} minutes and {} seconds.".format(minutes, seconds)

                    # set mode to "win"
                    Game.currentRoom = w1
                    
                    


            # enter the passcode to the den chest
            if (words[0] == den_pass and Game.currentRoom == f6 and pass_mode == True):
                response = "Chest unlocked! I got a lantern! Now I can see down that dark corridor."
                Game.inventory.append("lantern")
                f12.locked = False

                # disable passcode mode
                pass_mode = False

            # enter the passcode to the garage door
            if (words[0] == garage_pass and Game.currentRoom == f7 and pass_mode == True):
                garage_door_locked = False
                response = "Door unlocked! Now I can enter the garage."
                f8.locked = False

                # disable passcode mode
                pass_mode = False

            # enter the passcode to the left treasure key chest
            if (words[0] == treasure_left_pass and Game.currentRoom == b5 and pass_mode == True):
                response = "Chest unlocked! I got the left key to the treasure room."
                Game.inventory.append("left treasure key")

                # disable passcode mode
                pass_mode = False

            # enter the passcode to the right treasure key chest
            if (words[0] == treasure_right_pass and Game.currentRoom == b9 and pass_mode == True):
                response = "Chest unlocked! I got the right key to the treasure room."
                Game.inventory.append("right treasure key")

                # disable passcode mode
                pass_mode = False


            # show "how to play" screen again if player needs help
            if (verb == "help"):
                response = how_to_play

            # unlock treasure door if both keys are in inventory
            if ("left treasure key" in Game.inventory and "right treasure key" in Game.inventory):
                b11.locked = False

        
        # display the response on the right of the GUI
        # display the room's image on the left of the GUI
        # clear the player's input
        self.setStatus(response)
        self.setRoomImage()
        Game.player_input.delete(0, END)
    
               
##########################################################
        
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)

# generate passcodes
g.generatePasscodes()

# play the game
g.play()


# wait for the window to close
window.mainloop()
