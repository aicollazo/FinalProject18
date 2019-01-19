import time
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
    'Hearts': 8,
    'Energy': 30
    }
c = input("Check out your inventory by pressing 'i'!")
if c == "i":
    print_inventory()
#for game end:
#if inventory['Hearts'] == 0:
    #print("Oh no, you lost so much love that you couldn't bring yourself to go to prom\n")
    #print("GAME OVER")




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
Xavier = character('Xavier', 12,'MHS', 'Cuban', 'loves videogames and cosplay, 80s and 90s hip hop, had his first kiss to Kung Fu Fighting', 'Looks like a cinnamon roll but could kill you, chaotic good')
Naomi = character('Naomi', 11, 'AIT', 'Naan', 'loves coding, looks darn good in suits, grew up on Studio Ghibli, will love you forever if you get her mango icecream', 'Looks like she could kill you, is actually a cinnamon roll, neutral good')



print(f"""Ah UCVTS. An ordinary campus like any other, save for its vocational classes and it being one of the highest ranked schools in bread education.
That's right.
Bread education.
You see, in decades past, a new string of the flu virus was discovered and it for some reason, caused a mutation in bread. This mutation caused them to gain human like features, incuding a functioning brain. Your campus has been one of the few and most notable to accept these bread people into their school. You, dear {name}, have never known a world without these people, especially your best friend Dirk, a whole wheat bread slice.\n""")
time.sleep(10)
print(f"You and him have been friends since you were toddlers and have been inseparable since. You've accompanied eachother to all the school dances and every family function you could think of. Speaking of functions, you've seem to nearly forget about the prom! You and Dirk have been talking about it for a bit and even went shopping together for it but you seem to have forgot to ask someone out. But no worries, I'm sure your charming self will win someone over. The prom is on Saturday which gives you five days to find someone to ask out.\n")
time.sleep(10)
print(f"Anyways enough talk of the prom, you promised Dirk that you'd help out with his drama club show, you should probably go try and find him.\n")
print("MONDAY, DAY 1...\n")
time.sleep(5)

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
  print("You walked into the classroom and got scared by the way too realistic CPR dummies. You bolt out, scarred for life.")
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

print(f"DIRK: 'Hey {name}, I was just about to go looking for you!'\n")
location = input("DIRK:'Where were you?: bathroom, classroom'\n")
while location not in ['bathroom', 'classroom']:
  print("DIRK:'Huh?? Come on tell me where you were!'")
  location = input()
if location == 'bathroom':
  print("DIRK:'Oh ok, hope you're feeling well!'")
  time.sleep(3)
if location == 'classroom':
    print("DIRK: 'Oh did you get scared by the CPR dummies too?? They're so freaky right!'")
    time.sleep(3)

print(f"DIRK: 'Anyways, I really could use your help! I need to memorise my lines but I have no partner.'")
answer = input("""DIRK: 'Can you help me?'
A: Sorry I can't! Maybe next time
B: Sure, what do you need me to do?\n""")
while answer not in ['A', 'B', 'a', 'b']:
  print("DIRK:'Huh?? Come on give me an answer!'")
  answer = input()
if answer in ['A', 'a']:
    print("Dirk looks dissapointed but hides it with a smile\n")
    time.sleep(2)
    print("DIRK: 'Oh...that's alright, I understand you're busy and all...'\n")
    inventory['Hearts']-=1
    print(f"Oh no! Because you dissapointed Dirk you lost one heart!")
    print(f"Hearts: {inventory['Hearts']}")
if answer in ['B','b']:
    print("""Dirk starts flailing his arms excitedly.
    DIRK: 'YAY! Let's get started then!!'\n""")
    print("You and Dirk run lines together in the auditorium, chatting during your session. You've always know him to be the shy type but you never expected him to blush as much as he did when you ran romantic scenes.")
    time.sleep(3)
    print("DIRK: 'Thank's again for running lines with me, you're such a good friend. Oh! Here!'\n")
    inventory['Hot cocoa']+=2
    print("Dirk gives you two packets of hot cocoa! You were such a big help that you gained a heart from the experience!")
    inventory['Hearts']+=1


print("You go home and think about the day. It was kind of short, wasn't it? Almost as if the programmer couldn't be bothered to narrate your school day because you're supposed to get busy falling in love.\n")
time.sleep(2)
print("After doing your homework you decide to mess around on your phone to kill some time before sleeping.")
website = input("""Which website are you using?
A: Picturegram
B: Videotube
C: Crackchat\n""")
while website not in ['A', 'a', 'B', 'b', 'C', 'c']:
    print("You stare blankily at your screen before realising you haven't clicked on anything yet. Please choose somewhere to go.")
    website = input()
if website in ['A', 'a']:
    print("You decide to use picturegram to check up on some of your favourite accounts. You scroll through a dog blog's newest posts, showing off the cutest little corgi in a pumpkin costume. You decide to send the picture to Dirk.\n")
    time.sleep(5)
    print("Scrolling through, you get a notification that someone's requested to follow you. Opening it you see a teenage bread, cosplaying a character from your favourite video game. Their username is '@CrumbyCosplay'. You're immediately enamoured and follow back. You spend a few minutes scrolling through their blog admiring their craftsmanship and dedication to the hobby.\n")
    time.sleep(5)
    print("Before you know it, it's 11pm. Like the good student you are, you send Dirk a quick goodnight and get to sleeping.\n")
    print("Because you were so enamoured by the random cosplayer you gained 2 hearts!\n")
    inventory['Hearts']+=2
if website in ['B', 'b']:
    print("You decide to use Videotube to check up on some of your favourite accounts. You watch a 30 minute video essay about why OgreMan 2 is the perfect example of a good sequel. \n")
    time.sleep(5)
    print("While scrolling through your recommendations, you notice a short video titled 'Common Beginner's French Mistakes!'. You're intrigued and click on it. Once the video loads up, you notice a super chill croissant in a varsity jacket, who introduces herself as JC. She explain's the basics of French pronounciation and spelling with such confidence you're compelled to subscribe.\n")
    time.sleep(5)
    print("Before you know it, it's 11pm. Like the good student you are, you get to sleeping.\n")
    print("Because you were so engaged with the video, you decided to take up learning French in the meantime. You gained one journal!\n")
    inventory['Journals']+=1
if website in ['C', 'c']:
    print("You decide to use Crackchat to check up on some of your favourite accounts. You watch through your friends stories, mildly amused by one friend screaming 'I'M A REBEL' before dipping half a leg into the freezing lake.\n")
    time.sleep(5)
    print("While scrolling through your recommendations, you get a notification from Dirk. Opening it you see the caption 'OMFG DUDE LOOK PRETTY GIRL'. You open the picture to see a beautiful baguette lounging at a cafe. She's reading from a journal while having a drink, clearly a candid moment. The caption reads 'Why my friend a whole model out here :,('. You decide to add the bread, her username being '@MariewithBrie<3'. You end up looking through her whole story.\n")
    time.sleep(5)
    print("Before you know it, it's 11pm. Like the good student you are, you get to sleeping.\n")
    print("Because you were so enamoured by Marie, you gain one heart.\n")
    inventory['Hearts']+=1

print("At the end of each day, you can check on your inventory when prompted! You can always ignore it though. You can also get a description of the new breads you've met!\n")
c = input("Check out your inventory by pressing 'i'!\n")
if c == "i":
    print_inventory()

info = input("Check out the bread you know so far by pressing 'b'!\n")
if info == "b":
    Dirk.describe()
time.sleep(3)


print("TUESDAY, DAY 2...\n")
wakingup = input("""You wake up at about 6AM. You don't feel rested in the slightest but you're still willing to take on the day! Do you
A: Hit snooze and sleep for another hour
B: Get up and ready\n""")
while wakingup not in ['A', 'B', 'a', 'b']:
    print(f"You gotta choice something, {name}")
    wakingup = input()
if wakingup in ['A', 'a']:
    print("Yikes. You slept through your second alarm and now you've missed the bus. You decide you can make the run and barely arrive by 7:50, soaked in sweat. You notice a magazine on the ground and decide to put it in your bag. Good reading material for when you're bored in class. However, because you did cardio, you gain a heart!")
    inventory['Hearts']+=1
    inventory['Magazines']+=1
if wakingup in ['B', 'b']:
    print("You get up on time and prep yourself for the day. You got on your bus on time and were able to walk around the quad for a bit. Suddenly you spot something on the ground. Hey, it's a keychain that screams 'IT WAS ME, DIO!'. You decide to pocket it, maybe it'll come in handy later?")
    inventory['Keychains']+=1
    inventory['Energy']+=10

c = input("Check out your inventory by pressing 'i'!")
if c == "i":
    print_inventory()

print("Entering the building, you begin walking to your Spanish class while reading a book.\n")
print("You’re enthralled by the reading, truly Fitzgerald has done it again, you think to yourself. You’re so caught up in the description of Gatsby’s smile that you fail to notice the figure running towards you.\n")
status = input(f"""??? and {name} : AGH!
Lying across from you is a beautiful naan bread in a suit. You both fell after she ran into you.
???: 'Hey are you ok?'
A: Yeah, are you alright??
B: Watch where you’re going, ugh!
C: Guess you could say I’m falling for you ;)""")
while status not in ['A', 'a', 'B', 'b', 'C', 'c']:
    print("Ok edgelord, you’ve gotta have some emotion.")
    status = input()

if status in ['A', 'a']:
    print(f"""???: 'Yeah I’m fine, thanks for asking. Oh here you dropped your book. Good reading choice by the way ;).'
    Realisation suddenly covers her face as she scrambles to pick up her scattered belongings.
    ???: 'I’ve got to get going, business conference and all. Name’s Naomi by the way! Bye!'
    She runs off while brushing down her suit. She seemed awfully nice, quite rushed and clumsy. As you fix yourself up before heading to class you notice a slip of paper on the floor. The paper reads ‘SINGH, NAOMI’.
    {name}: 'Oh shoot! She must have dropped this. I’ll have to give it to her later. You put the paper in a journal and head off to class.'\n""")
    time.sleep(30)
    inventory['Journals']+=1
if status in [ 'B', 'b']:
    print(f"""???: 'Oh sorry then. Oh shoot! I might miss my conference. Sorry again!'
    She runs off while brushing down her suit. She seemed awfully nice, quite rushed and clumsy. As you fix yourself up before heading to class you notice a slip of paper on the floor. The paper reads ‘SINGH, NAOMI’.
    {name}: 'Oh shoot! She must have dropped this. I’ll have to give it to her later.
    You put the paper in a journal and head off to class.'\n""")
    print(f"{name} decided to be rude to Naomi and lost a heart.")
    time.sleep(30)
    inventory['Journals']+=1
    inventory ['Hearts']-=1

if status in ['C', 'c']:
    print(f"""???: 'Hahahahaha'
    She lets out a long laugh though she is blushing through it.
    ???: 'Hey you’re the apple of my RYE! ;p'
    She laughs at her own pun, clearly amused with herself.
    ???: 'Thanks for that, I’m a little on edge and really needed that laugh. Here, have an energy card for your troubles. Oh shoot I’ve gotta get going! Nice talking to you though, name’s Naomi!'
    She runs off while brushing down her suit. She seemed awfully nice, quite rushed and clumsy. As you fix yourself up before heading to class you notice a slip of paper on the floor. The paper reads ‘SINGH, NAOMI’.
    {name}: 'Oh shoot! She must have dropped this. I’ll have to give it to her later.
    You put the paper in a journal and head off to class.'\n""")
    time.sleep(30)
    inventory['Journals']+=1
    inventory['Hearts']+=1
    inventory['Energy']+=10

print("""SR. MELONPAN: 'Alright everybready, remember to do the worksheet for homework and grab your phones.' Sr. Melonpan stands by his desk announcing the end of your Spanish class. You walk up to the hanging case to grab your phone while chatting with Dirk.
DIRK: 'God I'm so tiredddddd. Drama club is really taking the energy out of me.' he says, slouching over.'""")
inventory['Energy']-=20
time.sleep(10)
print(f"{name}:'Oof yikes, how's that going?'")
time.sleep(10)
print(f"""DIRK: 'I messed up one of my lines and accidentally said 'Mike's Hard Pass' and totally embarrassed myself.' he groaned.
{name}: 'Wow! Even more embarrasing than that time you accidentally introduced yourself as 'Dirt'?'
DIRK: 'Oh god don't remind me of that.' he chuckles while recalling the memory.\n""")
time.sleep(10)
print(f"""DIRK: 'Anways, let's get going, I wanna get some spirit points from Magnet for spirit week!!'
{name}:'...But you don't go to Magnet?'
DIRK: 'Ok maybe I just wanna see the cool costumes. Come on lets go!'\n""")

print("The two of you walk back to Magnet. Well that's an understatement. More so, Dirk was nearly running while dragging you along. You love the guy but you don't really understand the excitement. It's probably gonna be half done costumes to get a meager point.\n")
time.sleep(15)
print("""DIRK: 'Yo look that kid's dressed like OgreMan...you think if I paid him $20 he'd sing 'All Star' for me?'
You can't help but laugh at the idea. You joke that Dirk isn't 'the sharpest tool in the shed' if he thinks he even has enough money for that.\n""")
time.sleep(15)
print("While watching the costumed students you notice one walk up to you. Looking up, you notice a slice of Cuban bread dressed as Roxas. Since the school doesn't allow huge props and it is just a spirit day, he's carrying a keychain version of the keyblade.")
time.sleep(15)
print("???: 'Have either of you seen my keychain? It was a small one that said 'IT WAS ME, DIO!'. I think I lost it this morning.\n")
if inventory['Keychains']==0:
    print(f"""{name}: 'Sorry, I haven't seen it, but maybe it's still outside?'
    ???: Yeah I guess, I'll probably go looking for it later.""")
if inventory['Keychains']>=1:
    print("You suddenly remember the keychain you pocketed in the morning while strolling around campus. Reaching inside your coat pocket, you present the keychain to the bread.\n")
    inventory['Keychains']-=1
    time.sleep(10)
    print(f"""???: 'MY KEYCHAIN! Thank you so much!'
    {name}: 'It's no problem!'\n""")
    print("He was so thankful for you finding his keychain, you gained 1 heart!")
    inventory['Hearts']+=1


print(f"""{name}: 'Oh by the way, love your cosplay!'
???: 'Thanks, took a while to put together. You like KH?'
{name}: 'Yeah! Can't wait to play KH III.'\n""")
time.sleep(10)
print(f"""Dirk coughs to get your attention.
DIRK: 'If you two are done flirting, we need to get some lunch, {name}. We're gonna miss the good fries!!'
{name}: 'Oh right, well it was fun talking to you!'""")
response = input("""???: 'You too...actually would you mind me tagging along?'
A: Don't mind at all!
B: Um sorry but we really need to get going but maybe another time?""")
while response not in ['A', 'a', 'B', 'b']:
    print("You're just going to leave him hanging? Give an answer.")
    response = input()
if response in ['A', 'a']:
    print(f"""{name}: 'Don't mind at all, right Dirk?'
    DIRK: 'Yeah, I guess, but if you steal my fries, you're dead homes.' he jokingly threatens the student
    ???: 'No worries man, won't even think about it. By the way what are your names?'
    DIRK: 'Oh well I'm Dirk and this is {name}!'
    XAVIER: 'Oh well nice to meet y'all. I'm Xavier, by the way.'\n""")
    time.sleep(10)
    print("With that, the three of you head to the cafeteria. You spend the time eating of course and chatting about your interests. You and Dirk recall insanse club stories, such as that time Dirk hurdled over a seated student to get to the stage in time for his cue. You learn more Xavier, such as his love of 80s/90s R&B.\n")
    time.sleep(5)
    print("By spending time with Dirk and Xavier, you gained energy and hearts!\n")
    inventory['Energy']+=15
    inventory['Hearts']+=1
    time.sleep(5)

if response in [ 'B', 'b']:
    print(f"""{name}: Sorry but Dirk is right, we really need to get going. I'll see you around though?
    ???: Oh yeah, see you around I guess! My name's Xavier by the way.\n""")
    time.sleep(10)
    print("And with that, you and Dirk head to the cafeteria. You both get burgers and fries with you getting yourself a mango icecream pop. You decide to keep it for later. Hopefully it won't melt.\n")
    inventory['Mango Ice cream']+=1
    time.sleep(5)

print("It's finally the end of the school day and you are dead tired. You and Dirk walk together to the buses, chatting about your day and week plans.\n")
time.sleep(5)
print(f"""DIRK: 'Yeah, so we basically ended up watching a bootleg of the musical during my dance class because the teacher was out.'
{name}: 'Wait, Mrs. Corn let you watch it through class?? Doesn't she have that app that lets her watch your computer?'
DIRK: 'Nah, she's pretty chill. Ms. Sourdough however, well they don't call her SOURdough for nothing.'
{name}: 'Yeah you'd still be getting yelled at right now if it was her subbing your class.' you say, laughing.\n""")
time.sleep(10)

print("You and Dirk part ways and get on your respective buses. You get yourself as comfortable as possible and pull out your earbuds.")
music = input("""What are you listening to?
A: Classic Show tunes
B: Decades playlist: Hits of the 70s through 90s
C: Modern Pop\n""")
while music not in ['A', 'a', 'B', 'b', 'C', 'c']:
    print("You sit in silence for a bit before realising you didn't select anything to play. Pick a playlist.\n")
    music = input()
if music in ['A', 'a']:
    print("You select an older song, the classic 'Season of Love' from RENT. It's rather cliche but the day has really tired you out and you need something calm to listen to. You begin thinking about Dirk on the way home. You've only got a few days until Prom. If you don't find a date soon, you and Dirk might just end up going together...That isn't to say it's a bad thing, in fact thats great!! But you know how he is, the poor boy's too for that shy.\n")
    time.sleep(5)
if music in ['B', 'b']:
    print("You decide to play a song from your decades playlist. Playing 'Wheel in the Sky' by Journey, you rest your head against the window. While listening to the song you can't seem to get your mind off of Xavier. He's pretty cool and you seriosuly admired his cosplay during your lunch period.")
    time.sleep(5)
    print("Thinking about the Cuban bread teen nearly makes you miss your stop. You hurry off your bus and make your way home.\n")
    time.sleep(5)
if music in ['C', 'c']:
    print("You decide to tune in to a local radio station as you don't feel like making any more choices than you already have. The station plays pop music and beings playing some new Beer Bread Boyz song. As the song plays you can't help but think of that Naomi girl. You shared such a small interaction but you can't seem to get the sight of her in her suit out of your head.\n")
    time.sleep(5)
    print("You were so distracted by the thought of Naomi you nearly miss your stop. You hop off and make your way home.\n")
    time.sleep(5)

c = input("Check out your inventory by pressing 'i'!\n")
if c == "i":
    print_inventory()

info = input("Check out the bread you met today by pressing 'b'!\n")
if info == "b":
    Naomi.describe()
    Xavier.describe()
time.sleep(3)


