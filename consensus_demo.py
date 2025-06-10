import random

# Create mock objects for 3 validators:
# miner = {power: random value} for PoW
miners = [{'name': 'MinerA', 'power': random.randint(1, 100)},
          {'name': 'MinerB', 'power': random.randint(1, 100)},
          {'name': 'MinerC', 'power': random.randint(1, 100)}]
# staker = {stake: random value} for PoS
stakers = [{'name': 'StakerA', 'stake': random.randint(1, 100)},
           {'name': 'StakerB', 'stake': random.randint(1, 100)},
           {'name': 'StakerC', 'stake': random.randint(1, 100)}]
# voters = [3 mock accounts voting] for DPoS
delegates = [{'name': 'DelegateA', 'votes': random.randint(1, 100)},
             {'name': 'DelegateB', 'votes': random.randint(1, 100)},
             {'name': 'DelegateC', 'votes': random.randint(1, 100)}]
voters = [{'voter': 'Voter1', 'stake': random.randint(1, 50), 'delegate': 'DelegateA'},
          {'voter': 'Voter2', 'stake': random.randint(1, 50), 'delegate': 'DelegateB'},
          {'voter': 'Voter3', 'stake': random.randint(1, 50), 'delegate': 'DelegateA'}]
delegates = {'DelegateA': sum(v['stake'] for v in voters if v['delegate'] == 'DelegateA'),
             'DelegateB': sum(v['stake'] for v in voters if v['delegate'] == 'DelegateB'),
             'DelegateC': sum(v['stake'] for v in voters if v['delegate'] == 'DelegateC')}

# For PoW: Select validator with highest power
pow_decision = max(miners, key=lambda x: x['power'])
# For PoS: Select validator with highest stake
pos_decision = max(stakers, key=lambda x: x['stake'])
# For DPoS: Randomly choose a delegate based on most votes
dpos_decision = max(delegates.items, key=lambda x: x[1])

# Print selected validator and consenasus method used
print(f"Selected PoW validator: {pow_decision['name']}, (Consensus method: Power {pow_decision['power']})")
print(f"Selected PoS validator: {pos_decision['name']}, (Consensus method: Stake {pos_decision['stake']})")
print(f"Selected DPoS validator: {dpos_decision [0]}, (Consensus method: Votes {dpos_decision[1]})")
# Include a console.log explanation of the selection logic
print("\nPoW: Validator with highest computational power is selected.")
print("PoS: Validator with highest stake is selected.")
print("DPoS: Delegate with most votes is selected by token holders.")
