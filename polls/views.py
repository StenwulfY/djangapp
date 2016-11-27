from django.http import HttpResponse
# Import Question and Choice from our models file
from .models import Question, Choice
# 6 Renders a page when it is passed a template and
# any data required by the template
from django.shortcuts import render
# 7 Opens a 404 page if get doesn't supply a result
from django.shortcuts import get_object_or_404
# 9 Used to avoid receiving data twice from a form if the user
# clicks the back button
from django.http import HttpResponseRedirect
# 9 Used to return a url we can point to based on the
# current question we are dealing with
from django.core.urlresolvers import reverse
# Generic view
from django.views import generic
# Create your views here.
# 2 Each view is represented by a function
# We'll create :
# index : Display the latest questions
# detail : Display the question and the choices
# results : Display question results
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
 
#     # 6 Define the name for the data to pass to the template
#     context = {
#         'latest_question_list': latest_question_list,
#     }
 
#     # 6 Render the page in the browser using the template
#     # and data required by the template
#     return render(request, 'polls/index.html', context)
# Using generic view 
class IndexView(generic.ListView):
    # point to the template we're gonna use for this list
    template_name = 'polls/index.html'
    # question list we're gonna user
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
# a view represented by a function
# results() to show voting results
# def results(request, question_id):

#     # 10 Get the question id passed or 404
#     question = get_object_or_404(Question, pk=question_id)

#     # 10 Render the template
#     return render(request, 'polls/results.html', {'question': question})
#     Using generic view
class ResultsView(generic.DetailView):
    # define the model we're using
    model = Question
    # define the template using 
    template_name = 'polls/results.html'
# def detail(request, question_id):
#     # 7 Check if the page exists, or display 404 page
#     question = get_object_or_404(Question, pk=question_id)
    
#     return render(request, 'polls/detail.html', {'question': question})
# Using generic viw
class DetailView(generic.DetailView):
    # define the model we're using
    model = Question
    # define the template using 
    template_name = 'polls/detail.html'
# 9 Now we will update vote() to except the choice picked

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # 9 Try to get the selected radio button
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except(KeyError, Choice.DoesNotExist):

        # 9 Re-render the form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:

        # 9 If a choice was selected increment it in the DB
        selected_choice.votes += 1
        selected_choice.save()

        # 9 Protect from data being sent twice if user clicks back
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
