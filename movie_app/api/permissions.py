from rest_framework   import permissions
from movie_app.models import Collections

class IsCollectionCreatorLoggedIn(permissions.BasePermission):
    '''Custom permissions which allow only collections creator can view/update their collections'''

    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user

    def has_permission(self, request, view):
        try:
            if view.kwargs.get('pk'):
                return Collections.objects.get(uuid=view.kwargs['pk']).creator == request.user
            return True
        except Exception as e:
            print('Exception - ',e)
            return False
    
