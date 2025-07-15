from src.flashloan import simulate_flashloan

def test_flashloan_sim():
    result = simulate_flashloan("DAI", 5000)
    assert result["status"] == "success"
    assert result["profit"] >= 0
