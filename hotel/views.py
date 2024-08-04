from django.http import HttpResponse
from django.shortcuts import render, redirect

from hotel.models import Room, Reservation
from hotel.forms import RoomForm, ReservationForm, TypeForm

# Create your views here.


def index(request):
    ctx = {
        'rooms': Room.objects.all()
    }

    return render(request, 'hotel/index.html', ctx)


def room_res(request, id):
    room = Room.objects.get(id=id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['arrival_date'] < form.cleaned_data['departure_date']:
                res_room = form.save(commit=False)
                res_room.room = room
                res_room.user = request.user
                res_room.save()

    reservations = Reservation.objects.filter(room=room)
    ctx = {
        'room': room,
        'form': ReservationForm(),
        'reservations': reservations
    }

    return render(request, 'hotel/room_res.html', ctx)


def profile(request):
    reservations = Reservation.objects.filter(user=request.user)
    ctx = {
        'reservations': reservations
    }

    return render(request, 'hotel/profile.html', ctx)


def delete_res(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    reservation.delete()
    return redirect('profile')


def edit(request):
    if not request.user.is_superuser:
        return redirect('index')
    ctx = {
        'rooms': Room.objects.all()
    }

    return render(request, 'hotel/edit.html', ctx)


def add_room(request):
    if not request.user.is_superuser:
        return redirect('index')
    if request.method == 'POST':
        print(1)
        print('ee')
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            print(2)
            form.save()
            return redirect('edit')
        else:
            print(form.errors)
    ctx = {
        'form': RoomForm()
    }

    return render(request, 'hotel/add_room.html', ctx)


def edit_room(request, pk):
    if not request.user.is_superuser:
        return redirect('index')
    room = Room.objects.get(pk=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            return redirect('edit')

    ctx = {
        'form': RoomForm(instance=room)
    }

    return render(request, 'hotel/edit_room.html', ctx)


def delete_room(request, pk):
    if not request.user.is_superuser:
        return redirect('index')
    room = Room.objects.get(pk=pk)
    room.delete()

    return redirect('edit')
