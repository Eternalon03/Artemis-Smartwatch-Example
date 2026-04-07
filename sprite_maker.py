from PIL import Image # Requires: pip install pillow

# --- CONFIGURATION ---
image_file = "try.png"  # The image you want to convert
out_width = 20          
out_height = 20        
def convert_to_rgb565(image_path, w, h):
    try:
        # Open the image and force it into standard RGB mode
        img = Image.open(image_path).convert('RGB')
        # Resize it to fit the dimensions specified
        img = img.resize((w, h))
    except Exception as e:
        print(f"Error opening image: {e}")
        return
    pixels = list(img.getdata())
    byte_array = []
    for r, g, b in pixels:
        # Compress 24-bit RGB (8-8-8) down to RGB565 (5-6-5)
        # We shift bits to keep only the most significant ones
        r5 = (r >> 3) & 0x1F
        g6 = (g >> 2) & 0x3F
        b5 = (b >> 3) & 0x1F
        # Combine into a single 16-bit number
        rgb565 = (r5 << 11) | (g6 << 5) | b5
        # Split into two bytes (Big Endian/Standard order for these buffers)
        high_byte = (rgb565 >> 8) & 0xFF
        low_byte = rgb565 & 0xFF
        
        byte_array.append(high_byte)
        byte_array.append(low_byte)

    # Format the bytes into a hex string (e.g., \x80\xff...)
    hex_str = "".join([f"\\x{b:02x}" for b in byte_array])
    # Break the giant string into chunks so it doesn't crash text editors
    chunk_size = 60
    chunks = [hex_str[i:i+chunk_size] for i in range(0, len(hex_str), chunk_size)]
    
    
    print("\n--- COPY THE CODE BELOW INTO YOUR ARTEMIS SCRIPT ---\n")
    print(f"sprite_data = bytearray(")
    for i, chunk in enumerate(chunks):
        if i == len(chunks) - 1:
            print(f"    b'{chunk}'")
        else:
            print(f"    b'{chunk}' +")
    print(f")")
    print(f"my_sprite = FrameBuffer(sprite_data, {w}, {h}, RGB565)")
    print("\n----------------------------------------------------\n")


if __name__ == "__main__":
    convert_to_rgb565(image_file, out_width, out_height)