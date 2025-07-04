"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
        
            }]
        [{
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            }]
        [{
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }]
        

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        if not member.get("id"):
            member["id"] = self.generateId()
        self._members.append(member)
        print("Añadir miembro de la familia", member)
        # You have to implement this method Si no tiene id, créaselo
        # Append the member to the list of _members
        pass

    def delete_member(self, id):
        print(id)
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True
            # si no existe el miembro, que nos devuelva un false:
            return False
        # You have to implement this method
        # Loop the list and delete the member with the given id
        pass

    def update_member(self, id, member):
        print("Actualizando", id)
        for family_member in self._members:
            if family_member["id"] == id:
                self._members.remove(family_member)
                # Para actualizar, he querido hacer que se borre el miembro x y se vuelva a crear.
                member["id"] = id
                self.member.append(member)
                return True
        return False

    def get_member(self, id):
        for family_member in self._members:
            if family_member["id"] == id:
                return family_member

            return False
        # You have to implement this method
        # Loop all the members and return the one with the given id
        pass

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
