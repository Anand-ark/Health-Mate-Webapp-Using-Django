from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
import numpy as np
from PIL import Image
from keras.models import load_model
from keras.preprocessing import image
import joblib

import tensorflow as tf
model =load_model('./models/malaria_detection.h5')

img_height,img_width=128,128

def index(request):
    return render(request,'App/index.html',{})

def about(request):
    #return HttpResponse('<h1>Welcome </h1>')
    return render(request, 'App/about.html')
def contact(request):
    return render(request, 'App/contact.html')
def diabetes(request):
    return render(request, 'App/diabetes.html')
def malariaa(request):
    return render(request, 'App/malariaa.html')
def pneumonia(request):
    return render(request, 'App/pneumonia.html')
def predict(request):
    lis=[]
    lis.append(int(request.GET['N1']))
    lis.append(int(request.GET['N2']))
    lis.append(int(request.GET['N3']))
    N = np.array(lis)
    pred=np.sum(N)
    return render(request, 'App/diabetes.html', {'pred':pred})
def upload1(request):#Pneumonia
    p1 = request.FILES['image'];
    fs1=FileSystemStorage()
    filePathname1=fs1.save(p.name,p);
    filePathname1=fs1.url(filePathname)
    context={'filePathname1':filePathname1}
    return render(request, 'App/pneout.html',context)
def upload2(request):#Malaria
    p2 = request.FILES['image'];
    fs2=FileSystemStorage()
    filePathname2=fs2.save(p2.name,p2);
    filePathname2=fs2.url(filePathname2)
    testimage='.'+filePathname2
    img=image.load_img(testimage,target_size=(img_height,img_width))
    x=image.img_to_array(img)
    #x=np.array(img)
    #x=x/255;
    x=x.reshape(1,img_height,img_width,3)
    ans=model.predict(x)
    if(ans[0][0]>ans[0][1]):
        ans='Infected'
    else:
        ans='Uninfected'
    #ans='Infected'
    context={'filepathname2':filePathname2,'pred2':ans}
    return render(request, 'App/malout.html',context)




