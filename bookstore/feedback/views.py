from django.shortcuts import redirect, render

from feedback.forms import FeedbackForm


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_sent')
        return render(request, 'feedback_form.html', {'form': form})

    form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})


def feedback_sent(request):
    return render(request, 'feedback_sent.html')
