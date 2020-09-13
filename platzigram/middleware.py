""" Platzigram Middleware catalog """


# Django imports
from django.shortcuts import redirect
from django.urls import reverse





class ProfileCompletionMiddleware:
    """ Profile completion Middleware

        Ensure every user that is interacting with the plataform 
        have their profile picture and biography
    """





    def __init__(self, get_response):
        """ Middleware Inicialization """
        self.get_response = get_response
        self.routes = [reverse("feed"), reverse("login")]

    def __call__(self, request):
        """Code to be executed for each reponse before the view router is
        called
        """

        print(request.path)

        if not request.user.is_anonymous:
            profile = request.user.profile
            
            if not profile.picture or not profile.biography:
                # validating that its not the same url so we can redirect
                # correctly 
                if request.path in self.routes:
                    return redirect("update_profile")

        response = self.get_response(request)
        return response
