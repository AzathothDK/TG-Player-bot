"""Оператор удаления плейлиста из базы данных"""
from telegram import Update, ParseMode
from telegram.ext import CallbackContext

from db.schemas import delete_playlist


def delete_playlist(update: Update, context: CallbackContext):
    playlist_name = update.message.text
    deleted = delete_playlist(playlist_name)
    if deleted:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Плейлист {playlist_name} успешно удален.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Плейлиста {playlist_name} не существует.")
