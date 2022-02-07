# not running properly yet...
from django.test import TestCase

"""
from django.contrib.auth.models import User
from .models import Drones

class DronesTests(TestCase):
	@classmethod
	def setUpTestData(cls):
		# Create a user
		testuser1 = User.objects.create_user(username='testuser1', password='abc123')
		testuser1.save()
		# Create a drone entry
		test_drones = Drones.objects.create(
			author=testuser1, 
			model='Model type', 
			megapixel=int(12), 
			brand='brandtype',
			serialno='1234abcd',
			supported_cameras='Random Camera')
			
		test_drones.save()

	def test_drones_inventory(self):
		drone = Drones.objects.get(id=1)
		author = f'{drone.author}'
		model = f'{drone.model}'
		megapixel = f'{drone.megapixel}'
		brand = f'{drone.brand}'
		serialno = f'{drone.serialno}'
		supported_cameras = f'{drone.supported_cameras}'
		self.assertEqual(author, 'testuser1')
		self.assertEqual(model, 'Model type')
		self.assertEqual(megapixel, int(12)
		self.assertEqual(brand, 'brandtype')
		self.assertEqual(serialno, '1234abcd')
		self.assertEqual(supported_cameras, 'Random Camera')

"""