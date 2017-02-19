from people.model import Person, Fellow, Staff
from rooms.model import Office, LivingSpace
import random
import re


class Amity(object):
    '''this is the class that allocates rooms to people randomly'''

    def __init__(self):
        self.allocations = []
        self.unallocated = []

    def add_rooms(self, room_list, room_type):
        '''create office objects and store them in a list'''
        if room_type.lower() == 'office':
            room_list = [Office(room_name) for room_name in room_list]

        elif room_type.lower() == 'living':
            room_list = [LivingSpace(room_name) for room_name in room_list]
        return room_list

    def get_allocations(self):
        return self.allocations

    def print_allocations(self):
        '''print all allocations'''
        for room in self.allocations:
            print '%s %s' % (room.name, room_type)
            for occupant in rooms.occupants:
                print occupant.name
                print '\n'
            return True

    def get_unallocated(self):
    	return self.unallocated

    @sta

