from django.shortcuts import render, redirect
from apps.prestamos.models import Prestar, Usuario, Ejemplar
from apps.prestamos.form_Prestar import PrestarForm
from apps.prestamos.form_Usuario import UsuarioForm
from apps.prestamos.form_Ejemplar import EjemplarForm
from django.db.models import Count #Para usar el count se debe importar
#from django.db.models import Sum #Se usa para sumar

# Create your views here.

def listPrestamos(request):
    prestamos = Prestar.objects.all().order_by('id')
    context = {'prestamos':prestamos}
    return render(request, 'prestamos/listPrestamos.html', context)


def PrestarCreate(request):
    if request.method == 'POST':
        form = PrestarForm(request.POST) #clase que importo desde el archivo ventaform.py
        if form.is_valid():
            form.save()
        return redirect('prestamos:listPrestamos') #el enlace que puse en base.html cuando va a vehiculos
    else:
        form =PrestarForm()
        return render(request,'prestamos/prestar_form.html', {'form': form})

def PrestarEdit(request, id_prestar):

    prestar= Prestar.objects.get(pk=id_prestar)

    if request.method == 'GET':
        form = PrestarForm(instance=prestar) #clase que importo desde el archivo formVehiculo.py
    else:
        form =PrestarForm(request.POST, instance=prestar)
        if form.is_valid():
            form.save()
        
        return redirect('prestamos:listPrestamos')

    return render(request,'prestamos/prestar_form.html', {'form': form})

def PrestarElim(request, id_prestar):

    prestar= Prestar.objects.get(pk=id_prestar)

    if request.method == 'POST':
        prestar.delete() #clase que importo desde el archivo formVehiculo.py
        return redirect('prestamos:listPrestamos')
    
    return render(request,'prestamos/PrestarElimform.html', {'prestamos': prestar})



#----------------------------------------------------
#--------------------- USUARIO-----------------------
#----------------------------------------------------

def listUsuarios(request):
    usuarios = Usuario.objects.all().order_by('id')
    context = {'usuarios':usuarios}
    return render(request, 'usuarios/listUsuario.html', context)


def UsuarioCreate(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST) #clase que importo desde el archivo ventaform.py
        if form.is_valid():
            form.save()
        return redirect('prestamos:listUsuarios') #el enlace que puse en base.html cuando va a vehiculos
    else:
        form =UsuarioForm()
        return render(request,'usuarios/usuario_form.html', {'form': form})

def UsuarioEdit(request, id_usuario):

    usuario= Usuario.objects.get(pk=id_usuario)

    if request.method == 'GET':
        form = UsuarioForm(instance=usuario) #clase que importo desde el archivo formVehiculo.py
    else:
        form =UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
        
        return redirect('prestamos:listUsuarios')

    return render(request,'usuarios/usuario_form.html', {'form': form})

def UsuarioElim(request, id_usuario):

    usuario= Usuario.objects.get(pk=id_usuario)

    if request.method == 'POST':
        usuario.delete() #clase que importo desde el archivo formVehiculo.py
        return redirect('prestamos:listUsuarios')
    
    return render(request,'usuarios/UsuarioElimform.html', {'usuarios': usuario})






#--------------------------------------------------------
#---------------------- EJEMPLARES ----------------------
#--------------------------------------------------------

def listEjemplares(request):
    ejemplares = Ejemplar.objects.all().order_by('id')
    context = {'ejemplares':ejemplares}
    return render(request, 'ejemplares/listEjemplares.html', context)


def EjemplarCreate(request):
    if request.method == 'POST':
        form = EjemplarForm(request.POST) #clase que importo desde el archivo ventaform.py
        if form.is_valid():
            form.save()
        return redirect('prestamos:listEjemplares') #el enlace que puse en base.html cuando va a vehiculos
    else:
        form =EjemplarForm()
        return render(request,'ejemplares/ejemplar_form.html', {'form': form})

def EjemplarEdit(request, id_ejemplar):

    ejemplar= Ejemplar.objects.get(pk=id_ejemplar)

    if request.method == 'GET':
        form = EjemplarForm(instance=ejemplar) #clase que importo desde el archivo formVehiculo.py
    else:
        form =EjemplarForm(request.POST, instance=ejemplar)
        if form.is_valid():
            form.save()
        
        return redirect('prestamos:listEjemplares')

    return render(request,'ejemplares/ejemplar_form.html', {'form': form})

def EjemplarElim(request, id_ejemplar):

    ejemplar= Ejemplar.objects.get(pk=id_ejemplar)

    if request.method == 'POST':
        ejemplar.delete() #clase que importo desde el archivo formVehiculo.py
        return redirect('prestamos:listEjemplares')
    
    return render(request,'ejemplares/EjemplarElimform.html', {'ejemplares': ejemplar})





#----------------------------------
#------------ CONSULTAS -----------
#----------------------------------

def consulta1(request):
    fecha1 = request.POST.get('fecha1')
    fecha2 = request.POST.get('fecha2')
    consulta1=Prestar.objects.values('id','usuario__nombre','ejemplar__localizacion','ejemplar__libro__titulo','ejemplar__libro__autor__nombre','fechadev','fechapres').filter(fechapres__range=[fecha1,fecha2])
    
    context = {
        'fecha1':fecha1,
        'fecha2': fecha2,
        'consulta1': consulta1
    }
    print(consulta1)
    return render(request,'consultas/Consulta1.html',{'context':context})


def consulta2(request):
    fecha1 = request.POST.get('fecha1')
    fecha2 = request.POST.get('fecha2')
    consulta2=Prestar.objects.values('id','usuario__nombre','ejemplar__libro__titulo').filter(fechapres__range=[fecha1,fecha2]).annotate(total=Count('ejemplar__libro__titulo'))
    #cantidad= Prestar.objects.values('ejemplar__libro__titulo').filter(fechapres__range=[fecha1,fecha2]).annotate(total=Count('ejemplar__libro')).aggregate(Sum('total'))
    
    context = {
        'fecha1':fecha1,
        'fecha2': fecha2,
        'consulta2': consulta2,
        #'cantidad':cantidad
    }
    print(consulta2)
    return render(request,'consultas/Consulta2.html',{'context':context})


def consulta3(request):
    fecha1 = request.POST.get('fecha1')
    fecha2 = request.POST.get('fecha2')
    consulta3=Prestar.objects.values('usuario__nombre').filter(fechapres__range=[fecha1,fecha2]).annotate(total=Count('ejemplar__libro__titulo'))
    
    context = {
        'fecha1':fecha1,
        'fecha2': fecha2,
        'consulta3': consulta3,
    }
    print(consulta3)
    return render(request,'consultas/Consulta3.html',{'context':context})