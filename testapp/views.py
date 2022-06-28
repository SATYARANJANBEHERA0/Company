from django.shortcuts import render
from testapp.models import Company
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
class CompanyListView(ListView):
    model = Company
    # default template file comany_list.html
    # default context object company_list
class CompanyDetailView(DetailView):
    model = Company
class CompanyCreateView(CreateView):
    model = Company
    fields = '__all__'
class CompanyUpdateView(UpdateView):
    model = Company
    fields = ('location','ceo')
class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('list')
