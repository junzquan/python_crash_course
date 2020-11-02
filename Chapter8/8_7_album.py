def make_album(artist, title, tracks=''):
    dict = {}
    dict['artist'] = artist
    dict['album title'] = title
    if tracks:
        dict['number of tracks'] = tracks
    return dict

print(make_album('Adele', '21', 15))
print(make_album('Taylor Swift', 'Red'))
