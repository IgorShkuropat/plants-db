from django.shortcuts import render
from .models import Company
from django.views.generic import TemplateView, ListView
from django.db.models import Q

# Create your views here.


def index(request):
    companys = Company.objects.all()
    context = {'index': companys}
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


class SearchResultsView(ListView):
    model = Company
    template_name = 'main/search_result.html'
    queryset = Company.objects.filter(ur_lico__icontains='')

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Company.objects.filter(Q(ur_lico__icontains=query))
        return object_list

