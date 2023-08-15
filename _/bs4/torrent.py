import requests
torrents = requests.get('http://localhost:8080/api/v2/torrents/info?category=delete').json()

delme = []
for torrent in torrents:
 if torrent.get('category') == 'delete' and torrent.get('seeding_time') > 86400:
 delme.append(torrent['hash'])
if delme:
 hashes = '|'.join(delme)
 requests.post(f'http://localhost:8080/api/v2/torrents/delete?hashes={hashes}&deleteFiles=true')