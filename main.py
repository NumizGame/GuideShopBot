from aiogram import *
from config import *
from data import *
import asyncio
from aiogram.types.input_file import InputFile


bot = Bot(token, parse_mode='HTML')
disp = Dispatcher(bot)


@disp.message_handler(commands=['start'])
async def start_cmd(message):
    await bot.send_message(message.chat.id, '<b>Добро пожаловать, я бот, специализирующийся на продаже учебных курсов. В появившейся клавиатуре вы можете выбрать нужный вам курс и оплатить его.</b>', reply_markup=main_menu_kb)

    await message.delete()


@disp.message_handler(text='Выбрать курс')
async def choose_guide(message):
    bot_message = await bot.send_message(message.chat.id, '<b>Вот список доступных курсов: </b>', reply_markup=buy_guides_ikb)

    await message.delete()

    await asyncio.sleep(14)
    await bot_message.delete()

# Покупка курса


@disp.callback_query_handler()
async def sending_invoice(callback):
    await bot.send_invoice(callback.message.chat.id,
                           title=guides_data[callback.data]['title'],
                           description=guides_data[callback.data]['desc'],
                           provider_token=payments_token,
                           currency='rub',
                           photo_url=guides_data[callback.data]['photo_url'],
                           photo_height=512,
                           photo_width=512,
                           photo_size=512,
                           is_flexible=False,
                           prices=guides_data[callback.data]['price'],
                           payload=guides_data[callback.data]['payload'])


@disp.pre_checkout_query_handler()
async def pre_checkout(pre_checkout_query):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@disp.message_handler(content_types=ContentTypes.SUCCESSFUL_PAYMENT)
async def successful_payment_handler(message):
    guide_file = InputFile(r'guides_data\ '[:-1] + message.successful_payment.invoice_payload)

    bot_message = await bot.send_message(message.chat.id, '<b>Подождите, в данный момент происходит обработка оплаты. Скоро вы получите файл с курсом.</b>')

    await asyncio.sleep(7)
    await bot_message.delete()

    await bot.send_document(message.chat.id, document=guide_file, caption='<b>Спасибо, что выбрали нас!</b>')

# Техподдержка

@disp.message_handler(text='Связаться с поддержкой')
async def connect_support(message):
    bot_message = await bot.send_message(message.chat.id, '<b>Если у вас появилась какая-то проблема или вопрос, касаемо данного бота, обратитесь в службу техподдержки: https://t.me/ThisIsMyShadow</b>')

    await message.delete()

    await asyncio.sleep(7)
    await bot_message.delete()

if __name__ == '__main__':
    executor.start_polling(disp, skip_updates=True)