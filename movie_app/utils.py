# movie_app/utils.py

# Python
from collections import Counter

def get_top_genres(queryset):
    '''Return Top 3 favorite genres'''

    if queryset:
        # Count the occurrences of each genre
        genre_counts     = Counter(queryset)

        # Count the occurrences of each genre
        favourite_genres = [ genre for genre, _ in genre_counts.most_common(3) ]

        return favourite_genres

    return []

def prepare_response( user_collections, favourite_genres):
    '''Prepare response for views'''

    response = { 
        'is_success' : True,
        'data' : {
            'collections' : user_collections
        },
        'favourite_genres' : favourite_genres
    }

    return response
