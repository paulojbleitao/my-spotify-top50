import json

def is_duplicate(tested_edge, edges):
    for edge in edges:
        if ((tested_edge['source'] == edge['source'] 
            and tested_edge['target'] == edge['target']) 
            or
            (tested_edge['source'] == edge['target'] 
            and tested_edge['target'] == edge['source'])):
                return True

    return False


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

        if not is_duplicate(edge, new_artists['edges']):
            new_artists['edges'].append(edge)


with open('../graph.json', 'w') as f2:
    json.dump(new_artists, f2)
