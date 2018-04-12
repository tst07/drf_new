from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Bank, Branch, Accounts, BanksInfo, Customer


class BanksInfoSerializer(serializers.HyperlinkedModelSerializer):
	bank = serializers.ReadOnlyField(source='bank.name')
	customer = serializers.ReadOnlyField(source='customer.name')

	class Meta:
		model = BanksInfo
		fields = ('bank', 'customer', 'first_arrived', 'last_arrived', 'total_balance',)	

class AccountsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Accounts
		fields = ('account_number', 'account_name', 'description', 'created_at', 'updated_at', )


class BranchSerializer(serializers.HyperlinkedModelSerializer):
	bank = serializers.ReadOnlyField(source='bank.name')
	accounts_set = AccountsSerializer(read_only=True, many = True)

	class Meta:
		model = Branch
		fields = ('address', 'is_active', 'created_at', 'updated_at', 'bank', 'accounts_set',)


class BankSerializer(serializers.HyperlinkedModelSerializer):
	# branch_set = BranchSerializer(read_only=True, many = True)
	customer_set = BanksInfoSerializer(source='banksinfo_set', many=True)
	branch_set = serializers.HyperlinkedRelatedField(many=True, view_name='branches', read_only=True)

	class Meta:
		model = Bank
		fields = ('name', 'owner', 'created_at', 'updated_at', 'branch_set', 'customer_set', )


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
	banks = BanksInfoSerializer(source='banksinfo_set', many = True)

	class Meta:
		model = Customer
		fields = ('name', 'address', 'banks',)
