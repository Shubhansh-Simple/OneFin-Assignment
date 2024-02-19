# movie_app/utils.py

def prepare_response( user_collections, favourite_genres):
    '''Prepare Response for Views'''

    response = { 
        'is_success' : True,
        'data' : {
            'collections' : user_collections
        },
        'favourite_genres' : favourite_genres
    }
    return response


