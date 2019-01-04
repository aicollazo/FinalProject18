print("All You Knead is Love: A Bread Dating Simulator\n")
name = input("Enter your name!\n")

A = input("Great are you bready to get this bread! Y/N\n")
while A not in ['yes', 'y', 'Y', 'Yes']:
  print(f"You're not allowed to say no, {name}")
  A = input()
print("Let's getis this breadis...\n")

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
JC = character('JC', 12, 'UCT','Croissant', 'loves hanging out at starbucks, best friends witht the duolingo owl, enjoys macchiatos and crunching fallen leaves', 'Looks like a cinnamon roll but could kill you, lawful neutral')
Marie = character('Marie', 12,'AAHS', 'Baguette', 'Super into dermatology, fashion magazines, loves boxing and takes classes at Tiger Bread Schulmann, dog walking', 'Looks like she could kill you, can actually kill you, true neutral ')
Mikey = character('Mikey', 12,'MHS', 'Cuban', 'loves videogames and cosplay, 80s and 90s hip hop, had his first kiss to sir-mix-alots Baby Got Back', 'Looks like a cinnamon roll but could kill you, chaotic good')
Naomi = character('Naomi', 11, 'AIT', 'Naan', 'loves coding, looks darn good in suits, grew up on Studio Ghibli, will love you forever if you get her mango icecream', 'Looks like she could kill you, is actually a cinnamon roll, neutral good')


Dirk.describe()
JC.describe()
Marie.describe()
Mikey.describe()
Naomi.describe()

print(f"Ah UCVTS. An ordinary campus like any other, save for its vocational classes. It has your usual clubs and activities like most school. You, dear {name}, have decided to stay after school to help out at one of these clubs. You're hanging out in the senior lounge of AAHS. \n")

location = input("Where will you go?: Bathroom, auditorium, a classroom\n")
while location not in ['Bathroom', 'auditorium', 'a classroom']:
  print("Please give an answer. Maybe you spelled it wrong?")
  location = input()
if location == 'Bathroom':
  print("You went to the bathroom, it was sooooo eventful")
  location = input("Where will you go?: auditorium, a classroom\n")
  while location not in ['auditorium', 'a classroom']:
    print("Please give an answer. Maybe you spelled it wrong?")
    location = input()
if location == 'a classroom':
  print("You walked into the classroom and got scared by the way too realistic CPR dummies. You bolt out, scared for life.")
  location = input("Where will you go?: auditorium\n")
  while location not in ['auditorium', 'Bathroom']:
    print("Please give an answer. Maybe you spelled it wrong?")
    location = input()
if location == 'auditorium':
  print("You travel downstairs.")