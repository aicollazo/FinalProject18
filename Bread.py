print("All You Knead is Love: A Bread Dating Simulator\n")
name = input("Enter your name!\n")

A = input("Great are you bready to get this bread! Y/N\n")
while A not in ['yes', 'y', 'Y', 'Yes']:
  print(f"You're not allowed to say no, {name}")
  A = input()
print("Let's getis this breadis...\n")

def print_inventory():
    global inventory
    for key in inventory:
        print(f"{key}:{inventory[key]}")
    return

inventory = {
    'Hot cocoa': 0,
    'Journals': 0,
    'Magazines': 0,
    'Keychains': 0,
    'Mango Ice cream': 0,
    'Hearts': 8
    }
c = input("Check out your inventory by pressing 'i'!")
if c == "i":
    print_inventory()
if inventory['Hearts'] == 0:
    print("Oh no, you lost so much love that you couldn't bring yourself to go to prom\n")
    print("GAME OVER")
#for reference, this is how to add items to the inventory inventory['Hot cocoa']+=1



class character:
  def __init__(self, name, year, school, bread, funfacts, alignment):
    self.name = name
    self.year = year
    self.school = school
    self.bread = bread
    self.funfacts = funfacts
    self.alignment = alignment
  def describe(self):
    print(f"""{self.name}:
    - Year: {self.year}
    - School: {self.school}
    - Bread Type: {self.bread}
    - Fun Facts!: {self.funfacts}
    - Alignment: {self.alignment}""")
    return
Dirk = character('Dirk', 11, 'APA', 'Whole grain', 'loves singing, dancing, watching horror movies with some hot cocoa, hanging out with friends by the lake', 'Looks like a cinnamon roll and is one, lawful good')
JC = character('JC', 12, 'UCT','Croissant', 'loves hanging out at starbucks, best friends with the duolingo owl, enjoys macchiatos and crunching fallen leaves', 'Looks like a cinnamon roll but could kill you, lawful neutral')
Marie = character('Marie', 12,'AAHS', 'Baguette', 'Super into dermatology, fashion magazines, loves boxing and takes classes at Tiger Bread Schulmann, dog walking', 'Looks like she could kill you, can actually kill you, true neutral ')
Xavier = character('Xavier', 12,'MHS', 'Cuban', 'loves videogames and cosplay, 80s and 90s hip hop, had his first kiss to sir-mix-alots Baby Got Back', 'Looks like a cinnamon roll but could kill you, chaotic good')
Naomi = character('Naomi', 11, 'AIT', 'Naan', 'loves coding, looks darn good in suits, grew up on Studio Ghibli, will love you forever if you get her mango icecream', 'Looks like she could kill you, is actually a cinnamon roll, neutral good')



print(f"Ah UCVTS. An ordinary campus like any other, save for its vocational classes. It has your usual clubs and activities like most schools. One of those activities of course being prom. It's a week away and while you may have everything prepared, you seem to lack a date. That's no matter to you, I'm sure you'll win someone over. While thinking about the prom you suddenly remember that you promised Dirk, your best friend since elementary school, that you'd help set up for Drama Club's spring show. You are currently in AAHS, the medical school, and need to find him. \n")

location = input("Where will you go?: bathroom, auditorium, classroom\n")
while location not in ['bathroom', 'auditorium', 'classroom']:
  print("Please give an answer. Maybe you spelled it wrong?")
  location = input()
if location == 'bathroom':
  print("You went to the bathroom, it was sooooo eventful")
  location = input("Where will you go?: auditorium, classroom\n")
  while location not in ['auditorium', 'classroom']:
    print("Please give an answer. Maybe you spelled it wrong?")
    location = input()
if location == 'classroom':
  print("You walked into the classroom and got scared by the way too realistic CPR dummies. You bolt out, scared for life.")
  location = input("Where will you go?: bathroom, auditorium\n")
  while location not in ['auditorium', 'bathroom']:
    print("Please give an answer. Maybe you spelled it wrong?")
    location = input()
if location == 'bathroom':
  print("You went to the bathroom, it was sooooo eventful")
  location = input("Where will you go?: auditorium\n")
  while location not in ['auditorium']:
    print("Please give an answer. Maybe you spelled it wrong?")
    location = input()
if location == 'auditorium':
  print("You travel downstairs.")

print(f"DIRK: Hey {name}, I was just about to go looking for you!\n")
location = input("DIRK:Where were you?: bathroom, classroom\n")
while location not in ['bathroom', 'classroom']:
  print("DIRK:Huh?? Come on tell me where you were!")
  location = input()
if location == 'bathroom':
  print("DIRK:Oh ok, hope you're feeling well!")
if location == 'classroom':
    print("DIRK: Oh did you get scared by the CPR dummies too?? They're so freaky right!")

print(f"DIRK: Anyways, I really could use your help! I need to memorise my lines but I have no partner.")
answer = input("""DIRK: Can you help me?
A: Sorry I can't! Maybe next time
B: Sure, what do you need me to do?\n""")
while answer not in ['A', 'B', 'a', 'b']:
  print("DIRK:Huh?? Come on give me an answer!")
  answer = input()
if answer in ['A', 'a']:
    print("Dirk looks dissapointed but hides it with a smile\n")
    print("DIRK: Oh...that's alright, I understand you're busy and all..\n")
    inventory['Hearts']-=1
    print(f"Oh no! Because you dissapointed Dirk you lost one heart!")
    print(f"Hearts: {inventory['Hearts']}")
if answer in ['B','b']:
    print("""Dirk starts flailing his arms excitedly.
    DIRK: YAY! Let's get started then!!\n""")
    print("You and Dirk run lines together in the auditorium, chatting during your session. You've always know him to be the shy type but you never expected him to blush as much as he did when you ran romantic scenes.")
    print("DIRK: Thank's again for running lines with me, you're so good to me. Oh! Here!\n")
    inventory['Hot cocoa']+=2
    print("Dirk gives you two packets of hot cocoa! You were such a big help that you gained a heart from the experience!")
    inventory['Hearts']+=1
    print_inventory()

print("You go home and think about the day. It was kind of short, wasn't it? Almost as if the programmer couldn't be bothered to narrate your school day because you're supposed to get busy falling in love. Ok I've said too much now.")
print("DAY 2...")
wakingup = input("""You wake up at about 6AM. You don't feel rested in the slightest but you're still willing to take on the day! Do you
A: Hit snooze and sleep for another hour
B: Get up and ready\n""")
while wakingup not in ['A', 'B', 'a', 'b']:
    print(f"You gotta choice something, {name}")
    wakingup = input()
if wakingup in ['A', 'a']:
    print("Yikes. You slept through your second alarm and now you've missed the bus. You decide you can make the run and barely arrive by 7:50, soaked in sweat. However, because you did cardio, you gain a heart!")
    inventory['Hearts']+=1
if wakingup in ['B', 'b']:
    print("You get up on time and prep yourself for the day. You got on your bus on time and were able to walk around the quad for a bit. Suddenly you spot something on the ground. Hey, it's a keychain that screams 'IT WAS ME, DIO!'. You decide to pocket it, maybe it'll come in handy later?")
    inventory['Keychains']+=1

c = input("Check out your inventory by pressing 'i'!")
if c == "i":
    print_inventory()

print("Entering the building, you begin walking to your Spanish class while reading a book. You’re incredibly enthralled by your, The Great Gatsby.\n")
print("You’re enthralled by the reading, truly Fitzgerald has done it again, you think to yourself. You’re so caught up in the description of Gatsby’s smile that you fail to notice the figure running towards you.\n")
status = input(f"""??? and {name} : AGH!
Lying across from you is a beautiful naan bread in a suit. You both fell after she ran into you
???: Hey are you ok??
A: Yeah, are you alright??
B: Watch where you’re going, ugh!
C: Guess you could say I’m falling for you ;)""")
while status not in ['A', 'a', 'B', 'b', 'C', 'c']:
    print("Ok edgelord, you’ve gotta have some emotion.")
    status = input()

if status in ['A', 'a']:
    print(f"""???: Yeah I’m fine, thanks for asking. Oh here you dropped your book. Good reading choice by the way ;).
    Realisation suddenly covers her face as she scrambles to pick up her scattered belongings.
    ???: I’ve got to get going, business conference and all. Name’s Naomi by the way! Bye!
    She runs off while brushing down her suit. She seemed awfully nice, quite rushed and clumsy. As you fix yourself up before heading to class you notice a slip of paper on the floor. The paper reads ‘SINGH, NAOMI’.
    {name}: Oh shoot! She must have dropped this. I’ll have to give it to her later. You put the paper in a journal and head off to class.\n""")
    inventory['Journals']+=1
if status in [ 'B', 'b']:
    print(f"""???: Oh sorry then. Oh shoot! I might miss my conference. Sorry again!
    She runs off while brushing down her suit. She seemed awfully nice, quite rushed and clumsy. As you fix yourself up before heading to class you notice a slip of paper on the floor. The paper reads ‘SINGH, NAOMI’.
    {name}: Oh shoot! She must have dropped this. I’ll have to give it to her later.
    You put the paper in a journal and head off to class.\n""")
    print(" you decided to be rude to Naomi you lose a heart.")
    inventory['Journals']+=1
    inventory ['Hearts']-=1

if status in ['C', 'c']:
    print(f"""???: Hahahahaha
    She lets out a long laugh though she is blushing through it.
    ???: Hey you’re the apple of my RYE! ;p
    She laughs at her own pun, clearly amused with herself.
    ???: Thanks for that, I’m a little on edge and really needed that laugh. Here, have a keychain for your troubles. Oh shoot I’ve gotta get going! Nice talking to you though, name’s Naomi!
    She runs off while brushing down her suit. She seemed awfully nice, quite rushed and clumsy. As you fix yourself up before heading to class you notice a slip of paper on the floor. The paper reads ‘SINGH, NAOMI’.
    {name}: Oh shoot! She must have dropped this. I’ll have to give it to her later.
    You put the paper in a journal and head off to class.\n""")
    inventory['Journals']+=1
    inventory['Hearts']+=1
    inventory['Keychains']+=1



#level2:meet xavier and naomi






