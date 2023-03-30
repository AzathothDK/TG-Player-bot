from telegram.ext import Updater, CommandHandler
from db.schemas import create_database
from handlers.add_song import add_song
from handlers.add_playlist import add_playlist
from handlers.delete_song import delete_song
from handlers.delete_playlist import delete_playlist
from handlers.show_all_songs import show_all_songs
from handlers.show_all_playlists import show_all_playlists
from handlers.show_playlists_songs import show_playlist_songs

def help(update, context):
    """Отправляет сообщение с описанием команд."""
    help_message = '''
    Это бот для комфортного прослушивания музыки. Вот список доступных команд:
    
    /add_song - добавить песню в базу данных
    /add_playlist - создать плейлист
    /delete_song - удалить песню из базы данных
    /delete_playlist - удалить плейлист
    /show_all_songs - показать все песни в базе данных
    /show_all_playlists - показать все плейлисты
    /show_playlist_songs - показать все песни в выбранном плейлисте
    '''
    update.message.reply_text(help_message)


def start(update, context):
    """Отправляет сообщение с приветствием и описанием команд."""
    start_message = '''
    Привет! Я бот для комфортного прослушивания музыки. Вот список доступных команд:
    
    /add_song - добавить песню в базу данных
    /add_playlist - создать плейлист
    /delete_song - удалить песню из базы данных
    /delete_playlist - удалить плейлист
    /show_all_songs - показать все песни в базе данных
    /show_all_playlists - показать все плейлисты
    /show_playlist_songs - показать все песни в выбранном плейлисте
    '''
    update.message.reply_text(start_message)


def main():
    """Запуск бота."""
    updater = Updater("TOKEN", use_context=True)

    create_database()

    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('add_song', add_song))
    updater.dispatcher.add_handler(CommandHandler('add_playlist', add_playlist))
    updater.dispatcher.add_handler(CommandHandler('delete_song', delete_song))
    updater.dispatcher.add_handler(CommandHandler('delete_playlist', delete_playlist))
    updater.dispatcher.add_handler(CommandHandler('show_all_songs', show_all_songs))
    updater.dispatcher.add_handler(CommandHandler('show_all_playlists', show_all_playlists))
    updater.dispatcher.add_handler(CommandHandler('show_playlist_songs', show_playlist_songs))

    updater.start_polling()

