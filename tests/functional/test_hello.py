def test_hello(client):
    response = client.post(
        '/hello',
        data = {
            'name':'Jannik',
        },
        follow_redirects = True
    )

    assert response.status_code == 200
    assert b'Jannik' in response.data