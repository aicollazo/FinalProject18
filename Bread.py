print("All You Knead is Love: A Bread Dating Simulator\n")
name = input("Enter your name!\n")

A = input("Great are you ready to get this bread! Y/N\n")
while A not in ['yes', 'y', 'Y', 'Yes']:
  print(f"You're not allowed to say no, {name}")
  A = input()
print("Let's getis this breadis...\n")

class character:
  def __init__(self, name, year, school, bread, interests):
    self.name = name
    self.year = year
    self.school = school
    self.bread = bread
    self.interests = interests
  def describe(self):
    print(f"""{self.name}:
    - Year: {self.year}
    - School: {self.school}
    - Bread Type: {self.bread}
    - Interests: {self.interests}""")
    return
Dirk = character('Dirk', 11, 'APA', 'Whole grain', 'Singing, dancing, watching horror movies with some hot cocoa, hanging out with friends by the lake')
JC = character('JC', 12, 'UCT','Croissant')
Mariah = character('Mariah', 12,'AAHS', 'Baguette')
Mikey = character('Mikey', 12,'MHS', 'Cuban', '')
Naomi = character('Naomi', 11, 'AIT', 'Naan', '')


Dirk.describe()
JC.describe()
Mariah.describe()
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