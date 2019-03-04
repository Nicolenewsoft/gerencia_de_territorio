from django.shortcuts import render, redirect, get_object_or_404
from .models import Formulario, Atualizacao_territorio
from .forms import AddForm, Att_territorio

# Create your views here.
def form(request):
    
        form = AddForm(request.POST or None) #Receberá dos forms, onde vai fazer uma requisição post, caso não tenha: None,
    if form.is_valid():
        form.save()
    
        #return redirect('/')
    
    return render(request, 'form.html', {'form': form})

def att(request):
    att = Att_territorio(request.POST or None)
    if att.is_valid():
        att.save()
    return render(request, 'att_territorio.html', {'att': att})

def territorio_list(request):

    atualizacao_territorios = Atualizacao_territorio.objects.all()
    return render(request, "territorios.html", {'atualizacao_territorios': atualizacao_territorios})
    

def territorios_update(request, id):
    atualizacao_territorio = get_object_or_404(Atualizacao_territorio, pk=id)
    att = Att_territorio(request.POST or None, instance=atualizacao_territorio)
    if att.is_valid():
        att.save()
        return redirect('territorio_list')
    return render(request, 'att_territorio.html', {'att': att})

def territorios_delete(request, id):
    atualizacao_territorio = get_object_or_404(Atualizacao_territorio, pk=id)
    att = Att_territorio(request.POST or None, instance=atualizacao_territorio)

    if request.method == 'POST':
        atualizacao_territorio.delete()
        return redirect('territorio_list')
    return render(request, 'territorio_delete_confirm.html', {'att': att})

