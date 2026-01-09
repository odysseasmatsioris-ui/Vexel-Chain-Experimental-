import time
import random
import sys
import threading
import os

# ===============================
# Vexel Miner — Persistent Simulator
# ===============================

difficulty = "000"
block_reward = 50
mining = False

balance = 0
shares = 0
username = ""

def user_file():
    return f"user_{username}.txt"

def load_user():
    global balance, shares
    if os.path.exists(user_file()):
        with open(user_file(), "r") as f:
            data = f.read().split(",")
            balance = int(data[0])
            shares = int(data[1])
    else:
        balance = 0
        shares = 0

def save_user():
    with open(user_file(), "w") as f:
        f.write(f"{balance},{shares}")

def fake_hash():
    chars = "abcdef0123456789"
    return difficulty + "".join(random.choice(chars) for _ in range(61))

def mining_loop(address):
    global mining, balance, shares

    attempts = 0
    start_time = time.time()
    next_share_time = random.randint(8, 20)

    print(f"\n⛏️  Mining on Vexel Chain")
    print(f"👤 User: {username}")
    print(f"📍 Address: {address}")
    print("🔄 Miner running...\n")

    while mining:
        nonce = random.randint(1_000_000, 9_999_999)
        attempts += random.randint(5_000, 20_000)
        current_hash = fake_hash()

        elapsed = time.time() - start_time
        hashrate = int(attempts / max(elapsed, 1))

        sys.stdout.write(
            f"\rNonce: {nonce} | Attempts: {attempts} | "
            f"Hashrate: {hashrate} H/s | Hash: {current_hash[:18]}..."
        )
        sys.stdout.flush()

        if elapsed >= next_share_time:
            shares += 1
            balance += block_reward
            save_user()

            print("\n\n✅ Share accepted")
            print(f"🏆 Reward: +{block_reward} VXL")
            print(f"📦 Shares: {shares}")
            print(f"💰 Balance: {balance} VXL\n")

            next_share_time = elapsed + random.randint(8, 20)

        time.sleep(0.5)

def start_mining(address):
    global mining
    mining = True
    t = threading.Thread(target=mining_loop, args=(address,))
    t.start()
    return t

# ===============================
# PROGRAM START
# ===============================

print("🔗 Vexel Miner v1.0")
print("Educational mining simulation — NOT real crypto\n")

username = input("Create / enter username: ").strip()
load_user()

print(f"\n👋 Welcome {username}")
print(f"💰 Saved balance: {balance} VXL")
print(f"📦 Saved shares: {shares}")

address = input("\nEnter your mining address: ")

while True:
    input("\nPress ENTER to start mining ")
    miner_thread = start_mining(address)

    input("\nPress ENTER to stop mining ")
    mining = False
    miner_thread.join()

    save_user()
    print("\n🛑 Miner stopped")
    print(f"💰 Balance: {balance} VXL")

    input("\nPress ENTER again to restart mining ")