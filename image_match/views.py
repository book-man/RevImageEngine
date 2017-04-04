# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import generic


from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render

from django.views import generic
from .forms import UploadFileForm
from .response import JSONResponse, response_mimetype
from .models import UploadedImage
# Create your views here.

# class ImageCreateView(generic.CreateView):
#     model = UploadedImage
#     fields = '__all__'
    
#     def form_valid(self,form):
#         self.object = form.save()
#         data = {'status':'success'}
#         response = JSONResponse(data,mimetype=response_mimetype(self.request))
#         return response

def home(request):
    print("Request method has been called")
    print("Request method: %s"%request.method)
    if request.method=='POST':
        print('request method is POST')
        form = UploadFileForm(request.POST,request.FILES)
        print request
        if form.is_valid():
            print("form is valid")
            #print(form.cleaned_data.file)
            new_file = UploadedImage(up_file=request.FILES['file'])
            new_file.save()
            print("form saved")
            return HttpResponseRedirect(reverse('image_match:home'))#reverse('image_match:home'))
    else:
        print('request method is not POST')
        form = UploadFileForm()

    data = {'form':form}
    return render(request,'image_match/image_form.html',data )
    # return render_to_response('image_match/index.html',data,context=RequestContext(request))


def thanks(request):
    return HttpResponse("Thank you!")

# class UploadView(generic.TemplateView):
#     template_name = 'image_engine/upload.html'

# class MatchesView(generic.TemplateView):
#     template_name = 'image_engine/matches.html'













