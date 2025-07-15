from src.flashloan_executor import FlashLoanExecutor
from src.swap_manager import SwapManager

class ArbitrageEngine:
    def __init__(self):
        self.flashloan_executor = FlashLoanExecutor()
        self.swap_manager = SwapManager()

    def run_arbitrage(self, token_pair, amount):
        profit = self.flashloan_executor.execute_flashloan(amount, token_pair)
        swapped = self.swap_manager.swap(token_pair[0], token_pair[1], amount)
        print(f"Arbitrage completed. Profit: {profit}, Swapped: {swapped}")
        return profit
