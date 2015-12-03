from django.views.generic import TemplateView

from apps.genres.models import Genre

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        return context

