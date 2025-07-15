import redis

class StakingManager:
    def __init__(self, redis_host="localhost", redis_port=6379):
        self.r = redis.Redis(host=redis_host, port=redis_port, db=0)

    def stake(self, wallet_address, amount):
        current = float(self.r.get(wallet_address) or 0)
        self.r.set(wallet_address, current + amount)
        return current + amount

    def get_staked_amount(self, wallet_address):
        return float(self.r.get(wallet_address) or 0)
