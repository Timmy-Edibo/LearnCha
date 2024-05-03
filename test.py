import secrets

# Generate a random URL-safe Base64-encoded string of length 16
random_base64 = secrets.token_urlsafe(36)
print(random_base64)
