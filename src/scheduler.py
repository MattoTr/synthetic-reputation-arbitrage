import schedule
import time
from src.arbitrage_engine import ArbitrageEngine

class Scheduler:
    def __init__(self):
        self.engine = ArbitrageEngine()

    def job(self):
        print("Running scheduled arbitrage...")
        self.engine.run_arbitrage(("WETH", "DAI"), 1000)

    def start(self):
        schedule.every(10).seconds.do(self.job)
        while True:
            schedule.run_pending()
            time.sleep(1)
