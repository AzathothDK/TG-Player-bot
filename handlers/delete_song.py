"""Удаление трека из бд"""
from telegram import Update
from telegram.ext import CallbackContext
from db.schemas import delete_song


def delete_song(update: Update, context: CallbackContext):
    song_id = int(context.args[0])
    delete_song(song_id)
    update.message.reply_text("Трек успешно удален из базы данных.")
