from rest_framework import serializers
from .models import Drones

# fields on api input page
class PostSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id', 
			'author', 
			'model', 
			'megapixel', 
			'brand',
			'serialno',
			'supported_cameras',
			'created_at',
			)
		model = Drones
