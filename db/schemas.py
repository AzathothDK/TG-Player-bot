from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, Song, Playlist


engine = create_engine('sqlite:///base.db')


def create_database():
    Base.metadata.create_all(engine)


def add_song(title: str, artist: str, file_id: str) -> Song:
    with Session(bind=engine) as session:
        song = Song(title=title, artist=artist, file_id=file_id)
        session.add(song)
        session.commit()
        session.refresh(song)
        return song
    

def add_playlist(name: str) -> Playlist:
    with Session(bind=engine) as session:
        playlist = Playlist(name=name)
        session.add(playlist)
        session.commit()
        session.refresh(playlist)
        return playlist
    

def add_song_to_playlist(song_id: int, playlist_id: int):
    with Session(bind=engine) as session:
        playlist = session.query(Playlist).get(playlist_id)
        song = session.query(Song).get(song_id)
        playlist.songs.append(song)
        session.commit()


def delete_song(song_id: int):
    with Session(bind=engine) as session:
        song = session.query(Song).get(song_id)
        session.delete(song)
        session.commit()


def delete_playlist(playlist_id: int):
    with Session(bind=engine) as session:
        playlist = session.query(Playlist).get(playlist_id)
        session.delete(playlist)
        session.commit()


def get_all_songs() -> Song:
    with Session(bind=engine) as session:
        songs = session.query(Song).all()
        return songs


def get_all_playlists() -> Playlist:
    with Session(bind=engine) as session:
        playlists = session.query(Playlist).all()
        return playlists
