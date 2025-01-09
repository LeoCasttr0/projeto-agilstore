from django.shortcuts import render,redirect
from agilstoreapp.forms import ProdutosForm
from agilstoreapp.models import Produtos
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')  # Obtém o termo de busca da URL

    # Filtrar os dados, se houver busca
    if search:
        queryset = Produtos.objects.filter(nomeProduto__icontains=search)
    else:
        queryset = Produtos.objects.all()

    # Paginar os resultados filtrados
    paginator = Paginator(queryset, 2)  # Mostra 2 itens por página
    page = request.GET.get('page')  # Obtém o número da página da URL
    data['db'] = paginator.get_page(page)  # Define os dados paginados

    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = ProdutosForm()
    return render(request, 'form.html', data)

def create(request):
    form = ProdutosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data={}
    data['db'] = Produtos.objects.get(pk=pk)
    data['form'] = ProdutosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request,pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    form = ProdutosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
        db = Produtos.objects.get(pk=pk)
        db.delete()
        return redirect('home')
