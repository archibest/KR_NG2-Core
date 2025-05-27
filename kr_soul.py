# kr_soul.py :: расшифровка и активация KR-контейнера
def unlock_container(phase, timestamp, soul_id):
    key = hash(f"{phase}∥{timestamp}∥{soul_id}")
    print("KR-container unlocked with key:", key)
