from pytube import Playlist

playlist_url = input("Enter the playlist URL: ")
playlist = Playlist(playlist_url)

for video in playlist.videos:
    video.streams.get_highest_resolution().download()    

print(f"Downloaded: {video.title}")
