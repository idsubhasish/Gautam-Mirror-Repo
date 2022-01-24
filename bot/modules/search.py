from quoters import Quote
from telegram.ext import CommandHandler
from bot.search.gdriveTools import GoogleDriveHelper
from bot import LOGGER, dispatcher
from bot.helper.telegram_helper.message_utils import sendMessage, editMessage
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands


def list_recursive(update,context):
    try:
        search = update.message.text.split(' ',maxsplit=1)[1]
    except IndexError:
        sendMessage(f'<b><i>Send A Keyword Along With Search Command</i></b>\n\n<b>Example:-</b><code> /search Avengers </code>', context.bot, update)
        return
    
    quo_te = Quote.print()    
    reply = sendMessage(f'<b>Searching...🔎</b> \n\n<b>{quo_te}</b>', context.bot, update)

    LOGGER.info(f"Searching: {search}")
        
    gdrive = GoogleDriveHelper(None)
    msg, button = gdrive.drive_list(search)

    editMessage(msg,reply,button)





search_handler = CommandHandler(BotCommands.SearchCommand, list_recursive,filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)

dispatcher.add_handler(search_handler)
