class DictionaryFileManager:
  """
  constructor: Initializes a new instance of the DictionaryFileManager class.
  filename: The name of the file to be used for storing/retrieving dictionary information.
  """
  def __init__(self, filename):
    self.filename = filename

  def write_dictionary_to_file(self, dictionary):
    """
    Writes the given dictionary to the file specified in the constructor.
    parameter: dictionary - The dictionary to be written to the file.
    """
    if dictionary is None or not dictionary:
      return

    with open(self.filename, 'w') as f:
      for key, value in dictionary.items():
        f.write(key + ' ' + str(value) + '\n')

  def read_dictionary_from_file(self):
    """
    Reads the dictionary from the file specified in the constructor. If the file is empty or does not exist, returns an empty dictionary.
    return value: The dictionary read from the file.
    dictionary: The dictionary read from the file.
    """
    try:
      with open(self.filename, 'r') as f:
        dictionary = {}
        for line in f:
          key, value = line.strip().split()
          dictionary[key] = int(value)
        return dictionary
    except FileNotFoundError:
      return {}

manager = DictionaryFileManager('dictionary.txt')
building_numbers = manager.read_dictionary_from_file()

name = input('Enter new name: ')

if name != '':
  building_number = int(input('Enter new building number: '))
  building_numbers[name] = building_number

lookup_name = input('Enter name to look up: ')

if lookup_name in building_numbers:
  print(building_numbers[lookup_name])

manager.write_dictionary_to_file(building_numbers)
