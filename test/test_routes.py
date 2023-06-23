import requests


def test_insert_route():
    data = {
        "product" : "Filtro de oleo",
        "brand" : "Lubrax",
        "user" : "fabricio.serrano"
    }

    resp = requests.post('http://127.0.0.1:5000/products/insert', params=data)


    