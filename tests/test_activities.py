from src.app import activities


def test_get_activities_returns_all_activity_details(client):
    # Arrange
    expected_activity = activities["Chess Club"]

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert response.json()["Chess Club"] == expected_activity
    assert set(response.json()) == set(activities)


def test_get_activities_includes_participant_lists(client):
    # Arrange
    expected_participants = activities["Programming Class"]["participants"]

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert response.json()["Programming Class"]["participants"] == expected_participants
