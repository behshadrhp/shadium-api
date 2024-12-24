from django.contrib.auth import logout
from django.views import View
from django.shortcuts import redirect


class LogoutView(View):
    """
    This class is for LogoutView user.
    """

    def get(self, request):
        logout(request)
        return redirect("/")
    
    def post(self, request):
        logout(request)
        return redirect("/")
