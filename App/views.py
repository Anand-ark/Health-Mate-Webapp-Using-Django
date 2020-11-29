from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
import numpy as np
from PIL import Image
from keras.models import load_model
from keras.preprocessing import image
import joblib
from sklearn.ensemble import RandomForestClassifier

import tensorflow as tf
model =load_model('./models/malaria_detection.h5')
dmodel=joblib.load('./models/diabetes_model.sav')
hmodel=joblib.load('./models/heart_model.sav')
cmodel=load_model('./models/covid_Xray_lungs_detection.h5')

img_height1,img_width1=150,150 #covid
img_height2,img_width2=128,128 # malaria
def index(request):
    return render(request,'App/index.html',{})

def about(request):
    #return HttpResponse('<h1>Welcome </h1>')
    return render(request, 'App/about.html')
def contact(request):
    return render(request, 'App/contact.html')
def diabetes(request):
    return render(request, 'App/diabetes.html')
def heart(request):
    return render(request, 'App/heart.html')
#def skin(request):
 #   return render(request, 'App/skin.html')
def malariaa(request):
    return render(request, 'App/malariaa.html')
def covid(request):
    return render(request, 'App/covid.html')
def predict(request):
    lis = []
    lis.append(int(request.GET['Pregnancies']))
    lis.append(int(request.GET['Glucose']))
    lis.append(int(request.GET['BloodPressure']))
    lis.append(int(request.GET['SkinThickness']))
    lis.append(int(request.GET['Insulin']))
    lis.append(float(request.GET['BMI']))
    lis.append(float(request.GET['DiabetesPedigreeFunction']))
    lis.append(int(request.GET['Age']))
    N = [np.array(lis)]

    pred = dmodel.predict(N)
    if(pred==1):
        pred='Congrats ! You Are Healthy'
    else:
        pred='Alas ! You Are Unhealthy '
    return render(request, 'App/diabetes.html', {'pred':pred})
def hpredict(request):
    liss = []
    liss.append(int(request.GET['age']))
    liss.append(int(request.GET['sex']))
    liss.append(int(request.GET['cp']))
    liss.append(int(request.GET['trestbps']))
    liss.append(int(request.GET['chol']))
    liss.append(int(request.GET['fbs']))
    liss.append(int(request.GET['restecg']))
    liss.append(int(request.GET['thalach']))
    liss.append(int(request.GET['exang']))
    liss.append(float(request.GET['oldpeak']))
    liss.append(int(request.GET['slope']))
    liss.append(int(request.GET['ca']))
    liss.append(int(request.GET['thal']))
    h = [np.array(liss)]

    predh = hmodel.predict(h)
    if(predh==0):
       predh='Congrats ! You Are Safe'
    else:
       predh='Alas ! You Are Not Safe '
    return render(request, 'App/heart.html', {'predh':predh})
def upload1(request):#Covid
    p1 = request.FILES['image'];
    fs1=FileSystemStorage()
    filePathname1=fs1.save(p1.name,p1);
    filePathname1=fs1.url(filePathname1)
    testimage='.'+filePathname1
    img=image.load_img(testimage,target_size=(img_height1,img_width1))
    x=image.img_to_array(img)
    x=np.array(img)
    x=x/255;
    x=x.reshape(1,img_height1,img_width1,3)
    ans=cmodel.predict(x)
    if(ans[0][0]>ans[0][1]):
       ans='COVID POSITIVE DETECTED'
    else:
        ans='COVID NEGATIVE DETECTED'
    context={'filepathname1':filePathname1,'pred1':ans}
    return render(request, 'App/covidout.html',context)
def upload2(request):#Malaria
    p2 = request.FILES['image'];
    fs2=FileSystemStorage()
    filePathname2=fs2.save(p2.name,p2);
    filePathname2=fs2.url(filePathname2)
    testimage='.'+filePathname2
    img=image.load_img(testimage,target_size=(img_height2,img_width2))
    x=image.img_to_array(img)
    #x=np.array(img)
    #x=x/255;
    x=x.reshape(1,img_height2,img_width2,3)
    ans=model.predict(x)
    if(ans[0][0]>ans[0][1]):
        ans='Above Cell is Infected'
    else:
        ans='Above Cell is Not Infected'
    #ans='Infected'
    context={'filepathname2':filePathname2,'pred2':ans}
    return render(request, 'App/malout.html',context)




