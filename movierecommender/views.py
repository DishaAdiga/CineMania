# Create your views here.
from . import views
from .models import Movie
from django.shortcuts import render

def movie_recommendation_view(request):
    if request.method == "GET":
      # The context/data to be presented in the HTML template
      context = generate_movies()

      # Render a HTML page with specified template and context
      return render(request, 'movierecommender/movie_list.html', context)

#display records from database in the html page
def generate_movies():
    #1.Show only movies in recommendation list
    #2. Sort by votes descending
    #3. Get count of recommendations
    context={}
    recommended_count = Movie.objects.filter(recommended='True').count()
    if (recommended_count==0):
        #Display top voted and unwatched movies
        #get the top 30 ones
        movies=Movie.objects.filter(watched='False').order_by('-vote_count')[:30]
    else:
        #Display top voted,unwatched,recommended movies
        movies=Movie.objects.filter(watched='False').filter(recommended='True').order_by('-vote_count')[:30]
    context['movie_list']=movies
    return context