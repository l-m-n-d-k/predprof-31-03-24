from requests import get, post, delete
print(get('http://localhost:5000/api/v2/users').json())
print(get('http://localhost:5000/api/v2/users/1').json())
print(get('http://localhost:5000/api/v2/users/999').json())
print(get('http://localhost:5000/api/v2/users/q').json())
print(post('http://localhost:5000/api/v2/users', json={}).json())
print(post('http://localhost:5000/api/v2/users',
           json={'surname': 'Заголовок'}).json())
print(post('http://localhost:5000/api/v2/users',
           json={"surname": "Petrov",
                 "name": "Petr",
                 "age": 1,
                 "position": "position",
                 "speciality": "speciality",
                 "email": "email5@email",
                 "address": "address",
                 "hashed_password": "qwerty12345",
                 "modified_date": None}).json())
print(get('http://localhost:5000/api/v2/users').json())
print(delete('http://localhost:5000/api/v2/users/-1').json())
print(delete('http://localhost:5000/api/v2/users/3').json())
print(get('http://localhost:5000/api/v2/users').json())