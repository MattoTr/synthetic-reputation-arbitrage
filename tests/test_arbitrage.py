from src.arbitrage import check_opportunity

def test_arbitrage_logic():
    arb = check_opportunity()
    assert isinstance(arb, dict)
    assert "profit" in arb
