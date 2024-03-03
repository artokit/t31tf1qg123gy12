import asyncio

from aiogram import Router, F
from aiogram.filters import Command, ChatMemberUpdatedFilter, KICKED
from aiogram.types import Message, CallbackQuery, ChatMemberUpdated

import keyboards
import utils
from database.models import Stat, User

router = Router()


@router.message(Command('start'))
async def start(message: Message):
    is_new_user = User.add_user(message.chat.id, message.chat.username)
    if is_new_user:
        Stat.increment_stat()

    await utils.send_photo(
        message.bot,
        message.chat.id,
        'start.png',
        caption='👋Всем привет, вы наверное меня видели, меня зовут Рамазан Акаев!\n\n'
                '🚀У меня есть бот который выдает точные сигналы в игре Aviator. Я готов поделиться этим ботом с вами.\n\n'
                '❓Но вы можете спросить, почему я это делаю❓ Потому что, чем больше людей будет использовать этого бота, тем большее количество сигналов он будет давать.\n\n'
                'Хочу отметить, этот бот БЕСПЛАТНЫЙ!✅\n'
                'Моя выгода в том, что вы даете мне процент после того как вы получили прибыль!\n\n'
                '🤑Зарабатывать в день 100.000 тг, это не предел!\n'
                'Пиши мне и начнем зарабатывать вместе!💪',
        reply_markup=keyboards.start()
    )


@router.callback_query(F.data == 'get_comments')
async def get_comments(call: CallbackQuery):
    await call.message.answer(
        'Я понимаю что ты не понимаешь почему я помогаю другим, но поверь, как только ты заработаешь больше 100 тысяч тенге, а ты можешь сделать это уже сегодня, то твои 25% которые ты скинешь мне, будут кормить меня еще очень долго😎\n\n'
        'Лови отзывы👇'
    )

    await asyncio.sleep(1)
    await utils.send_photo(call.bot, call.message.chat.id, '1.png')
    await asyncio.sleep(0.5)
    await utils.send_photo(call.bot, call.message.chat.id, '2.png')
    await asyncio.sleep(0.5)
    await utils.send_photo(call.bot, call.message.chat.id, '3.png', caption='Вот отзыв тех, кто уже поднял деньги вместе со мной, а на их месте можешь быть ты.')

    await asyncio.sleep(1)

    await call.message.answer(
        'Как ты видишь, я работаю честно, ведь чем больше заработаешь ты - тем больше заработаю и я💰\n\n'
        'Пиши мне и начинай работу уже сейчас',
        reply_markup=keyboards.end()
    )


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def check_bot(event: ChatMemberUpdated):
    Stat.add_block_user(event.chat.id)
