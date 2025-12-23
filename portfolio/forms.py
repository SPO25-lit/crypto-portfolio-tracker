from django import forms
from .models import CryptoAsset

class CryptoAssetForm(forms.ModelForm):
    class Meta:
        model = CryptoAsset
        fields = [
            'coin_symbol', 
            'coin_name', 
            'amount', 
            'purchase_price', 
            'exchange', 
            'notes',
            'image'  # НОВОЕ ПОЛЕ
        ]