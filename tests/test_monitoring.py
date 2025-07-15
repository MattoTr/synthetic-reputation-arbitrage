from src.monitor import simulate_event_trigger

def test_event_trigger():
    assert simulate_event_trigger() == "triggered"
