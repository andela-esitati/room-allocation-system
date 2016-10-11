from people.model import Staff, Fellow


class Room(object):
    '''This class models a room in amity'''

    def __init__(self, name):
        self.name = name
        self.occupants = []

    # get the occupants for a room
    def get_occupants(self):
        return self.occupants


class Office(Room):
    '''This class contains info about an office'''
    capacity = 6
    room_type = 'Office'

    # check whether a room is full
    def is_full(self):
        return len(self.occupants) == self.capacity

    def assign_person(self, person):
        if self.capacity > len(self.occupants):
            # check that the argument passed is an object of Staff or Fellow
            if isinstance(person, Staff) or isinstance(person, Fellow):
                self.occupants.append(person)
        return self.occupants

