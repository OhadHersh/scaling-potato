import hashlib
with open("redbullracingf1.jpg", "rb") as f:
    original_hash = hashlib.sha256(f.read()).hexdigest()
with open("redbullracingf1.jpg", "ab") as f:
    f.write(b"How are you, Shalom?")
with open("redbullracingf1.jpg", "rb") as f:
    new_hash = hashlib.sha256(f.read()).hexdigest()
if (original_hash == new_hash):
    print(f"The JPEG file has not changed\nhash code is --> {original_hash}")
else:
    print(f"The JPEG file has been changed\noriginal hash code was --> {original_hash}\nnew hash code is --> {new_hash}")