from django.shortcuts import render
from django.views.generic.base import View


# Create your views here.
class ExpansionView(View):
    def get(self, request):
        return render(request, template_name='expansionmoniter.html')



