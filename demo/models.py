from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Bank(models.Model):
	name = models.CharField(max_length=30)
	owner = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.name


class Customer(models.Model):
	name = models.CharField(max_length=50)
	address = models.TextField(default="", blank = True, null = True)
	banks = models.ManyToManyField(Bank, through='BanksInfo', blank=True)

	def __str__(self):
		return self.name


class BanksInfo(models.Model):
	bank = models.ForeignKey(Bank)
	customer = models.ForeignKey(Customer)

	first_arrived = models.DateTimeField(auto_now=True)
	last_arrived = models.DateTimeField(auto_now_add = True)
	total_balance = models.IntegerField(default=0)

	def __str__(self):
		return str(self.customer.name) + " has account(s) in " + str(self.bank.name)


class Branch(models.Model):
	bank = models.ForeignKey(Bank)
	address = models.TextField(default="", blank = True)
	is_active = models.BooleanField(default = True)
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.bank.name + self.address


class Accounts(models.Model):
	account_number = models.CharField(max_length=40, default="123")
	account_name = models.CharField(max_length=40, null=True, blank = True)
	description = models.TextField(blank=True, null=True)
	branch = models.ForeignKey(Branch)

	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.account_name
