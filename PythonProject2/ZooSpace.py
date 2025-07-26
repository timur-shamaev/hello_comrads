import telebot
from telebot import types

# Ваш токен
TOKEN = '7693141583:AAGaOOSfQFDowMidDUTjfsjgQC1PUQc3Ctk'
bot = telebot.TeleBot(TOKEN)

# Вопросы викторины и ответы
quiz = {
    "Какое самое большое животное на Земле?":
        {
            "answers": ["Синий кит", "Слон", "Акула", "Жираф"],
            "correct_answer": "Синий кит"
        },
    "Сколько ног у осьминога?":
        {
            "answers": ["6", "8", "10", "12"],
            "correct_answer": "8"
        },
    "Как называется детёныш кенгуру?":
        {
            "answers": ["Джо", "Кид", "Пап", "Джо-Джо"],
            "correct_answer": "Джо"
        },
    "Какие современные животные являются прямыми потомками динозавров?":
        {
            "answers": ["Вараны", "Крокодилы", "Драконы", "Птицы"],
            "correct_answer": "Птицы"
        },
    "Какое из этих животных относится к отряду кошкообразных?":
        {
            "answers": ["Северный морской котик", "Тибетская лисица", "Земляной волк", "Малая панда"],
            "correct_answer": "Земляной волк"
        },
    "Наиболее близкие родственники бегемотов это:":
        {
            "answers": ["Китообразные", "Носороговые", "Тапировые", "Свиные"],
            "correct_answer": "Китообразные"
        },
    "Самая громкая птица в мире:":
        {
            "answers": ["Большой белохохлый какаду", "Индийский павлин", "Крикливая сорокопутовая пиха", "Одноусый звонарь"],
            "correct_answer": "Одноусый звонарь"
        },
    "Какое животное может различать 12 основных цветов, воспринимая практически весь видимый спектр — от ультрафиолетовой границы до инфракрасной?":
        {
            "answers": ["Рак-щелкун Альфеус", "Исполинский соплохвост", "Глокая куздра", "Южный гигантский кальмар"],
            "correct_answer": "Рак-щелкун Альфеус"
        },
    "Какое из этих животных самое маленькое?":
        {
            "answers": ["Японский краб паук", "Обыкновенная луна-рыба", "Яванский оленёк", "Гамбийская крыса"],
            "correct_answer": "Яванский оленёк"
        },
    "На кого был похож общий предок обезьяны и человека?":
        {
            "answers": ["На обезьяну", "На человека", "На рептилоида", "На белку"],
            "correct_answer": "На белку"
        },
}

# разные исходы викторины
result = [
    'Не то чтобы ваши знания о животных были совсем плохими, но вам и лабораторную мышь страшно доверить! 🤨🤨🤨',
    'Немного старания, терпения и усердия и вы сможете позаботиться о каком-то редком животном. А пока просто погладьте кота. 😽😽😽',
    'Вы как бурый медведь. Весьма умны и хитры. Как насчёт того, чтобы стать опекуном прекрасного косолапого? 🐻🐻🐻',
    'Ваш разум сияет как шерсть снежного барса! Пожалуй, вы можете стать опекуном одного из этих великолепных созданий. 😍😍😍',
    'Ваши знания могут воскресить мамонта, шерстистого носорога и пару неандертальцев! ❤️❤️❤️'
]

# Словарь для хранения состояния пользователей
user_data = {}

# Функция приветствия
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Давай поиграем? Напиши 'викторина', чтобы начать.")

# Функция обработки команды 'викторина'
@bot.message_handler(func=lambda message: message.text.lower() == 'викторина')
def start_quiz(message):
    user_data[message.chat.id] = {'question_index': 0, 'score': 0}
    ask_question(message)

# Функция для задания вопроса с кнопками
def ask_question(message):
    chat_id = message.chat.id
    question_index = user_data[chat_id]['question_index']
    questions = list(quiz.keys())


    if question_index < len(questions):
        question = questions[question_index]
        options = quiz[question]['answers']


        markup = types.InlineKeyboardMarkup()
        for option in options:
            markup.add(types.InlineKeyboardButton(option, callback_data=option))


        bot.send_message(chat_id, question, reply_markup=markup)
    else:
        score = user_data[chat_id]['score']
        bot.send_message(chat_id, f"Викторина завершена! Ваш результат: {score} из {len(quiz)}")
        if score >= 9:
            bot.send_message(chat_id, f"{result[4]}")
        elif score >= 7:
            bot.send_message(chat_id, f"{result[3]}")
        elif score >= 5:
            bot.send_message(chat_id, f"{result[2]}")
        elif score >= 3:
            bot.send_message(chat_id, f"{result[1]}")
        elif score >= 0:
            bot.send_message(chat_id, f"{result[0]}")
        user_data.pop(chat_id)

# Функция для обработки ответов на вопросы викторины
@bot.callback_query_handler(func=lambda call: True)
def handle_answer(call):
    chat_id = call.message.chat.id
    question_index = user_data[chat_id]['question_index']
    questions = list(quiz.keys())
    question = questions[question_index]
    correct_answer = quiz[question]['correct_answer']


    if call.data == correct_answer:
        user_data[chat_id]['score'] += 1
        bot.answer_callback_query(call.id, "Правильно!")
    else:
        bot.answer_callback_query(call.id, f"Неправильно! Правильный ответ: {correct_answer}")


    user_data[chat_id]['question_index'] += 1
    ask_question(call.message)

# Запуск бота
bot.polling()