import requests


def download_dataset():
    print('Beginning file download...')

    dataset = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/json/'

    r = requests.get(dataset, allow_redirects=True)

    with open('dataset.json', 'wb') as f:
        f.write(r.content)

    if r.status_code == 200:
        print('Success!')
        print("Content type:", r.headers['content-type'])
    else:
        print('Problem occurred\n with code: ', r.status_code)


if __name__ == '__main__':
    download_dataset()
