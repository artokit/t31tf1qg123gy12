from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_keyboard(func):
    def wrapper():
        keyboard = InlineKeyboardBuilder()
        func(keyboard)
        return keyboard.as_markup()

    return wrapper


@create_keyboard
def start(keyboard: InlineKeyboardBuilder):
    keyboard.row(InlineKeyboardButton(text='Получить бота ', url='https://t.me/ramazanakaev_avi'))
    keyboard.row(InlineKeyboardButton(text='Отзывы', callback_data='get_comments'))


@create_keyboard
def end(keyboard: InlineKeyboardBuilder):
    keyboard.row(InlineKeyboardButton(text='Начать работать!', url='https://t.me/ramazanakaev_avi'))


admins = InlineKeyboardBuilder()
admins.row(InlineKeyboardButton(text="Начать рассылку", callback_data='start_sender'))
admins.row(InlineKeyboardButton(text="Получить статистику", callback_data='get_stat'))


note_or_video = InlineKeyboardBuilder()
note_or_video.row(InlineKeyboardButton(text="Видео", callback_data="admin_sender_choice:video"))
note_or_video.row(InlineKeyboardButton(text="Кружок", callback_data="admin_sender_choice:video_note"))


start_sender_or_not = InlineKeyboardBuilder()
start_sender_or_not.row(InlineKeyboardButton(text="✅", callback_data="sender_start:yes"))
start_sender_or_not.row(InlineKeyboardButton(text="❌", callback_data="sender_start:no"))


type_of_push = InlineKeyboardBuilder()
type_of_push.row(InlineKeyboardButton(text="Мгновенный пуш", callback_data="instant_push"))
# type_of_push.row(InlineKeyboardButton(text="Ежедневный пуш", callback_data="every_day_push"))
# type_of_push.row(InlineKeyboardButton(text="Отложенный пуш", callback_data="time_push"))


sender_example_urls = InlineKeyboardBuilder()
sender_example_urls.row(InlineKeyboardButton(text="🔥 Стратегия 🔥", url='https://example.com'))
sender_example_urls.row(InlineKeyboardButton(text="💰 Лучшие выигрыши 💰", url='https://example1.com'))

no_buttons = InlineKeyboardBuilder()
no_buttons.row(InlineKeyboardButton(text="В этой рассылке не нужны кнопки", callback_data="no_buttons"))