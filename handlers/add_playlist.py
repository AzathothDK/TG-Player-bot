"""Оператор добавления плейлиста в бд"""
from telegram import Update
from telegram.ext import CallbackContext

from db.schemas import add_playlist, get_playlist_by_name


def add_playlist(update: Update, context: CallbackContext):
    playlist_name = update.message.text
    playlist = get_playlist_by_name(playlist_name)

    if playlist:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Playlist {playlist_name} already exists!")
    else:
        add_playlist(playlist_name)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Playlist {playlist_name} added successfully")
