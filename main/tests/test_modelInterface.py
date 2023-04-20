from django.test import TestCase
from .. import modelInterface as mI
from ..models import *

# Test the various model API for acquiring room data
class RoomQueryTest(TestCase):
    def setUp(self):
        Room.objects.create(id = 1,number='TEST' + '1', description='Test description 1', floor=10,
                            image='room_images/Draco.png', size=10, price=10, availability=True, type='Studio',
                            visitCount = 1)
        Room.objects.create(id = 2,number='TEST' + '2', description='Test description 2', floor=11,
                            image='room_images/Draco.png', size=15, price=100, availability=False, type='Studio',
                            visitCount = 2)
        Room.objects.create(id = 3,number='TEST' + '3', description='Test description 3', floor=12,
                            image='room_images/Draco.png', size=20, price=1000, availability=True, type='Studio',
                            visitCount = 3)
        Room.objects.create(id = 4,number='TEST' + '4', description='Test description 4', floor=13,
                            image='room_images/Draco.png', size=25, price=10000, availability=False, type='Studio',
                            visitCount = 4)
        Room.objects.create(id = 5,number='TEST' + '5', description='Test description 5', floor=14,
                            image='room_images/Draco.png', size=30, price=20000, availability=True, type='Single',
                            visitCount = 5)
        Room.objects.create(id = 6,number='TEST' + '6', description='Test description 6', floor=15,
                            image='room_images/Draco.png', size=35, price=30000, availability=False, type='Single',
                            visitCount = 6)
    
    # Make sure the first index is the room with the highest visitCount
    def test_getFeaturedRooms(self):
        featuredRooms = mI.getFeaturedRooms(8)
        self.assertEqual(featuredRooms.get('studio',None)[0].visitCount, 4)
        self.assertEqual(featuredRooms.get('single',None)[0].visitCount, 6)

    # Test the query processing system
    def test_getRooms_by_type(self):
        testStudio = Room(id = 1,number='TEST' + '1', description='Test description', floor=10,
                            image='room_images/Draco.png', size=10, price=10, availability=True, type='Studio',
                            visitCount = 1)
        testSingle = Room(id = 6,number='TEST' + '6', description='Test description', floor=15,
                            image='room_images/Draco.png', size=35, price=30000, availability=False, type='Single',
                            visitCount = 6)

        queryData = {'query': 'Studio', 'queryType': 'type', 'priceMin': 0, 'priceMax': 0, 'orderField': 'id', 'orderDirection': True}
        rooms = mI.getRooms(queryData)
        self.assertNotIn(testSingle, rooms)
        self.assertIn(testStudio, rooms)

        queryData = {'query': 'Single', 'queryType': 'type', 'priceMin': 0, 'priceMax': 0, 'orderField': 'id', 'orderDirection': True}
        rooms = mI.getRooms(queryData)
        self.assertNotIn(testStudio, rooms)
        self.assertIn(testSingle, rooms)


    def test_getRooms_by_description(self):
        queryData = {'query': 'Test', 'queryType': 'description', 'priceMin': 0, 'priceMax': 0, 'orderField': 'id', 'orderDirection': True}
        rooms = mI.getRooms(queryData)
        self.assertEqual(len(rooms), 6)


        queryData = {'query': 'Test description 6', 'queryType': 'description', 'priceMin': 0, 'priceMax': 0, 'orderField': 'id', 'orderDirection': True}
        rooms = mI.getRooms(queryData)
        self.assertEqual(len(rooms), 1)
        self.assertEqual(rooms[0].id, 6)

    def test_getRooms_by_number(self):
        queryData = {'query': 'TEST1', 'queryType': 'number', 'priceMin': 0, 'priceMax': 0, 'orderField': 'id', 'orderDirection': True}
        rooms = mI.getRooms(queryData)
        self.assertEqual(len(rooms), 1)
        self.assertEqual(rooms[0].id, 1)

    def test_getRooms_by_price_range(self):
        queryData = {'query': '', 'queryType': 'type', 'priceMin': 0, 'priceMax': 0, 'orderField': 'id', 'orderDirection': True}
        rooms = mI.getRooms(queryData)
        self.assertEqual(len(rooms), 6)
        # self.assertEqual(rooms[0].type, 'Double')
        # self.assertEqual(rooms[1].type, 'Suite')

    def test_getRooms_by_order_field(self):
        # orderDirection = False for Descending
        queryData = {'query': '', 'queryType': 'type', 'priceMin': 0, 'priceMax': 0, 'orderField': 'price', 'orderDirection': False}
        rooms = mI.getRooms(queryData)
        highest1, lowest1 = rooms[0], rooms[len(rooms)-1]
        self.assertEqual(len(rooms), 6)
        self.assertGreaterEqual(rooms[0].price, rooms[len(rooms)-1].price)
        
        queryData = {'query': '', 'queryType': 'type', 'priceMin': 0, 'priceMax': 0, 'orderField': 'price', 'orderDirection': True}
        rooms = mI.getRooms(queryData)
        highest2, lowest2 = rooms[len(rooms)-1], rooms[0]
        self.assertEqual(len(rooms), 6)
        self.assertLessEqual(rooms[0].price, rooms[len(rooms)-1].price)

        self.assertEqual(highest1, highest2)
        self.assertEqual(lowest1, lowest2)



    # def test_query_by_order_direction(self):
    #     queryData = {'query': '', 'queryType': 'type', 'priceMin': 0, 'priceMax
    
    def test_getRoom(self):
        self.assertEqual(mI.getRoom(id = 3).number, 'TEST3')
        self.assertEqual(mI.getRoom(id = 3).size, 20)
        
    