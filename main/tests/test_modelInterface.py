from django.test import TestCase
from .. import modelInterface as mI
from ..models import *

# Test the various model API for acquiring room data
class RoomReadTest(TestCase):
    def setUp(self):
        Room.objects.create(id = 1,number='TEST' + '1', description='Test description', floor=10,
                            image='room_images/Draco.png', size=10, price=10, availability=True, type='Studio',
                            visitCount = 1)
        Room.objects.create(id = 2,number='TEST' + '2', description='Test description', floor=11,
                            image='room_images/Draco.png', size=15, price=100, availability=False, type='Studio',
                            visitCount = 2)
        Room.objects.create(id = 3,number='TEST' + '3', description='Test description', floor=12,
                            image='room_images/Draco.png', size=20, price=1000, availability=True, type='Studio',
                            visitCount = 3)
        Room.objects.create(id = 4,number='TEST' + '4', description='Test description', floor=13,
                            image='room_images/Draco.png', size=25, price=10000, availability=False, type='Studio',
                            visitCount = 4)
        Room.objects.create(id = 5,number='TEST' + '5', description='Test description', floor=14,
                            image='room_images/Draco.png', size=30, price=20000, availability=True, type='Single',
                            visitCount = 5)
        Room.objects.create(id = 6,number='TEST' + '6', description='Test description', floor=15,
                            image='room_images/Draco.png', size=35, price=30000, availability=False, type='Single',
                            visitCount = 6)
    
    # Make sure the first index is the room with the highest visitCount
    def test_getFeaturedRooms(self):
        featuredRooms = mI.getFeaturedRooms(8)
        self.assertEqual(featuredRooms.get('studio',None)[0].visitCount, 4)
        self.assertEqual(featuredRooms.get('single',None)[0].visitCount, 6)

    def test_getRooms(self):
        pass

    def test_getRoom(self):
        self.assertEqual(mI.getRoom(id = 3).number, 'TEST3')
        self.assertEqual(mI.getRoom(id = 3).size, 20)
        
    