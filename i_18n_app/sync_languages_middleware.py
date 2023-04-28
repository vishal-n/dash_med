from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from i_18n_app.views import sync_languages_to_db

class SyncLanguagesMiddleware:
    def __init__(self, get_response, request):
        self.get_response = get_response
        self.sync_languages_view(request)
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def sync_languages_view(self, request):
        print("Inside sync languages middleware execution")
        sync_languages_to_db(request)
