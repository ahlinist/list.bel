from .person import Person

class Recipient(Person):
  def __init__(self, id, name, description):
    self.id = id
    self.name = name
    self.description = description

