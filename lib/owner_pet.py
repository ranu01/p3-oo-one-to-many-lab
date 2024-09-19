class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if not isinstance(pet_type, str) or pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)  
        if owner:
            owner.add_pet(self)  

    def __repr__(self):
        return f"Pet(name={self.name}, pet_type={self.pet_type})"


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  

    def pets(self):
       
        return self._pets

    def add_pet(self, pet):
       
        if not isinstance(pet, Pet):
            raise Exception("Can only add an instance of Pet")
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        
        return sorted(self._pets, key=lambda pet: pet.name)

    def __repr__(self):
        return f"Owner(name={self.name})"



owner = Owner("John")
pet1 = Pet("Jim Jr.", "dog", owner)
pet2 = Pet("Clifford", "dog", owner)


print(owner.pets())  