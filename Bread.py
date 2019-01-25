import time#allows programmer to use "time.sleep()"
print("All You Knead is Love: A Bread Dating Simulator\n")
name = input("Enter your name!\n")

A = input("Great are you bready to get this bread! Y/N\n")
while A not in ['yes', 'y', 'Y', 'Yes']: #player must select option to move forward
  print(f"You're not allowed to say no, {name}")
  A = input()
print("Let's getis this breadis...\n")

def print_inventory():#function for printing the dictionary "inventory"
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

i = input("Check out your inventory by pressing 'i'!")
if i == "i":
    print_inventory()


class character:#class for defining the characters
  def __init__(self, name, year, school, bread, funfacts, alignment):
    self.name = name
    self.year = year
    self.school = school
    self.bread = bread
    self.funfacts = funfacts
    self.alignment = alignment
  def describe(self):#function to describe any one character
    print(f"""{self.name}:
    - Year: {self.year}
    - School: {self.school}
    - Bread Type: {self.bread}
    - Fun Facts!: {self.funfacts}
    - Alignment: {self.alignment}""")
    return

Dirk = character('Dirk', 11, 'APA', 'Whole grain', 'loves singing, dancing, watching horror movies with some hot cocoa, hanging out with friends by the lake', 'Looks like a cinnamon roll and is one, lawful good')
Xavier = character('Xavier', 12,'MHS', 'Cuban', 'loves videogames and cosplay, 80s and 90s hip hop, had his first kiss to Kung Fu Fighting', 'Looks like a cinnamon roll but could kill you, chaotic good')
Naomi = character('Naomi', 11, 'AIT', 'Naan', 'loves coding, looks darn good in suits, grew up on Studio Ghibli, will love you forever if you get her mango icecream', 'Looks like she could kill you, is actually a cinnamon roll, neutral good')
#Character descriptions, variables for the character class

print(".....This is just a demo version! You'll only be meeting 3 out of the 5 available love interests and playing through 3 days! Have fun <3..........")
time.sleep(10)
print(f"""Ah UCVTS. An ordinary campus like any other, save for its vocational classes and it being one of the highest ranked schools in bread education.
That's right.
Bread education.
You see, in decades past, a new string of the flu virus was discovered and it for some reason, caused a mutation in bread. This mutation caused them to gain human like features, incuding a functioning brain. Your campus has been one of the few and most notable to accept these bread people into their school. You, dear {name}, have never known a world without these people, especially your best friend Dirk, a whole wheat bread slice.\n""")
time.sleep(10)#time.sleep(__) creates a pause of any length in seconds
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
    inventory['Hearts']-=1 #changes values of an item in the defined dictionary "inventory"
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
    print("Scrolling through, you get a notification that someone's requested to follow you. Opening it you see a teenage bread, cosplaying a character from your favourite video game. It's famous picturegrammer '@CrumbyCosplay'! You're immediately enamoured and follow back. You spend a few minutes scrolling through their blog admiring their craftsmanship and dedication to the hobby.\n")
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

i = input("Check out your inventory by pressing 'i'!\n")
if i == "i":
    print_inventory()

info = input("Check out the bread you met today by pressing 'b'!\n")
if info == "b":
    Naomi.describe()
    Xavier.describe()
time.sleep(3)

print("WEDNESDAY, DAY 3...\n")
time.sleep(3)
print("AH AH AH AH AH AH")
time.sleep(3)
print("Your alarm blares in your ears as you struggle to shut it off. You slam your hand into the snooze button and push yourself off the bed. You notice, for once, that you've woken up on time, 6:00am. You decide this calls for something, a treat perhaps. Making your way to the kitchen you prep yourself breakfast.")
time.sleep(10)
breakfast = input("""What will you have?:
    A: Oatmeal and fruit
    B: an Omelette
    C: Beans and toast\n""")
while breakfast not in ['A', 'a', 'B', 'b', 'C', 'c']:
    print("You stare at the fridge. Looking at the time, you realise you have about 55 minutes to eat. Please make something.\n")
    breakfast = input()
if breakfast in ['A', 'a']:
    print("You make a healthy meal of sweet oatmeal and fruit. The meal was so filling and energising you gained a heart and 20 energy!\n")
    inventory['Hearts']+=1
    inventory['Energy']+=20
    time.sleep(5)
if breakfast in ['B', 'b']:
    print("As you munch down on your omelette you notice something awful. The eggs are rotten and thus you spit it out. You lose 3 hearts because of the life threatening experience.\n")
    inventory['Hearts']-=3
    time.sleep(5)
if breakfast in ['C', 'c']:
    print("You stoop so low as to eat beans and toast like a monster. The beans themself aren't so bad and for that, you gain 10 energy. However, partaking in such a horrific act as eating bread makes you lose 5 hearts.\n")
    inventory['Hearts']-=5
    inventory['Energy']+=10
    time.sleep(5)

item = input("""After the enjoyment, or lack there of, of breakfast, you return to your room at about 6:40am to prep your bag before leaving. The essentials are packed, your binders, laptop, pens and all. But, there's something missing, essential or not. What do you add to your bag?:
    A: Hot cocoa
    B: Reading Material
    C: Joker Keychain
    D: Ice Cream\n""")
while item not in ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd']:
    print("Little boring not to take something extra, don't you think?\n")
    item = input()
if item in ['A', 'a']:
    print("You quickly make a thermos of hot cocoa and place it in the side pocket of your book bag.\n")
    inventory['Hot cocoa']+=1
    time.sleep(5)
if item in ['B', 'b']:
    print("You pick up a magazine from the kitchen counter, finding the cover intriguing. Something to keep your mind working on the ride to school.\n")
    inventory['Magazines']+=1
    time.sleep(5)
if item in ['C', 'c']:
    print("You clip your Joker keychain to the back of your bag, god you couldn't wait to main him when smash ultimate comes out.\n")
    inventory['Keychains']+=1
    time.sleep(5)
if item in ['D', 'd']:
    print("Looking outside, you just now notice the blasing sun. It's only 6:40 but it looks like it'll be a sweltering day. You take an ice cream to cool you down before school.\n")
    inventory['Mango Ice cream']+=1
    time.sleep(5)

print("After completing your tasks for the morning, you head out the door ready to take on the day.\n")
print("....................................(ᴗ ͜ʖ ᴗ)travelling(ᴗ ͜ʖ ᴗ)......................................................")
time.sleep(5)

print(f"""You arrive at school and remember your interactiong with Naomi yesterday. She had dropped her ID and you still have it on you. Pulling it, you head over to the AIT main office to put it in the lost and found.
DIRK: Hey {name}! What's up!
{name}: Oh, hey Dirk! Just got here. Actually heading to AIT rn.
DIRK: Oh why?
{name}: I bumped into someone yesterday and she dropped her ID. I'm just going to return to the school.
DIRK: Ah gotcha. I'll tag along.\n""")
time.sleep(10)

print(f"""MS. WHITE: Hi how may I help you?
{name}: Well you see one of the students dropped her ID and I just wanted to return it?
MS. WHITE: No problem, just leave it here and I'll call her down to-\n""")
time.sleep(10)
print(f"""Before the woman behind the desk could finish her sentence, the bread in question comes bustling in, once again wearing a suit. Her hair's a little unkempt and she seems slightly panicked.
NAOMI: EXCUSE ME I LOST MY ID IM SORRY BUT I WAS IN A RUSH AND MY ID I JU-
{name}: Naomi is it? I think I have what you're looking for. """)
time.sleep(10)
print(f"""You present her with the ID, a little scratched from the fall. Her name, SINGH, NAOMI, clear as day.
NAOMI: YOU'RE A LIFE SAVER THANK YOU GOD I CAN'T SERVER ANOTHER LOP
{name}: It's no problem, I notice you dropped it and was actually here to return it-
Naomi cuts you off with a bear hug. She's got a pretty strong grip for being so lanky.""")
inventory['Journals']-=1
time.sleep(10)

print("You notice both her worry and relief. You think, maybe she need's something to cheer her up.")
gift = input("Would you like to offer her ice cream? Y/N\n")
while gift not in ['Y', 'y', 'N', 'n']:
    print("Please give some sort of answer\n")
    gift = input()

if gift in ['Y', 'y']:
    if inventory['Mango Ice cream']==0:
        print("Ha even if you wanted to, you have absolutely nothing to offer that she'd like. B I G S A D : (")
    if inventory['Mango Ice cream']>=1:
        print("You remember suddenly, that you have some mango ice cream on you. Luckily, you have one of those freezer lunchbags so it was still frozen. You pull it out and offer it to Naomi.\n")
        print(f"""NAOMI: Yo wait is that Friendly's brand Mango Ice cream! Can I have some??
        {name}: Of course!""")
        inventory['Hearts']+=5

if gift in ['N', 'n']:
    print("You don't offer the ice cream because you're a selfish little goblin. You lose 3 hearts.\n")
    inventory['Hearts']-=3

time.sleep(10)
print("Your day was not as quite eventful as you had hope'd it would be but c'est la vie. You hung out with Dirk, Xavier, and Naomi during lunch. You learned alot about her including her love of ghibli movies, her favourite she says is Grave of the Firelies. She's hoping to go into computer programming in her college years and maye create her own horror novel game!")
time.sleep(6)

print("It's the end of the final period and you're itching to confront you-know-who. As the final bell rings, you blast out of your classroom, bidding your Literature teacher a quick goodbye.\n")
time.sleep(5)
print("You arrive at the bussing lanes, searching through the crowd for that special someone. But before you find them, let's review your stats.\n")

i = input("Check out your inventory by pressing 'i'!\n")
if i == "i":
    print_inventory()
date = input("""If you remember well, most items correlate to one of the breads you've met along your journey! The hearts as well, some breads have level of affection that needed to be met. Choose wisely, they will be your prom date for better or worse.
A: DIRK
B: NAOMI
C: XAVIER
""")
while date not in ['A', 'a', 'B', 'b', 'C', 'c',]:
    print("You must pick someone to take, this is a D A T I N G S I M U L A T O R .\n")
    date = input()
if date in ['A', 'a']:
    if inventory['Hot cocoa']>=2:
        print("You decide to ask out Dirk. Nervous, you walk over to him. He seems rather stunned at first, a blush rising to his bready complexion. He happily accepts and you two plan your night together.\n")
        time.sleep(5)
        print("CONGRATS YOU GOT THE GOOD ENDING! YOU AND DIRK HAD A GREAT TIME AT PROM")
    if inventory['Hot cocoa']<=2:
        print("You decide to ask out Dirk. Nervous, you walk over to him. Unfortunately, he rejects you. He says he sees you two as simply friends and would like to keep it that way.")
        time.sleep(10)
        print("BAD ENDING...wonder where you went wrong?")
if date in ['B', 'b']:
    if inventory['Mango Ice cream']>=1:
        print("You decide to ask out Naomi. Nervous, you walk over to her. She starts blushing and stuttering, breadcrumbs falling from her lips. She mutters out an embarrased but happy yes. Ecstatic, you two decide to wak home together, planning for Saturday ")
        time.sleep(10)
        print("CONGRATS YOU GOT THE GOOD ENDING! YOU AND NAOMI HAD A GREAT TIME AT PROM")
    if inventory['Mango Ice cream']<=1:
        print("You decide to ask out Naomi. Nervous, you walk over to her. Unfortunately, she rejects you. She says she sees you two as simply friends and would like to keep it that way. She thinks you're taking things too fast :("")
        time.sleep(10)
        ("BAD ENDING...wonder where you went wrong?")
if date in ['C', 'c']:
    if inventory['Hearts']>=18:
        print("You decide to ask out Xavier. Nervous, you walk over to him. He's shocked but happily accepts the invite. He seems almost more excited than you are it's entertaining to say the least. None the less, you're relieved he accepted the invitation.")
        time.sleep(10)
        print("CONGRATS YOU GOT THE GOOD ENDING! YOU AND XAVIER HAD A GREAT TIME AT PROM")
    if inventory['Hearts']<=18:
        print("You decide to ask out Xavier. Nervous, you walk over to him. He sadly smiles and tells you sorry but he only sees you as a friend and would like to keep it that way. He finds you too clingy :(")
        time.sleep(10)
        ("BAD ENDING...wonder where you went wrong?")












\








