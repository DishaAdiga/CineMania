# CineMania
A personal movie recommendation website developed using Django.<br>
A content filtering based algorithm is used to recommend unwatched movies based on the history of watched movies.<br>
The similarity between watched and unwatched movies is calculated using Jaccard Similarity.<br>
Jaccard similarity is given by (size of intersection of 2 sets)/(size of union of 2 sets). In this case, the 2 sets are the genres of watched and unwatched movies.<br>
More the intersection value, more is the similarity.<br>

# Working
1. Load the csv file containing a list of movies into the database.
2. Login to the Django admin panel and mark a few movies as 'watched' based on your preferences thus creating a watched movie history.
3. Run the python manage.py make_recommendations command to obtain the recommendations for unwatched movies.
