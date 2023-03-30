"""Оператор добавления трека в плейлист"""
from telegram import Update
from telegram.ext import CallbackContext

from db.schemas import add_track_to_playlist


def add_track(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    message = update.message

    if not message.audio:
        context.bot.send_message(chat_id=chat_id, text="Отправьте аудио файл.")
        return

    playlist_id = context.user_data.get('playlist_id')

    if not playlist_id:
        context.bot.send_message(chat_id=chat_id, text="Сперва нужно выбрать плейлист.")
        return

    track_title = message.audio.title
    track_artist = message.audio.performer
    track_file_id = message.audio.file_id

    add_track_to_playlist(playlist_id, track_title, track_artist, track_file_id)

    context.bot.send_message(chat_id=chat_id, text=f"{track_title} от {track_artist} добавлен в плейлист.")
