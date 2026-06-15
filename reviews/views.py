from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
class ThankView(TemplateView):
    template_name = "reviews/thank.html" 

    def get_context_data(self, **kwargs):        
        context =  super().get_context_data(**kwargs)
        context['message'] = "this works!"
        return context


class ReviewView(CreateView):
    template_name = "reviews/index.html"
    form_class = ReviewForm
    success_url = "/thank"
    

class ReviewListView(ListView):
    template_name = "reviews/list.html"
    model = Review
    

class DetailView(DetailView):
    template_name = "reviews/detail.html"
    model = Review
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object        
        request = self.request        
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)                
        return context
    

    
class AddFavorite(View):
    def post(self, request):
        review_id = request.POST['review_id']        
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/list/" + review_id)

