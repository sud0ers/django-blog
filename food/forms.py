from django.forms import ModelForm
from .models import Item

class Itemform(ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']
        labels = {
            'item_name': ('Item Name'),
            'item_desc': ('Item Desc'),
            'item_price': ('Item Price'),
            'item_image': ('Item Image'),
        }