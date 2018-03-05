from django.contrib import admin

from .models import *

class ContatoInline(admin.TabularInline):
    model = Contato

class EnderecoInline(admin.TabularInline):
    model = Endereco

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">people_outline</i>'
    inlines = [ContatoInline,EnderecoInline]
    list_display = ('nome', 'data_adimicao')
    search_fields = ['nome', 'cpf']

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">people_outline</i>'
    list_display = ('nome',)
    search_fields = ['nome', 'cpf']

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
	list_display = ('placa', 'ano','modelo')
	search_fields = ['modelo','ano','placa']

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
	list_display = ('nome_fantasia','telefone')
	search_fields = ['nome_fantasia']


@admin.register(Locacao)
class LocacaoAdmin(admin.ModelAdmin):
	list_display = ('valor', 'data_locacao', 'data_entrega')
	search_fields = ['valor',]

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
	list_display = ('quantidade','tipo')
	search_fields = ['quantidade','tipo']

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
	list_display = ('valor','data_de_venda','quantidade')
	search_fields = ['valor','data_de_venda','quantidade']

