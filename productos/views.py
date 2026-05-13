from django.shortcuts import render, redirect, get_object_or_404
from .models import Alfajor
from .forms import AlfajorForm


def home(request):
    return render(request, "productos/home.html")


def alfajor(request):
    alfajores = Alfajor.objects.all().order_by("-id")
    return render(request, "productos/alfajor.html", {"alfajores": alfajores})


def alfajor_listar(request):
    alfajores = Alfajor.objects.all().order_by("-id")
    return render(request, "productos/alfajor_listar.html", {"alfajores": alfajores})


def alfajor_crear(request):
    if request.method == "POST":
        form = AlfajorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("alfajor_listar")
    else:
        form = AlfajorForm()

    return render(request, "productos/alfajor_form.html", {"form": form})


def alfajor_editar(request, id):
    alfajor = get_object_or_404(Alfajor, id=id)

    if request.method == "POST":
        form = AlfajorForm(request.POST, instance=alfajor)
        if form.is_valid():
            form.save()
            return redirect("alfajor_listar")
    else:
        form = AlfajorForm(instance=alfajor)

    return render(request, "productos/alfajor_form.html", {"form": form})


def alfajor_eliminar(request, id):
    alfajor = get_object_or_404(Alfajor, id=id)

    if request.method == "POST":
        alfajor.delete()
        return redirect("alfajor_listar")

    return render(request, "productos/alfajor_confirmar_eliminar.html", {"alfajor": alfajor})