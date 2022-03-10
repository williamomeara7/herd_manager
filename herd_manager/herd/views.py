from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from .forms import AnimalForm, CreateUserForm
from .models import Animal, value_per_kg

# values = value_per_kg.objects.all()


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

# def getTable():
#     animal = Animal.objects.get(id=6)
#     herd = []
#     for

# Create your views here.
def herd_list_view(request):
    queryset = Animal.objects.all()
    sum = 0
    profit = 0
    for item in queryset:

        sum += item.get_current_value()
        profit += item.get_profit()
    herd = getHerd()
    # animal = Animal.objects.get(id=5)
    context = {
        "herd": herd,
        "table": table_view(),
        "animal_list": queryset,
        "sum": sum,
        "profit": profit,
        # "table": animal.get_all_values()
    }
    return render(request, "herd/herd_list.html", context)

def table_view():
    queryset = Animal.objects.all()
    data = {}
    for item in queryset:
        animal_data = item.get_all_values()
        for current_date in animal_data:
            if current_date['x'] not in data:
                data[current_date['x']] = 0
                data[current_date['x']] += current_date['y'] * item.get_weight()
            else:
                data[current_date['x']] += current_date['y'] * item.get_weight()


    output = []
    for key in data:
        output.append({
            "y": data[key],
            "x": key
        })

    context = {
        # "dates": animal.get_all_dates(),
        "table": output
    }
    return output


def valid_animal(request):
    post = request.POST
    query = value_per_kg.objects.filter(type=f"{post['type']}", letter_grade=f"{post['letter_grade']}",
                                        number_grade=f"{post['number_grade']}").reverse()
    for item in query:
        current_value = item.get_value_per_kg()
        if current_value != -1:
            return True
        return False





def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, f'User {form.cleaned_data["username"]} was created')

    context = {'form': form}
    return render(request, "accounts/register.html", context)



def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/herd")
        else:
            messages.add_message(request, messages.INFO, "Username or password is incorrect")
    context = {}
    return render(request, "accounts/login.html", context)


def logout_user(request):
    logout(request)
    return redirect('login')

def animal_add_view(request):
    form = AnimalForm(request.POST or None)
    if form.is_valid():
        if valid_animal(request):
            form.save()
        else:
            messages.add_message(request, messages.WARNING, 'No data for given entry')
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

def test(request, pk):
    animal = Animal.objects.get(id=pk)
    animal.get_all_values()
    context = {
        "table" : animal.get_all_values()
    }
    return render(request, "herd/herd_list.html", context)