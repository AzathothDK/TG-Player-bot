from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    artist = Column(String(255))
    file_id = Column(String(255))


class Playlist(Base):
    __tablename__ = 'playlists'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    songs = relationship('Song', secondary='playlist_song_link')


playlist_song_link  = Table('playlist_song_link', Base.metadata, 
    Column('playlist_id', ForeignKey('playlists_id'), primary_key=True),
    Column('song_id', ForeignKey('songs.id'), primary_key=True)
)