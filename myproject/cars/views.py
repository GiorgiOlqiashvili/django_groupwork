from django.shortcuts import render, get_object_or_404, redirect
from .models import Car
from .forms import CarForm


def car_list(request):
    query = request.GET.get('q')
    if query:
        cars = Car.objects.filter(name__icontains=query)
    else:
        cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'cars/car_detail.html', {'car': car})


def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)  # Use request.FILES to handle file uploads
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'cars/add_car.html', {'form': form})


