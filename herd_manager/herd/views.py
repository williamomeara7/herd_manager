from django.shortcuts import render, redirect

from .forms import AnimalForm
from .models import Animal, value_per_kg


def getHerd():
    queryset = Animal.objects.all()
    herd = []
    for item in queryset:
        herd.append({
            "id": item.id,
            "price": item.price,
            "type": item.type,
            "weight": item.weight,
            "value": item.get_current_value(),
            "profit": item.get_profit()

        })
    return herd


# Create your views here.
def herd_list_view(request):
    queryset = Animal.objects.all()
    sum = 0
    profit = 0
    for item in queryset:
        sum += item.get_current_value()
        profit += item.get_profit()
    herd = getHerd()
    context = {
        "herd": herd,
        "animal_list": queryset,
        "sum": sum,
        "profit": profit
    }
    return render(request, "herd/herd_list.html", context)


def animal_add_view(request):
    form = AnimalForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AnimalForm()
    context = {
        'form': form
    }
    return render(request, "herd/animal_add.html", context)


def animal_update_view(request, pk):
    animal = Animal.objects.get(id=pk)
    form = AnimalForm(instance=animal)
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('/herd')
    context = {
        'form': form
    }
    return render(request, "herd/animal_update.html", context)


def animal_delete_view(request, pk):
    Animal.objects.get(id=pk).delete()
    return redirect('/herd')