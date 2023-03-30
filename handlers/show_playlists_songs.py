"""Вывод всех существующиз плейлистов и связанных с ними треков"""
from telegram import Update, ChatAction
from telegram.ext import CallbackContext
from db.schemas import get_all_playlists


def show_playlist_songs(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id

    context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)

    playlists = get_all_playlists()

    if not playlists:
        context.bot.send_message(chat_id=chat_id, text='Нет плейлистов')
        return

    if len(context.args) == 0:
        context.bot.send_message(chat_id=chat_id, text='Введите название плейлиста')
        return

    playlist_name = ' '.join(context.args)

    playlist = next((pl for pl in playlists if pl.name == playlist_name), None)

    if not playlist:
        context.bot.send_message(chat_id=chat_id, text='Плейлист не найден')
        return

    if playlist.songs:
        songs = '\n'.join([f'{s.title} - {s.artist}' for s in playlist.songs])
        text = f'Список песен в плейлисте "{playlist.name}":\n{songs}'
    else:
        text = f'Плейлист "{playlist.name}" пуст'
    context.bot.send_message(chat_id=chat_id, text=text)
