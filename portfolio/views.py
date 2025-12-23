from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CryptoAsset
from .forms import CryptoAssetForm

@login_required
def portfolio_list(request):
    assets = CryptoAsset.objects.filter(user=request.user)
    return render(request, 'portfolio/list.html', {'assets': assets})

@login_required
def add_asset(request):
    if request.method == 'POST':
        form = CryptoAssetForm(request.POST)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.user = request.user
            asset.save()
            return redirect('portfolio_list')
    else:
        form = CryptoAssetForm()
    return render(request, 'portfolio/add_asset.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404  # ← добавь get_object_or_404

@login_required
def edit_asset(request, asset_id):
    # Находим актив текущего пользователя
    asset = get_object_or_404(CryptoAsset, id=asset_id, user=request.user)
    
    if request.method == 'POST':
        # Обновляем существующий актив
        form = CryptoAssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('portfolio_list')
    else:
        # Показываем форму с текущими данными
        form = CryptoAssetForm(instance=asset)
    
    return render(request, 'portfolio/edit_asset.html', {'form': form, 'asset': asset})

@login_required
def delete_asset(request, asset_id):
    # Находим и удаляем актив
    asset = get_object_or_404(CryptoAsset, id=asset_id, user=request.user)
    asset.delete()
    return redirect('portfolio_list')