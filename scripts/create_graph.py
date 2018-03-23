import json

f = open('../mytop50.json', 'r')
data = f.read()
json_obj = json.loads(data)
artists = json_obj['items']
new_artists = {'nodes': [], 'edges': []}
new_artist = {}
genres = {}

for artist in artists:
    new_artist = {'id': artist['id'],
                  'name': artist['name'],
                  'genres': artist['genres'],
                  'img': artist['images'][1]['url'],
                  'url': artist['external_urls']['spotify']}
    new_artists['nodes'].append(new_artist)
    new_artist = {}

for new_artist in new_artists['nodes']:
    for genre in new_artist['genres']:
        if not (genre in genres.keys()):
            genres[genre] = []

        genres[genre].append(new_artist['id'])

for genre in genres:
    for i in range(len(genres[genre]) - 1):
        edge = {'source': genres[genre][i],
                'target': genres[genre][i+1],
                'type': genre}

        if len(genres[genre]) > 2 or genre in 'deep chiptune rap':
            new_artists['edges'].append(edge)


with open('../graph.json', 'w') as f2:
    json.dump(new_artists, f2)
