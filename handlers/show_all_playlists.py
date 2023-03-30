"""Оператор, который выводит все существующие плейлисты"""
from telegram import Update
from telegram.ext import CallbackContext
from ..db.schemas import get_all_playlists


def show_all_playlists(update: Update, context: CallbackContext):
    playlists = get_all_playlists()
    if not playlists:
        update.message.reply_text('Список плейлистов пуст')
        return

    response = 'Список плейлистов:\n'
    for playlist in playlists:
        response += f"{playlist.id}. {playlist.name}\n"

    update.message.reply_text(response)
