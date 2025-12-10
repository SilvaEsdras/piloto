from django import forms

class ContatoForm(forms.Form):
    ASSUNTO_CHOICES = [
        ('suporte', 'Suporte técnico'),
        ('comercial', 'Comercial'),
        ('reclamacao', 'Reclamação'),
        ('parceria', 'Parceria'),
        ('financeiro', 'Financeiro'),
    ]

    nome = forms.CharField(
        max_length=100, 
        label='Nome Completo',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'})
    )
    
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'})
    )


    telefone = forms.CharField(
        label='Telefone / WhatsApp',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(99) 99999-9999'})
    )


    assunto = forms.ChoiceField(
        choices=ASSUNTO_CHOICES,
        label='Assunto do contato',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    mensagem = forms.CharField(
        label='Mensagem',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva sua mensagem', 'rows': 4})
    )

class ProdutoForm(forms.Form):
    nome = forms.CharField(
        max_length=100, 
        label='Nome do Produto',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do produto'})
    )
    preco = forms.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        label='Preço',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite o preço'})
    )