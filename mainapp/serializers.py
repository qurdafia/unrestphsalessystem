from django.db.models import fields
from mainapp.models import Customer, Item, Order, Expense
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'price', 'inventory', 'media_width_inches', 'media_height_inches']
    
class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'mobile_number', 'email']

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['customer', 'item', 'order_date', 'description', 'is_cancelled', 'is_delivered', 'is_paid', 'height_inches', 'width_inches', 'quantity', 'initial_payment']

class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Expense
        fields = ['name', 'description', 'type', 'cost', 'expense_date']