def test_create_note(client):
    response = client.post("/notes", json={"title": "Test Title", "content": "Test Content"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Title"
    assert "id" in data

def test_get_notes_list_and_pagination(client):
    client.post("/notes", json={"title": "Note 1"})
    client.post("/notes", json={"title": "Note 2"})
    
    response = client.get("/notes?limit=1&offset=0")
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_get_note_by_id(client):
    create_resp = client.post("/notes", json={"title": "Target Note"})
    note_id = create_resp.json()["id"]
    
    response = client.get(f"/notes/{note_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Target Note"

def test_get_nonexistent_note_returns_404(client):
    response = client.get("/notes/999")
    assert response.status_code == 404

def test_delete_note(client):
    create_resp = client.post("/notes", json={"title": "To Delete"})
    note_id = create_resp.json()["id"]
    
    del_resp = client.delete(f"/notes/{note_id}")
    assert del_resp.status_code == 204
    
    get_resp = client.get(f"/notes/{note_id}")
    assert get_resp.status_code == 404