import json


def related_artists(genres1, genres2):
    for genre1 in genres1:
        for genre2 in genres2:
            if genre1 == genre2:
                return genre1

    return False


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

for artist in artists:
    new_artist['id'] = artist['id']
    new_artist['name'] = artist['name']
    new_artist['genres'] = artist['genres']
    new_artist['img'] = artist['images'][1]['url']
    new_artist['url'] = artist['external_urls']['spotify']
    new_artists['nodes'].append(new_artist)
    new_artist = {}


edge = {}
for artist in new_artists['nodes']:
    for artist2 in new_artists['nodes']:
        same_genre = related_artists(artist['genres'], artist2['genres'])
        if (artist['id'] != artist2['id']) and same_genre:
            edge['source'] = artist['id']
            edge['target'] = artist2['id']
            edge['type'] = same_genre

            if not is_duplicate(edge, new_artists['edges']):
                new_artists['edges'].append(edge)
            edge = {}


with open('../graph.json', 'w') as f2:
    json.dump(new_artists, f2)
