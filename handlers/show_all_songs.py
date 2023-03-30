"""Оператор, который выводит все треки из базы данных"""
from telegram import Update
from telegram.ext import CallbackContext
from db.schemas import get_all_songs


def show_all_songs(update: Update, context: CallbackContext):
    songs = get_all_songs()

    if not songs:
        update.message.reply_text(
"""
На данный момент треков нет
Чтобы добавить новый трек, отправьте мне файл в формате mp3.
"""
)
        return

    message = 'Список треков:\n\n'

    for song in songs:
        message += f"{song.id}. {song.title} - {song.artist}\n"

    update.message.reply_text(message)
