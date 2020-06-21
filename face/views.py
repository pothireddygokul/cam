from django.http import HttpResponse
from django.conf import settings

from django.shortcuts import render, redirect
from django.contrib import messages


import cv2


def index(request):
    #x="C:/Users/pothi/Desktop/host/face/templates/"
    print(1)
    x=str(settings.SETTINGS_PATH)
    print(x)
    return render(request,x+'\\face\\templates\\index.html')


def fun(request):


    
    stream = cv2.VideoCapture(0)
   
    # loop over frames from the video file stream
    while True:
        # grab the frame from the threaded video file stream
        (grabbed, frame) = stream.read()
        # if the frame was not grabbed, then we have reached the end
        # of the stream
        if not grabbed:
            break
        
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):break
        cv2.waitKey(1)
    
    
    stream.release()
    cv2.destroyAllWindows()
    
    return redirect('/')