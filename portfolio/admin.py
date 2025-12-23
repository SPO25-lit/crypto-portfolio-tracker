from django.contrib import admin
from .models import Exchange, CryptoAsset, Transaction

@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(CryptoAsset)
class CryptoAssetAdmin(admin.ModelAdmin):
    list_display = ['coin_symbol', 'coin_name', 'amount', 'purchase_price', 'purchase_date']
    list_filter = ['coin_symbol', 'purchase_date']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['asset', 'transaction_type', 'amount', 'price', 'date']
    list_filter = ['transaction_type', 'date']