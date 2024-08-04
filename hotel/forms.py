from django import forms

from hotel.models import Room, Type, Reservation


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = 'name',


class ReservationForm(forms.ModelForm):
    arrival_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    departure_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Reservation
        fields = 'arrival_date', 'departure_date',
