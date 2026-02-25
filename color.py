import cv2
import matplotlib.pyplot as plt
import os

def analyze_histogram(image_path):
   
    if not os.path.exists(image_path):
        print(f"Error: The file was not found at:\n{image_path}")
        print("\nPossible fixes:")
        print("1. Check if the file extension is .jpg or .jpeg")
        print("2. Ensure the file is actually in that folder")
        return

    
    image = cv2.imread(image_path)
    
    if image is None:
        print("Error: Could not decode the image.")
        return

    
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    
    plt.figure(figsize=(12, 6))
    
    
    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title('Source Image')
    plt.axis('off')

    
    plt.subplot(1, 2, 2)
    for i, col in enumerate(('r', 'g', 'b')):
        hist = cv2.calcHist([image_rgb], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])
    
    plt.title('Color Histogram')
    plt.xlabel('Intensity')
    plt.ylabel('Pixels')
    plt.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.show()


path = r"C:\Users\ASUS\Downloads\WhatsApp Image 2026-02-21 at 1.24.02 AM.jpeg"

analyze_histogram(path)