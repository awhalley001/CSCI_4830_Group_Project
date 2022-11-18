from django.shortcuts import render

# Create your views here.
# def about(request):
#     return render(request, "about.html")

# def problem_statement(request):
#     return render(request, "problem_statement.html")

# def software_design_document(request):
#     return render(request, "software_design_docuement.html")

def home(request):
    return render(request, "home.html")