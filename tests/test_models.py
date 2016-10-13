import unittest
from people.model import Person, Fellow, Staff
from rooms.model import LivingSpace, Office


class ModelTests(unittest.TestCase):

    def setUp(self):
        self.fellow = Person.create(
            'Elsis Sitati', 'fellow', wants_accomodation=True)
        self.staff = Person.create('Percila Njira', 'staff')
        self.office = Office('Hogwarts')
        self.living_space = LivingSpace('Haskel')

    def test_person_creation(self):
        self.assertIsInstance(self.fellow, Fellow)
        self.assertEqual(self.fellow.name, 'Elsis Sitati')
        self.assertIsInstance(self.staff, Staff)

    def test_room_creation(self):
        """ generate rooms and test their specs """
        full_office = self.office.capacity
        full_dorm = self.living_space.capacity
        self.assertEquals(full_office, 6)
        self.assertEquals(full_dorm, 4)
        self.assertIsInstance(self.office, Office)
        self.assertIsInstance(self.living_space, LivingSpace)

    
