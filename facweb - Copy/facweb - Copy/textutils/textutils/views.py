# #i have created this file - yash chandramore
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse('''<h1>hello aamir khan</h1> <a href = "https://www.google.com/search?q=aamir+khan&oq=aamir+khan&aqs=chrome..69i57j0i271l2.2454j0j15&sourceid=chrome&ie=UTF-8"> AAMIR KHAN</a>>''') 

# def about(request):
#     return HttpResponse("hello aamir khan sahab") 
def ex1(request):
    s =''' "<h2>PLAYLIST<br></h2>
        <a href = "https://www.youtube.com/watch?v=H9auXrVEQSM">BHEED TRAILER </a><br>
        <a href = "https://youtube.com/watch?v=eYR4lKEZB9U&feature=shares">tere hawalwe </a><br>
       '''
    return HttpResponse(s)
def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = (request.POST.get('text','default'))
    print(djtext)
    
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    # print(removepunc)
    if removepunc == "on":
        print(djtext)
    # analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params  = {'purpose':'Removedons' , 'analyzed_text' : analyzed , 'tests': djtext}
        return render(request,'analyze.html', params)
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        
        params  = {'purpose':'uppercase' , 'analyzed_text' : analyzed}
        return render(request,'analyze.html', params)
    # elif(removepunc=="on" and fullcaps =="on"):
    #     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    #     analyzed = ""
    #     for char in djtext:
    #         if char not in punctuations:
    #             analyzed = analyzed + char

    #     params  = {'purpose':'Removedons' , 'analyzed_text' : analyzed}
    #     return render(request,'analyze.html', params)
        

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        
        params  = {'purpose':'newlineremove' , 'analyzed_text' : analyzed}
        return render(request,'analyze.html', params)
    
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        
        params  = {'purpose':'extraspaceremover' , 'analyzed_text' : analyzed}
        return render(request,'analyze.html', params)
        


      
            
    else:
        return HttpResponse("error")




