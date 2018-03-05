from django.db import models

class Funcionario(models.Model):
    ECIVIL_CHOICES = (
        ("solteiro", "Solteiro"),
        ("casado", "Casado"),
        ("separado", "Separado"),
        ("divorciado", "Divorciado"),
        ("viúvo", "Viúvo"),
    )
    SEXO_CHOICES = (
        ("feminino", "Feminino"),
        ("masculino", "Masculino"),
    )
    TIPO_CHOICES = (
        ("fichado", "Fichado"),
        ("experiência", "Experiência"),
        ("diarista", "Diarista"),
    )
    nome = models.CharField(max_length=255, null=False)
    cpf = models.CharField(max_length=14, null=False, verbose_name="CPF")
    rg = models.CharField(max_length=7, null=False, verbose_name="RG")
    sexo = models.CharField(max_length=20, null=False, choices=SEXO_CHOICES)
    estado_civil = models.CharField(max_length=20, null=False, choices=ECIVIL_CHOICES, verbose_name="Estado Civil")
    nome_pai = models.CharField(max_length=255, null=False, verbose_name="Nome do Pai")
    nome_mae = models.CharField(max_length=255, null=False, verbose_name="Nome da Mãe")
    data_nascimento = models.DateField(null=False, verbose_name="Data de Nascimento")
    data_adimicao = models.DateField(null=False, verbose_name="Data de Adimição")
    numero_ctps = models.CharField(max_length=11, null=False, verbose_name="Número CTPS")
    numero_pis = models.CharField(max_length=11, null=False, verbose_name="Número do PIS")
    tipo = models.CharField(max_length=20, null=False, choices=TIPO_CHOICES)


    def __str__(self):
        return self.nome

class Cliente(models.Model):
    ECIVIL_CHOICES = (
        ("solteiro", "Solteiro"),
        ("casado", "Casado"),
        ("separado", "Separado"),
        ("divorciado", "Divorciado"),
        ("viúvo", "Viúvo"),
    )
    SEXO_CHOICES = (
        ("feminino", "Feminino"),
        ("masculino", "Masculino"),
    )

    nome = models.CharField(max_length=255, null=False)
    cpf = models.CharField(max_length=14, null=False, verbose_name="CPF")
    rg = models.CharField(max_length=7, null=False, verbose_name="RG")
    sexo = models.CharField(max_length=20, null=False, choices=SEXO_CHOICES)
    estado_civil = models.CharField(max_length=20, null=False, choices=ECIVIL_CHOICES, verbose_name="Estado Civil")
    nome_pai = models.CharField(max_length=255, null=False, verbose_name="Nome do Pai")
    nome_mae = models.CharField(max_length=255, null=False, verbose_name="Nome da Mãe")
    data_nascimento = models.DateField(null=False, verbose_name="Data de Nascimento")

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    ESTADO_CHOICES = (
        ("pe", "PE"), ("ac", "AC"), ("al", "AL"), ("am", "AM"), ("ap", "AP"), ("ba", "BA"), ("ce", "CE"), ("df", "DF"),
        ("es", "ES"), ("go", "GO"), ("ma", "MA"), ("mg", "MG"), ("ms", "MS"), ("mt", "MT"), ("pa", "PA"), ("pb", "PB"),
        ("pi", "PI"), ("pr", "PR"), ("rj", "RJ"), ("rn", "RN"), ("ro", "RO"), ("rr", "RR"), ("rs", "RS"), ("sc", "SC"),
        ("se", "SE"), ("sp", "SP"), ("to", "TO"),
    )
    rua = models.CharField(max_length=255, null=False)
    numero = models.IntegerField(null=False)
    bairro = models.CharField(max_length=50, null=False)
    complemento = models.CharField(max_length=50, null=False)
    cep = models.CharField(max_length=8, null=False)
    cidade = models.CharField(max_length=50, null=False)
    estado = models.CharField(max_length=20, null=False, choices=ESTADO_CHOICES)
    funcionario = models.ForeignKey(Funcionario)

    def __str__(self):
        return self.rua

class Contato(models.Model):
    SEXO_CHOICES = (
        ("telefone", "Telefone"),
        ("email", "Email"),
        ("facebook", "Facebook"),
    )
    contato = models.CharField(max_length=50, null=False)
    tipo = models.CharField(max_length=20, null=False, choices=SEXO_CHOICES)
    funcionario = models.ForeignKey(Funcionario)

    def __str__(self):
        return self.contato

class Fornecedor(models.Model):
    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    razao_social = models.CharField('Razão Social', max_length=100)
    nome_fantasia = models.CharField('Nome Fantasia', max_length=100)
    tipo_fornecimento = models.CharField('Tipo de Fornecimento', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=20)
    telefone = models.CharField('Telefone', max_length=100)

class Veiculo(models.Model):
    CORES_CHOICES = (
        ("preto", "Preto"),
        ("azul", "Azul"),
        ("amarelo", "Amarelo"),
        ("branco", "Branco"),
        ("prata", "Prata"),
        ("vermelho", "Vermelho"),
    )
    TIPO_CHOICES = (
        ("moto", "Moto"),
        ("carro", "Carro"),
        ("caminhão", "Caminhão"),
        ("máquina", "Máquina"),
    )
    modelo = models.CharField(max_length=50, null=False)
    marca = models.CharField(max_length=20, null=False)
    placa = models.CharField(max_length=8, null=False)
    cor = models.CharField(max_length=20, null=False, choices=CORES_CHOICES)
    ano = models.IntegerField(null=False)
    preco = models.FloatField(null=False)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    def __str__(self):
        return self.modelo

# Entidades Fracas

class Estoque(models.Model):
    class Meta:
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoque'

    valor_compra = models.CharField('Valor da Compra', max_length=9)
    valor_venda = models.CharField('Valor da Venda', max_length=9)
    quantidade = models.CharField('Quantidade', max_length=9)
    taxa_lucro = models.CharField('Taxa de Lucro', max_length=9)
    especificacao = models.CharField('Especificacao', max_length=100)
    nome = models.CharField('Nome', max_length=100)


class Locacao(models.Model):
    class Meta:
        verbose_name = 'Locação'
        verbose_name_plural = 'Locações'
    valor = models.CharField('Valor', max_length=9)
    data_locacao = models.DateField(null=False, verbose_name="Data de Início")
    data_entrega = models.DateField(null=False, verbose_name="Data de Fim")
    veiculo = models.ManyToManyField(Veiculo)
    cliente = models.ForeignKey(Cliente)





class Produto(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    quantidade = models.CharField('Quantidade', max_length=9)
    tipo = models.CharField('Tipo', max_length=9)


class Venda(models.Model):
    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

    valor = models.CharField('Valor', max_length=9)
    data_de_venda = models.CharField('Data de Venda', max_length=9)
    quantidade = models.CharField('Quantidade', max_length=9)
