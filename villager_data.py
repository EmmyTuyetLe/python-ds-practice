"""Functions to parse a file containing villager data."""


def all_species(filename):
  """Return a set of unique species in the given file.
  
    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings"""
  species = set() #return set
  data = open("villagers.csv") #access data from file
  for line in data: 
    stats = line.split("|")
    species.add(stats[1])

    # TODO: replace this with your code

  return species

#print(all_species("villagers.csv"))

def get_villagers_by_species(filename, species="All"):
    """Return a list of villagers' names by species.
s
    Arguments:
      - filename (str): the path to a data file
      - species (str): optional, the name of a species

    Return:
      - list[list]: a list of lists
    """

    villagers = []
    data = open(filename) #access data from filess
    for line in data: 
      stats = line.split("|")
      
      if species == "All":
        villagers.append(stats[0])
        continue
        
      if stats[1] == species:
        villagers.append(stats[0])
    # TODO: replace this with your code

    return sorted(villagers)

#print(get_villagers_by_species("villagers.csv", "All"))

def all_names_by_hobby(filename):
    """Return a list that villagers' names, grouped by hobby.

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """
    hobbies = [[], [], [], [], [], []]
  # fitness = []
  # nature = []
  # education = []
  # music = []
  # fashion = []
  # play = []

    data = open(filename)
    for line in data:
      stats = line.split("|")
      if stats[3] == "Fitness":
        hobbies[0].append(stats[0])
      elif stats[3] == "Nature":
        hobbies[1].append(stats[0])
      elif stats[3] == "Education":
        hobbies[2].append(stats[0])
      elif stats[3] == "Music":
        hobbies[3].append(stats[0])
      elif stats[3] == "Fashion":
        hobbies[4].append(stats[0])
      elif stats[3] == "Play":
        hobbies[5].append(stats[0])
      
    for i in range(6):
      hobbies[i].sort()

      # TODO: replace this with your code

      return hobbies

# result = all_names_by_hobby("villagers.csv")
# for j, item in enumerate(["fitness", "nature","education", "music","fashion" ,"play"]): #iterates through index and item
#   print(item, result[j])


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    data = open(filename)
    for line in data:
      line = tuple(line.strip().split("|"))
      all_data.append(line)
    return all_data

#print(all_data("villagers.csv"))

def find_motto(filename, name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    # TODO: replace this with your code

    data = open(filename)
    for line in data:
      stats = line.split("|")
      if stats[0] == name:
        return stats[4]
    return
      
#print(find_motto("villagers.csv", "sdfsdfsdfs"))

def find_likeminded_villagers(filename, name):
    """Return a set of villagers with the same personality as the given villager."""

    data = open(filename)
    lines = []
    personality = ""
    likeminded_villagers = set()
    for line in data:
      line = line.split("|")
      lines.append(line)
      if line[0] == name:
        personality = line[2]
        _ = line[0]
    print(_)
    for line in lines:
      if line[2] == personality:
        likeminded_villagers.add(line[0])

    return likeminded_villagers

print(find_likeminded_villagers("villagers.csv", "Teddy"))