from django.db import models
from django.contrib.auth.models import User

class Exchange(models.Model):
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=255, blank=True)
    secret_key = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.name

class CryptoAsset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coin_symbol = models.CharField(max_length=10)
    coin_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    purchase_price = models.DecimalField(max_digits=20, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)
    exchange = models.ForeignKey(Exchange, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(blank=True)
    
    # НОВОЕ ПОЛЕ ДЛЯ КАРТИНКИ
    image = models.ImageField(
        upload_to='crypto_images/',
        blank=True,
        null=True,
        verbose_name="Изображение"
    )
    
    class Meta:
        ordering = ['-purchase_date']
    
    def __str__(self):
        return f"{self.coin_symbol} - {self.amount}"

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('BUY', 'Покупка'),
        ('SELL', 'Продажа'),
        ('TRANSFER', 'Перевод'),
    ]
    
    asset = models.ForeignKey(CryptoAsset, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    fee = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)