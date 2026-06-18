from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserLoginForm, UserUpdateForm, UserProfileForm, AddressForm
from .models import Address, UserProfile

def register_view(request):
    if request.user.is_authenticated:
        return redirect('menu:menu_list')
        
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to Crave, {user.first_name}!')
            return redirect('menu:menu_list')
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('menu:menu_list')
        
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            remember_me = form.cleaned_data.get('remember_me')
            if not remember_me:
                # Set session to expire when the browser is closed
                request.session.set_expiry(0)
                
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('menu:menu_list')
    else:
        form = UserLoginForm()
        
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST' or request.method == 'GET': # Normally POST is better, but GET is fine for a simple link
        logout(request)
        messages.success(request, 'You have been successfully logged out.')
        return redirect('users:login')

@login_required
def profile_view(request):
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        # Check which form was submitted via a hidden input or just by checking fields
        if 'update_profile' in request.POST:
            user_form = UserUpdateForm(request.POST, instance=request.user)
            profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Your profile has been updated successfully.')
                return redirect('users:profile')
        elif 'add_address' in request.POST:
            address_form = AddressForm(request.POST)
            if address_form.is_valid():
                address = address_form.save(commit=False)
                address.user = request.user
                address.save()
                messages.success(request, 'New address added successfully.')
                return redirect('/users/profile/?tab=addresses')
    
    user_form = UserUpdateForm(instance=request.user)
    profile_form = UserProfileForm(instance=profile)
    address_form = AddressForm()
    
    addresses = request.user.addresses.all()
    # We will pass orders in from the orders app using a related name or query
    orders = request.user.orders.prefetch_related('items__product').all() if hasattr(request.user, 'orders') else []

    active_tab = request.GET.get('tab', 'profile')

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'address_form': address_form,
        'addresses': addresses,
        'orders': orders,
        'active_tab': active_tab,
    }
    return render(request, 'users/profile.html', context)
