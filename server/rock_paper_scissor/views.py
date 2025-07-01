from django.shortcuts import render
import random

def rps_game(request):
    result = ''
    user_choice = ''
    computer_choice = ''
    
    if request.method == 'POST':
        user_choice = request.POST.get('choice')
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        if user_choice == computer_choice:
            result = "It's a draw!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            result = "You win!"
        else:
            result = "You lose!"

    return render(request, 'index.html', {
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result
    })
