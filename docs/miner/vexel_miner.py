import time
import random

# Vexel Miner - Educational Simulation

balance = 0
blocks = []
difficulty = "000"

def fake_hash():
    chars = "abcdef0123456789"
    return difficulty + "".join(random.choice(chars) for _ in range(61))

def mine_block():
    global balance
    print("\n⛏️ Mining block...")
    time.sleep(3)

    block = {
        "index": len(blocks),
        "timestamp": time.ctime(),
        "nonce": random.randint(1000, 99999),
        "hash": fake_hash(),
        "reward": 50
    }

    blocks.append(block)
    balance += 50

    print("✅ Block mined!")
    print("Block #:", block["index"])
    print("Nonce:", block["nonce"])
    print("Hash:", block["hash"])
    print("Reward: 50 VXL")
    print("Balance:", balance, "VXL")

print("🔗 Vexel Miner (Simulation)")
print("Educational use only. No real crypto.\n")

while True:
    input("Press ENTER to mine a block ")
    mine_block()