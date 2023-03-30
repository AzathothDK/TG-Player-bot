"""Оператор добавления трека в базу данных"""
from telegram.ext import MessageHandler, filters
from db.schemas import add_song
from models import Song


def add_song() -> MessageHandler:
    def handler(update, context):
        song = update.message.audio
        if song and song.mime_type ==  'audio/mpeg':
            title = song.title
            artist = song.performer
            file_id = song.file_id

            song.add_song(title=title, artist=artist, file_id=file_id)

            message = f"Трек {title} от {artist} добавлен в базу данных."
            update.message.reply_text(message)
        else:
            message = "Я понимаю только mp3 файлы :("
            update.message.reply_text(message)

    return MessageHandler(filters.AUDIO, handler)