from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.shortcuts import render,get_object_or_404
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import resolve

from questions.models import Answer


# Create your views here.

class DeleteAnswer(DeleteView):
    model = Answer
    success_url="/"
    #success_url = reverse_lazy('user_iscrizioni_list')
    #success_url = reverse_lazy('visualizza_discussione')
    #success_url = reverse_lazy('visualizza_discussione',kwargs={'pk':post.discussione__id})
    template_name = "questions/question_confirm_delete.html"
    context_object_name = 'answer_da_eliminare'

    def get_context_data(self, **kwargs):
            # Call the base implementation first to get the context
            context = super().get_context_data(**kwargs)
            # Create any data and add it to the context
            context['avviso'] = "Confermi di voler eliminare la seguente risposta?"
            return context
