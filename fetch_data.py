#this script will parse for Michael Jackson's lyrics an generate a new song

from bs4 import BeautifulSoup as bs
import requests




#generate url links
songs = ['black or white', 'man in the mirror', 'smooth criminal', 'ill be there', 'thriller']
songs_url  = []

def generate_url_link(song_name):
    for song in song_name:
        new_name = song.replace(' ', '-')
        songs_url.append(new_name)
        
generate_url_link(songs)

                
#parse the url and get the lyrics
def parse_url():
    for url in songs_url:
        get_html = requests.get('http://www.metrolyrics.com/'+url+'-lyrics-michael-jackson.html') 
        html_lyrics = get_html.content
        soup = bs(html_lyrics, 'html.parser')
        lyrics = soup.find_all('p', class_ = 'verse')
        for song in lyrics:
            yield song.text

parse_url()

#generate lyrics and write to txt file

def add_lyrics():
    open_txt = open('lyrics.txt', 'w')
    for words in parse_url():
        open_txt.write(words)
    open_txt.close()
               
add_lyrics()




