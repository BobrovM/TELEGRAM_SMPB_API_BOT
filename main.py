import logging
import os

import telegram as t
import telegram.ext as te


logger = logging.getLogger(__name__)


async def start(update: t.Update, context: te.ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=t.ForceReply(selective=True)
    )


async def help_command(update: t.Update, context: te.ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Help!")


async def echo(update: t.Update, context: te.ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)


def main():
    application = te.Application.builder().token(os.getenv("TG_SMPB_API_BOT_TOKEN")).build()

    application.add_handler(te.CommandHandler("start", start))
    application.add_handler(te.CommandHandler("help", help_command))

    application.add_handler(te.MessageHandler(te.filters.TEXT & ~te.filters.COMMAND, echo))

    application.run_polling()


if __name__ == "__main__":
    main()