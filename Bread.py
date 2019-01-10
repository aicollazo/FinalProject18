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
    'Mango Ice cream': 0
    }
c = input("Check out your inventory by pressing 'i'!")
if c == "i":
    print_inventory()

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
Mikey = character('Mikey', 12,'MHS', 'Cuban', 'loves videogames and cosplay, 80s and 90s hip hop, had his first kiss to sir-mix-alots Baby Got Back', 'Looks like a cinnamon roll but could kill you, chaotic good')
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

print(f"Anyways, I really could use your help! I need to memorise my lines but I have no




