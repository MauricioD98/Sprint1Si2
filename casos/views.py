from django.shortcuts import render,redirect,get_object_or_404
from .models import Caso, Expediente
from .forms import CasoForm,ExpedienteForm

def casos(request):
    if request.method == 'POST':
        form = CasoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expedientes/')  # URL que corresponda expediente
    else:
        form = CasoForm()

    return render(request, 'casos.html', {'form': form})

def expedientes(request):
    if request.method == 'POST':
        form = ExpedienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/casos/expedientes/vista_expediente')  # URL que corresponda vista
    else:
        form = ExpedienteForm()
    return render(request, 'expedientes.html', {'form': form})

def vista(request):
    casos= Caso.objects.all()
    return render(request, 'vista.html',{
        'casos':casos
                                         })

def vista_expediente(request):
    expedientes= Expediente.objects.all()
    return render(request, 'vista_expediente.html',{
        'expedientes':expedientes
                                         })

def eliminar_caso(request,id):
    caso=get_object_or_404(Caso,id=id)
    caso.delete()
    return redirect('/casos/expedientes/vista') 

def eliminar_expediente(request,id):
    expediente=get_object_or_404(Expediente,id=id)
    expediente.delete()
    return redirect('/casos/expedientes/vista_expediente')