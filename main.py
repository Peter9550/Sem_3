import telebot
from telebot import types

API_TOKEN = '7364578875:AAErqghKrEmco4UHt7rNqKBLJBnKswTF66w'

bot = telebot.TeleBot(API_TOKEN)

class Task:

    def __init__(self, text):
        self.text = text
        self.is_done = False

    def mark_done(self):
        self.is_done = True

    def __str__(self):
        status = "✅" if self.is_done else "⬜"
        return f"{status} {self.text}"


class UrgentTask(Task):

    def __init__(self, text):
        super().__init__(text)

    def __str__(self):

        status = "✅" if self.is_done else "🔥"
        return f"{status} ВАЖНО: {self.text.upper()} !!!"


class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, text, is_urgent=False):
        if is_urgent:
            new_task = UrgentTask(text)
        else:
            new_task = Task(text)
        self.tasks.append(new_task)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            return True
        return False

    def get_all_tasks_text(self):
        if not self.tasks:
            return "Список задач пуст! Отдыхайте 🌴"

        result = "Ваши дела:\n"
        for i, task in enumerate(self.tasks):
            result += f"{i + 1}. {task}\n"
        return result

    def is_empty(self):
        return len(self.tasks) == 0


user_managers = {}

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("📝 Добавить задачу")
    btn2 = types.KeyboardButton("🔥 Добавить СРОЧНУЮ")
    btn3 = types.KeyboardButton("📋 Показать список")
    btn4 = types.KeyboardButton("🗑 Удалить задачу")
    markup.add(btn1, btn2, btn3, btn4)
    return markup


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    if chat_id not in user_managers:
        user_managers[chat_id] = TaskManager()

    bot.send_message(chat_id,
                     "Привет! Я Smart To-Do Bot.\nЯ помогу организовать твои дела.",
                     reply_markup=main_menu())


@bot.message_handler(func=lambda m: m.text == "📝 Добавить задачу")
def ask_normal_task(message):
    msg = bot.send_message(message.chat.id, "Напишите текст задачи:", reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, save_normal_task)


def save_normal_task(message):
    chat_id = message.chat.id
    text = message.text
    if chat_id not in user_managers: user_managers[chat_id] = TaskManager()

    user_managers[chat_id].add_task(text, is_urgent=False)
    bot.send_message(chat_id, f"Задача '{text}' добавлена!", reply_markup=main_menu())


@bot.message_handler(func=lambda m: m.text == "🔥 Добавить СРОЧНУЮ")
def ask_urgent_task(message):
    msg = bot.send_message(message.chat.id, "Напишите текст СРОЧНОЙ задачи:", reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, save_urgent_task)


def save_urgent_task(message):
    chat_id = message.chat.id
    text = message.text
    if chat_id not in user_managers: user_managers[chat_id] = TaskManager()

    user_managers[chat_id].add_task(text, is_urgent=True)
    bot.send_message(chat_id, f"Срочная задача '{text}' добавлена!", reply_markup=main_menu())


@bot.message_handler(func=lambda m: m.text == "📋 Показать список")
def show_tasks(message):
    chat_id = message.chat.id
    if chat_id not in user_managers: user_managers[chat_id] = TaskManager()

    text_report = user_managers[chat_id].get_all_tasks_text()
    bot.send_message(chat_id, text_report)


@bot.message_handler(func=lambda m: m.text == "🗑 Удалить задачу")
def delete_task_start(message):
    chat_id = message.chat.id
    if chat_id not in user_managers: user_managers[chat_id] = TaskManager()
    manager = user_managers[chat_id]

    if manager.is_empty():
        bot.send_message(chat_id, "Список пуст, удалять нечего.", reply_markup=main_menu())
        return

    text_report = manager.get_all_tasks_text()
    msg = bot.send_message(chat_id, text_report + "\n\nВведите НОМЕР задачи, которую нужно удалить:",
                           reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, delete_task_finish)


def delete_task_finish(message):
    chat_id = message.chat.id
    manager = user_managers.get(chat_id)

    try:
        index = int(message.text) - 1
        success = manager.delete_task(index)

        if success:
            bot.send_message(chat_id, "Задача удалена!", reply_markup=main_menu())
        else:
            bot.send_message(chat_id, "Неверный номер задачи.", reply_markup=main_menu())
    except ValueError:
        bot.send_message(chat_id, "Нужно ввести число.", reply_markup=main_menu())

if __name__ == '__main__':
    print("Бот Smart To-Do запущен...")
    bot.infinity_polling()
