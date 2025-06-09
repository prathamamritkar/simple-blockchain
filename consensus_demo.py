import random

# PoW: Miner with highest power
miners = [{'name': 'MinerA', 'power': random.randint(1, 100)},
          {'name': 'MinerB', 'power': random.randint(1, 100)},
          {'name': 'MinerC', 'power': random.randint(1, 100)}]
pow_winner = max(miners, key=lambda x: x['power'])
print(f"PoW selected: {pow_winner['name']} (Power: {pow_winner['power']})")
print("PoW: Validator with highest computational power is selected.")

# PoS: Staker with highest stake
stakers = [{'name': 'StakerA', 'stake': random.randint(1, 100)},
           {'name': 'StakerB', 'stake': random.randint(1, 100)},
           {'name': 'StakerC', 'stake': random.randint(1, 100)}]
pos_winner = max(stakers, key=lambda x: x['stake'])
print(f"PoS selected: {pos_winner['name']} (Stake: {pos_winner['stake']})")
print("PoS: Validator with highest stake is selected.")

# DPoS: Delegate with most votes
delegates = [{'name': 'DelegateA', 'votes': random.randint(1, 100)},
             {'name': 'DelegateB', 'votes': random.randint(1, 100)},
             {'name': 'DelegateC', 'votes': random.randint(1, 100)}]
dpos_winner = max(delegates, key=lambda x: x['votes'])
print(f"DPoS selected: {dpos_winner['name']} (Votes: {dpos_winner['votes']})")
print("DPoS: Delegate with most votes is selected by token holders.")

