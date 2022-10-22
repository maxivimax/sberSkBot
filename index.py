import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
# from quizzes import quizzes

forTinder = [
    ["***Финансовая грамотность*** \nИз-за невежества в сфере экономики и денег люди часто не в состоянии обеспечить себе достойную жизнь даже при хорошей зарплате. К тому же нашей финансовой безграмотностью часто пользуются другие люди, что приводит к печальным последствиям. Именно по этим двум причинам стоит изучать основы финансовой грамотности.", 
    "*Полная статья 1*", 
    [
        [
            "Ты прочитал статью?", 
            [
                "Да", 
                "Нет"
            ],
            0
        ],
        [
            "Ты точно прочитал статью?", 
            [
                "Да", 
                "Нет"
            ],
            0
        ],
    ]
    ],
    ["***Финансовая грамотность*** \nЭто совокупность знаний, навыков и установок в сфере финансового поведения человека, ведущих к улучшению благосостояния и повышению качества жизни.",
    "*Полная статья 2*", 
    [
        [
            "Ты прочитал статью 2?", 
            [
                "Да", 
                "Нет"
            ],
            0
        ],
        [
            "Ты точно прочитал статью 2?", 
            [
                "Да", 
                "Нет"
            ],
            0
        ],
        [
            "Ты точно точно прочитал статью 2?", 
            [
                "Да", 
                "Нет"
            ],
            0
        ],
    ]
    ]
]
statStar = 0
quizStar = 0

button_hi = InlineKeyboardButton('Привет! 👋', callback_data='helloo')
firstb = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
firstb.add(button_hi)

button_IS = InlineKeyboardButton('Финансовая грамотность', callback_data='IS')
button_PH = InlineKeyboardButton('Placeholder', callback_data='ph')
what = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
what.add(button_IS)
what.add(button_PH)

button_back = InlineKeyboardButton('Назад', callback_data='helloo')
back = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
back.add(button_back)

button_quiz = InlineKeyboardButton('Задания к статье', callback_data='quiz')
backS = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
backS.add(button_quiz)
backS.add(button_back)

button_like = InlineKeyboardButton('Прочитать полностью', callback_data='like')
button_disl = InlineKeyboardButton('Не интерестно', callback_data='dislike')
tinder = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
tinder.add(button_like)
tinder.add(button_disl)

API_TOKEN = '5796845106:AAHhiD-thzIkWBtlDvz75M4QZx93cV3bJZs'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def quiz(quest, options, correct_option_id, message):
    return bot.send_poll(chat_id=message.from_user.id,
                              question=quest,
                              options=options,
                              type='quiz',
                              correct_option_id=correct_option_id,
                              is_anonymous=False)

def quizPoll(quest, options, correct_option_id, userid):
    return bot.send_poll(chat_id=userid,
                              question=quest,
                              options=options,
                              type='quiz',
                              correct_option_id=correct_option_id,
                              is_anonymous=False)

@dp.message_handler(commands=['start', 'help'])
async def cmd_start(message: types.Message):
    await message.reply("Привет, я Олеша! И я расскажу тебе всё о финансовой грамотности, но не только расскажу, но и позадаю вопросы!", reply_markup=firstb)

@dp.message_handler(commands=["quiz"])
async def poll(message: types.Message):
    await quiz("hjkl;", ["lf", "yrn", "gbplf"], 1, message)

@dp.poll_answer_handler()
async def poll_answer(poll_answer: types.PollAnswer):
    answer_ids = poll_answer.option_ids
    
    user_id = poll_answer.user.id
    poll_id = poll_answer.poll_id
    global statStar
    global quizStar

    if (forTinder[statStar][2][quizStar-1][2] not in answer_ids):
        await bot.send_message(user_id, f"""Неверно :(""")
        if quizStar < len(forTinder[statStar][2]):
            await quizPoll(forTinder[statStar][2][quizStar][0], forTinder[statStar][2][quizStar][1], forTinder[statStar][2][quizStar][2], user_id)
            quizStar = quizStar + 1
        else:
            await bot.send_message(user_id, 'Ты всё выполнил!\nЧто будем делать дальше?', reply_markup=what, parse_mode='markdown')
            quizStar = 0
    else:
        await bot.send_message(user_id, f"""Верно!""")
        if quizStar < len(forTinder[statStar][2]):
            await quizPoll(forTinder[statStar][2][quizStar][0], forTinder[statStar][2][quizStar][1], forTinder[statStar][2][quizStar][2], user_id)
            quizStar = quizStar + 1
        else:
            await bot.send_message(user_id, 'Ты всё выполнил!\nЧто будем делать дальше?', reply_markup=what, parse_mode='markdown')
            quizStar = 0

@dp.callback_query_handler(lambda c: c.data == 'helloo')
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Чему ты хочешь научиться ***сегодня***?', reply_markup=what, parse_mode='markdown')

@dp.callback_query_handler(lambda c: c.data == 'IS')
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, forTinder[statStar][0], reply_markup=tinder, parse_mode='markdown')

@dp.callback_query_handler(lambda c: c.data == 'ph')
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Тут что-то будет :)', reply_markup=back, parse_mode='markdown')

@dp.callback_query_handler(lambda c: c.data == 'like')
async def process_callback_button(callback_query: types.CallbackQuery):
    global statStar
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, forTinder[statStar][1], reply_markup=backS, parse_mode='markdown')

@dp.callback_query_handler(lambda c: c.data == 'quiz')
async def process_callback_button(callback_query: types.CallbackQuery):
    global statStar
    global quizStar
    await bot.answer_callback_query(callback_query.id)
    await quiz(forTinder[statStar][2][quizStar][0], forTinder[statStar][2][quizStar][1], forTinder[statStar][2][quizStar][2], callback_query)
    quizStar = quizStar + 1

@dp.callback_query_handler(lambda c: c.data == 'dislike')
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    global statStar
    if statStar < len(forTinder) - 1: 
        statStar = statStar + 1
        await bot.send_message(callback_query.from_user.id, forTinder[statStar][0], reply_markup=tinder, parse_mode='markdown')
    else:
        statStar = 0
        await bot.send_message(callback_query.from_user.id, "Пока больше нет статей.", reply_markup=back, parse_mode='markdown')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)