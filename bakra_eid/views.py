from django.shortcuts import render

from .models import EidModel

def bakra_home(request):
    name = request.POST.get('greeter_name_input')
    if request.method == 'POST':
        name = name.lower()
        EidModel.objects.create(greeter_name=name)
        filter_data = EidModel.objects.filter(greeter_name=name)
        for data in filter_data:
            pass
        if request.is_secure():
            share_link = "https://bakraeid.herokuapp.com/name:" + str(f"{name}" + "/id:" + str(f"{data.pk}"))        
        else:
            share_link = "http://bakraeid.herokuapp.com/name:" + str(f"{name}" + "/id:" + str(f"{data.pk}"))
        return render(request, 'bakra_home.html', {'name':name, 'share_link': share_link})
    return render(request, 'bakra_home.html', {'name':name})


def bakra_display_name(request, name, pk):
    # print(request.path)
    extract_name = ""
    print(name)
    # filter person and show his/her name
    query_name = EidModel.objects.filter(greeter_name=name)
    extracted_name = query_name.filter(pk=pk)
    for extract_name in extracted_name:
        pass
    print(extract_name)
    # for making a new entry on the same page
    name = request.POST.get("greeter_name_input")
    name = request.POST.get('greeter_name_input')
    if request.method == 'POST':
        EidModel.objects.create(greeter_name=name)
        filter_data = EidModel.objects.filter(greeter_name=name)
        for data in filter_data:
            pass
        if request.is_secure():
            share_link = "https://bakraeid.herokuapp.com/name:" + str(f"{name}" + "/id:" + str(f"{data.pk}"))        
        else:
            share_link = "http://bakraeid.herokuapp.com/name:" + str(f"{name}" + "/id:" + str(f"{data.pk}"))
        return render(request, 'bakra_home.html', {'name':name, 'share_link': share_link})
    return render(request, 'bakra_home.html', {'extract_name':extract_name, 'request':request.path})
