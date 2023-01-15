import logging
import os

import telegram as t
import telegram.ext as te


logger = logging.getLogger(__name__)

VIDEO_BUTTON = "Video"
IMAGE_BUTTON = "Image"

FIRST_MENU_MARKUP = t.InlineKeyboardMarkup([
    [t.InlineKeyboardButton(VIDEO_BUTTON, callback_data=VIDEO_BUTTON)],
    [t.InlineKeyboardButton(IMAGE_BUTTON, callback_data=IMAGE_BUTTON)]
])


async def start(update: t.Update, context: te.CallbackContext) -> None:
    await context.bot.send_message(
        update.message.from_user.id,
        text="TEXT",
        parse_mode=t.constants.ParseMode.HTML,
        reply_markup=FIRST_MENU_MARKUP
    )


async def button_tap(update: t.Update, context: te.CallbackContext) -> None:
    data = update.callback_query.data
    text = ""
    print(data)

    if data == VIDEO_BUTTON:
        text = VIDEO_BUTTON
    elif data == IMAGE_BUTTON:
        text = IMAGE_BUTTON

    await update.callback_query.answer()

    await context.bot.send_message(
        update.callback_query.from_user.id,
        text=text,
        parse_mode=t.constants.ParseMode.HTML,
        reply_markup=FIRST_MENU_MARKUP
    )


async def help_command(update: t.Update, context: te.ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("WIP!")


async def echo(update: t.Update, context: te.ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)


def main():
    application = te.Application.builder().token(os.getenv("TG_SMPB_API_BOT_TOKEN")).build()

    application.add_handler(te.CommandHandler("start", start))
    application.add_handler(te.CommandHandler("help", help_command))

    application.add_handler(te.MessageHandler(te.filters.TEXT & ~te.filters.COMMAND, echo))

    application.add_handler(te.CallbackQueryHandler(button_tap))

    application.run_polling()


if __name__ == "__main__":
    main()