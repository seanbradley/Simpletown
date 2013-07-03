from django.views.generic.base import TemplateView

class IndexView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        #context['model_attribute'] = Model.objects.all()[:5]
        return context
