from datetime import timezone
from django.db import models
from django.db.models.fields import DateTimeField
from django.utils import timezone

# Create your models here.
EXPENSE_TYPE_CHOICES = (
    ('cost of goods sold', 'COGS'),
    ('amortization', 'AMOR'),
    ('selling, general, and admin', 'SG&A'),
    ('salary', 'SALARY'),
    ('rent', 'RENT'),
)

class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0, unique=False)
    inventory = models.IntegerField(default=0, unique=False)
    media_width_inches = models.IntegerField(default=0, unique=False)
    media_height_inches = models.IntegerField(default=0, unique=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    order_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=1000, default='')
    is_cancelled = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    height_inches = models.IntegerField(default=0, unique=False)
    width_inches = models.IntegerField(default=0, unique=False)
    quantity = models.IntegerField(default=0, unique=False)
    initial_payment = models.IntegerField(default=0, unique=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.customer)

class Expense(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, default='')
    type = models.CharField(max_length=200, choices=EXPENSE_TYPE_CHOICES, default='selling, general, and admin')
    cost = models.IntegerField(default=0, unique=False)
    expense_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name