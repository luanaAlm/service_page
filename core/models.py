from django.db import models


class Cliente(models.Model):
    ID_Cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=11)
    mensagem = models.TextField()

    def __str__(self):
        template = '{0.nome} {0.email} {0.telefone} {0.mensagem}'
        return template.format(self)


class Portifolio_cliente (models.Model):
    UF_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernanbuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocantins')
    )
    ID_Portifolio = models.AutoField(primary_key=True)
    logomarca = models.ImageField(
        upload_to="img_portifolio/%y", blank=False, null=False)
    image = models.ImageField(
        upload_to="img_portifolio/%y", blank=False, null=False)
    link = models.URLField(max_length=400)
    empresa = models.CharField(max_length=100, blank=False, null=False)
    cidade = models.CharField(max_length=100, blank=False, null=False)
    estado = models.CharField(max_length=100, choices=UF_CHOICES)

    def __str__(self):
        template = '{0.empresa} {0.cidade} {0.estado}'
        return template.format(self)


class Social_Media (models.Model):
    UF_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernanbuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocantins')
    )
    ID_Social_Media = models.AutoField(primary_key=True)
    logomarca = models.ImageField(
        upload_to="img_portifolio/%y", blank=False, null=False)
    empresa = models.CharField(max_length=100, blank=False, null=False)
    cidade = models.CharField(max_length=100, blank=False, null=False)
    estado = models.CharField(max_length=100, choices=UF_CHOICES)

    def __str__(self):
        template = '{0.empresa} {0.cidade} {0.estado}'
        return template.format(self)
