
class Person(object):
    '''this class models a person'''

    def __int__(self, name):
        self.name = name

    @staticmethod
    def create(name, role, wants_accomodation=False):
        '''create a fellow or staff object'''
        andelan = Role.category[role.lower()]
        # create object called person
        person = andelan()
        person.name = name
        # all people have offices
        person.office = None
        # condition for if person is an object of class Staff
        if isinstance(person, Staff):
            person.wants_accomodation = False
        # condition for if person is an object of class Fellow
        if isinstance(person, Fellow):
            # incase fellow wants accomodation
            if wants_accomodation == 'Y' or wants_accomodation is 'True':
                person.wants_accomodation = True
            # incase  fellow does not want accomodation
            else:
                person.wants_accomodation = False
            # fellow has a living space
            person.living_space = None
        return person

    def has_office(self):
        '''check if person has been assigned an office'''
        return True if self.office is not None else False

    def allocate_office_space(self, office):
        '''allocate a person to an office space'''
        self.office = office
        return self.office

class Staff(Person):
    '''This class models a staff'''
    # a staff cannot have living space
    def has_living_space(self):
        return False

class Fellow(Person):
    '''This class models a fellow'''

    living_space = None

    def wants_living_space(self):
        '''inquire if the fellow wants living space'''
        return True if self.wants_accomodation else False

    def assign_living_space(self,room):
        '''assigns living space room to fellow'''
        self.living_space = room
        return self.living_space

    def has_living_space(self):
        '''check if fellow has living space'''
        return True if self.wants_accomodation is True else False
from model import Fellow,Staff


class Role:
    '''this class contains the role of a person ie 
    either a fellow or a staff'''
    category = {'fellow': Fellow, 'staff': Staff}


# writing stuff just to test out