from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from text_generator import generate
from django.views.decorators.csrf import csrf_exempt,csrf_protect

from .forms import Cadastro
from .models import Usuario

@csrf_exempt
def index(request):
    usuario = Usuario()
    users_qtd = len(Usuario.objects.all())
    if request.method == 'POST':
        form = Cadastro(request.POST)

        if form.is_valid():
            usuario.email = request.POST.get('email')
            usuario.nascimento = request.POST.get('nascimento')

            senha = request.POST.get('senha')

            if not senha:
                senha = generate(length_maximal=20)

            usuario.senha = senha
            usuario.save()

            return HttpResponseRedirect('/cadastro/')
    else:
        form = Cadastro()

    return render(request, 'cadastro/index.html', {'form': form, 'users': users_qtd})

def get_data(request):

    users = Usuario.objects.all()

    from openpyxl import Workbook
    from pathlib import Path
    import mimetypes
    import os

    wb = Workbook()
    ws = wb.active

    for row, user in enumerate(users):
        nascimento = user.nascimento.strftime("%d/%m/%Y")
        fields = [user.email, user.senha, nascimento]
        for cell in range(3):
            field = fields[cell]
            ws.cell(row=row + 1, column=cell+1, value=field)

    file_name = "Usuarios Cadastrados.xlsx"
    wb.save(file_name)

    FILE_DIR = Path(__file__).resolve().parent.parent
    FILE = FILE_DIR.joinpath(file_name)

    fl = open(FILE, 'rb')
    mime_type, _ = mimetypes.guess_type(FILE)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % file_name
    os.remove(FILE)

    return response