def make_album(artist, title, tracks=''):
    dict = {}
    dict['artist'] = artist
    dict['album title'] = title
    if tracks:
        dict['number of tracks'] = tracks
    return dict

while True:
    print("Collecting album information:")
    print("(enter 'q' at any time to quit.)")

    artist = input("Artist: ")
    if artist == 'q':
        break

    title = input("Title: ")
    if title == 'q':
        break
    
    print(make_album(artist, title))
    