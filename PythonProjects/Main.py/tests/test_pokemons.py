import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
def test_status_code():
    response = requests.get(f'{host}/trainers', params={'trainer_id':3791})
    assert response.status_code == 200

def test_part_of_body(): 
    response = requests.get(f'{host}/trainers', params={'trainer_id':3791}, headers={"trainer_token":"cafa6ffa097597ff59bfc33dd84a36de"})
    assert response.json()["trainer_name"] == "Данила"