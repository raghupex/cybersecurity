import hmac, hashlib, time, struct

def generate_totp(secret):
    counter = int(time.time() // 30)
    msg = struct.pack(">Q", counter)
    h = hmac.new(secret.encode(), msg, hashlib.sha1).digest()
    offset = h[-1] & 15
    code = int.from_bytes(h[offset:offset+4], "big") & 0x7fffffff
    return str(code % 1000000).zfill(6)

secret = "JBSWY3DPEHPK3PXP"
totp = generate_totp(secret)

print("Secret Key:", secret)
print("Generated 2FA Code (TOTP):", totp)
user_input = input("Enter OTP for Verification: ")

if user_input == totp:
    print("[SUCCESS] 2FA Authentication Successful!")
else:
    print("[FAILED] Invalid OTP Code.")
