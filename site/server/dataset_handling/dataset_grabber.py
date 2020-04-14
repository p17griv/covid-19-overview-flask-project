import requests

print('Beginning file download...')

url = 'https://storage.googleapis.com/kaggle-data-sets/494724/1079827/bundle/archive.zip?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1587135399&Signature=QfThSMyoxgxBwzEBAdk6FMN%2B9PCG8QU3rrmz%2Bep%2BhRWi6oYZqRE3G84F9NzixqVTghz%2FvWU6jm6mT543K9NQHVrCPSqrJz%2F8u87xR6SHD4QxvLChpbqbAlC0lhZodE9ymNmLlfHLITU27KxtfkrjH5AY6r3JdqjAd9%2F2yk8i4IzMVc70qPnMMsjfFCVTH6ooKOPsgolKj6ODxzghN4G3GWapGIwPcr3fYEXuhLfcQwMolOmGXvgryNRNkbylgwFkmM7nUsnB2tcrzJrMoT0L9Ue4IhpALkdBjz%2FAtVn6FmxLcKViXK7Y57Hm7UaHZvYrouMdOvD%2BYCEjbacqpyzbrA%3D%3D&response-content-disposition=attachment%3B+filename%3Dnovel-corona-virus-2019-dataset.zip'
r = requests.get(url, allow_redirects=True)

with open('datasets.zip', 'wb') as f:
    f.write(r.content)


print("HTTP status code:",r.status_code)
print("Content type:", r.headers['content-type'])