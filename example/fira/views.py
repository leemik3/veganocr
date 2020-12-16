from django.views.generic import CreateView
from fira.models import Fira
from fira.models import Vegan
from fira.forms import FiraForm
import os
import easyocr
import cv2
import glob

from django.shortcuts import render



def index(request):
    return render(request,'index.html')


class FiraCreateView(CreateView):
    model = Fira
    form_class = FiraForm
    template_name = 'create.html'
    success_url = '../result/'

def result(request):
    if request.method=='POST':
        form = FiraForm(request.POST, request.FILES)
        if form.is_valid():
            print("폼 정확함")
            print(form.cleaned_data)
    else:
        form = FiraForm()


    files_Path = "media/fira/" # 파일들이 들어있는 폴더
    file_name_and_time_lst = []
    # 해당 경로에 있는 파일들의 생성시간을 함께 리스트로 넣어줌.
    for f_name in os.listdir(f"{files_Path}"):
        written_time = os.path.getctime(f"{files_Path}{f_name}")
        file_name_and_time_lst.append((f_name, written_time))
    # 생성시간 역순으로 정렬하고,
    sorted_file_lst = sorted(file_name_and_time_lst, key=lambda x: x[1], reverse=True)
    # 가장 앞에 이는 놈을 넣어준다.
    recent_file = sorted_file_lst[0]
    recent_file_name = recent_file[0]

    ##ocr
    reader = easyocr.Reader(['ko'])
    pathname = "./media/fira/"+recent_file_name
    output = reader.readtext(pathname)
    strresult = "".join([i[1] for i in output])
    print(strresult)
    print(Vegan.objects.all())
    db = Vegan.objects.filter(vegan__contains="0").values_list('material',flat=True)
    print(db)
    veganyn="섭취 가능"
    for i in db:
        if i in strresult:
            veganyn = "섭취 불가 : "+i+"성분 함유"
            print(i)
            break

    vegan = {'data' : veganyn}
    if veganyn=="섭취 가능":
        return render(request, 'result2.html', vegan)
    return render(request, 'result.html', vegan)
