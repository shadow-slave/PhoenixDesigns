from django.conf import settings
from django.shortcuts import render,redirect
import os
# Create your views here.
def indexview(request):
    return render(request,'index.html')

def galleryview(request):
    images_path=os.path.join('User_App','static','images','folio')
    # image_files= [f for f in os.listdir(images_path) if f.endswith('jpg')]
    # image_urls= ['images/gallery/' + f for f in image_files]
    # context ={
    #     "image_urls":image_urls
    # }
    # print(context
    image_list = [filename for filename in os.listdir(images_path) if filename.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    # print(image_list)
    return render(request, 'gallery.html', {'images': image_list})
    # return render(request,'gallery.html' ,context)

