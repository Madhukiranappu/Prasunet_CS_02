from PIL import Image

def validate_key(key):
    """Validates the encryption key."""
    if len(key) != 3:
        raise ValueError("Key must be a tuple of three numbers.")
    if not all(isinstance(k, int) for k in key):
        raise ValueError("Each key element must be an integer.")
    return True

def clamp(value):
    """Ensures the pixel value is within the valid range (0-255)."""
    return max(0, min(value, 255))

def encrypt_image(image_path, key):
    """Encrypts an image using XOR with a key."""
    validate_key(key)
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            new_r = clamp(r ^ key[0])
            new_g = clamp(g ^ key[1])
            new_b = clamp(b ^ key[2])
            pixels[x, y] = (new_r, new_g, new_b)

    encrypted_path = f"{image_path}.encrypted.png"
    image.save(encrypted_path)
    print(f"Image encrypted and saved as {encrypted_path}")
    return encrypted_path

def decrypt_image(image_path, key):
    """Decrypts an encrypted image using XOR with the same key."""
    validate_key(key)
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            new_r = clamp(r ^ key[0])
            new_g = clamp(g ^ key[1])
            new_b = clamp(b ^ key[2])
            pixels[x, y] = (new_r, new_g, new_b)

    decrypted_path = f"{image_path}.decrypted.png"
    image.save(decrypted_path)
    print(f"Image decrypted and saved as {decrypted_path}")
    return decrypted_path

def compare_images(image_path1, image_path2):
    """Compares two images pixel by pixel."""
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)

    if image1.size != image2.size:
        print("Images are of different sizes")
        return False

    pixels1 = image1.load()
    pixels2 = image2.load()
    width, height = image1.size

    for y in range(height):
        for x in range(width):
            if pixels1[x, y] != pixels2[x, y]:
                print(f"Images differ at pixel ({x}, {y})")
                return False
    print("Images are the same")
    return True

# Example usage
image_path = r'C:\Users\Dell\OneDrive\Desktop\image encryption\7.jpg'
key = (123, 45, 67)  # Replace with your desired key (3 numbers within the range 0-255)

encrypted_image_path = encrypt_image(image_path, key)
decrypted_image_path = decrypt_image(encrypted_image_path, key)

# Compare original and encrypted images
compare_images(image_path, encrypted_image_path)

# Compare original and decrypted images
compare_images(image_path, decrypted_image_path)
