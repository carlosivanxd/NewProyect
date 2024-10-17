from django.shortcuts import render

# Define tu función de vista para manejar solicitudes de inicio de sesión
def login_view(request):
    # Especifica el archivo de plantilla que renderizará la página de inicio de sesión
    template_view = "login.html"

    # Renderiza la plantilla de inicio de sesión y devuelve la respuesta
    return render(request, template_name=template_view)