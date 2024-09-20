from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question, Answer

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})

def quiz_detail(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    if request.method == 'POST':
        score = 0
        questions = quiz.questions.all()
        for question in questions:
            selected_answer = request.POST.get(str(question.id))
            if selected_answer:
                answer = Answer.objects.get(id=selected_answer)
                if answer.is_correct:
                    score += 1
        return render(request, 'quiz/result.html', {'quiz': quiz, 'score': score, 'total': questions.count()})
    else:
        return render(request, 'quiz/quiz_detail.html', {'quiz': quiz})
