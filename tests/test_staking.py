from src.staking import stake, get_rewards

def test_stake_and_reward():
    stake(100, "USDC")
    rewards = get_rewards("USDC")
    assert rewards >= 0
