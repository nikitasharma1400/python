from PIL import Image

img = Image.open(r"C:\Users\ASUS\Downloads\WhatsApp Image 2026-02-21 at 1.24.02 AM.jpeg")
small_size = (64, 64)
img_small = img.resize(small_size, resample=Image.BILINEAR)
result = img_small.resize(img.size, Image.NEAREST)
result.show()
result.save('pixel_art.png')