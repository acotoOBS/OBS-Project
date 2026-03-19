import uuid

def generate_tracking_number():

    return f"INT-{uuid.uuid4().hex[:10].upper()}"