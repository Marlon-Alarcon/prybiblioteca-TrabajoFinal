from django.shortcuts import render, redirect
from apps.libros.models import Libro, Autor
from apps.libros.form_Libro import LibroForm
from apps.libros.form_Autor import AutorForm

# Create your views here.

def listLibros(request):
    libros = Libro.objects.all().order_by('id')
    context = {'libros':libros}
    return render(request, 'libros/listLibros.html', context)

def home (request):
    return render(request, 'base/base.html')

def LibroCreate(request):
    if request.method == 'POST':
        form = LibroForm(request.POST) #clase que importo desde el archivo ventaform.py
        if form.is_valid():
            form.save()
        return redirect('libros:listLibros') #el enlace que puse en base.html cuando va a vehiculos
    else:
        form =LibroForm()
        return render(request,'libros/libro_form.html', {'form': form})

def LibroEdit(request, id_libro):

    libro= Libro.objects.get(pk=id_libro)

    if request.method == 'GET':
        form = LibroForm(instance=libro) #clase que importo desde el archivo formVehiculo.py
    else:
        form =LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
        
        return redirect('libros:listLibros')

    return render(request,'libros/libro_form.html', {'form': form})

def libroElim(request, id_libro):

    libro= Libro.objects.get(pk=id_libro)

    if request.method == 'POST':
        libro.delete() #clase que importo desde el archivo formVehiculo.py
        return redirect('libros:listLibros')
    
    return render(request,'libros/LibroElimform.html', {'libros': libro})





#------------------------------------
#-------------- AUTOR ---------------
#------------------------------------

def listAutores(request):
    autores = Autor.objects.all().order_by('id')
    context = {'autores':autores}
    return render(request, 'autores/listAutores.html', context)


def AutorCreate(request):
    if request.method == 'POST':
        form = AutorForm(request.POST) #clase que importo desde el archivo ventaform.py
        if form.is_valid():
            form.save()
        return redirect('libros:listAutores') #el enlace que puse en base.html cuando va a vehiculos
    else:
        form =AutorForm()
        return render(request,'autores/autores_form.html', {'form': form})


def AutorEdit(request, id_autor):

    autor= Autor.objects.get(pk=id_autor)

    if request.method == 'GET':
        form = AutorForm(instance=autor) #clase que importo desde el archivo formVehiculo.py
    else:
        form =AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
        
        return redirect('libros:listAutores')

    return render(request,'autores/autores_form.html', {'form': form})

def AutorElim(request, id_autor):

    autor= Autor.objects.get(pk=id_autor)

    if request.method == 'POST':
        autor.delete() #clase que importo desde el archivo formVehiculo.py
        return redirect('libros:listAutores')
    
    return render(request,'autores/AutorElimform.html', {'autores': autor})