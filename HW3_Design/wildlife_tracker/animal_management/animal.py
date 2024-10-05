class Animal:
    def __init__(self, animal_id: int, species: str, age: int, health_status: str):
        self.animal_id = animal_id
        self.species = species
        self.age = age
        self.health_status = health_status

    def update_health(self, new_status: str):
        self.health_status = new_status
