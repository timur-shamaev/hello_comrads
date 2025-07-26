def get_question_by_index(questions, index):
    if index >= 0 and index < len(questions):
        return questions[index]
    else:
        return "Неверный индекс."

# Пример использования функции
questions = ["Какая птица самая большая?", "Какое копытное самое мелкое?", "Какое животное самое ядовитое?"]
index = 2
question = get_question_by_index(questions, index)
print(question)