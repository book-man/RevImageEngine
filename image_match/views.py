# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import generic


# from django.http import HttpResponseRedirect
# from django.template import RequestContext
# from django.core.urlsresolvers import reverse
# from django.shortcuts import render_to_response

from django.views import generic
from .models import Image
from .response import JSONResponse, response_mimetype

# Create your views here.

class ImageCreateView(generic.CreateView):
    model = Image
    fields = '__all__'
    
    def form_valid(self,form):
        self.object = form.save()
        data = {'status':'success'}
        response = JSONResponse(data,mimetype=response_mimetype(self.request))
        return response



# def home(request):
#     if request.method=='POST':
#         form = UploadFileForm(request.POST,request.FILES)
#         if form.is_valid():
#             new_file = UploadFile(file=request.FILES['file'])
#             new_file.save()

#             return HttpResponseRedirect(reverse('image_match:home'))
#     else:
#         form = UploadFileForm()

#     data = {'form':form}
#     return render_to_response('image_match/index.html',data,context_instance=RequestContext(request))

# class UploadView(generic.TemplateView):
#     template_name = 'image_engine/upload.html'

# class MatchesView(generic.TemplateView):
#     template_name = 'image_engine/matches.html'













