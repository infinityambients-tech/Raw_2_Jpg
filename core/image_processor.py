import cv2
import numpy as np

def optimize_image(image_np):
    """
    Applies basic optimizations to a numpy image array (BGR).
    Includes auto-exposure and contrast adjustment.
    """
    # Convert to LAB for better luminance control
    lab = cv2.cvtColor(image_np, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)

    # Merge channels
    limg = cv2.merge((cl, a, b))
    optimized = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

    # Denoising (optional, can be slow)
    # optimized = cv2.fastNlMeansDenoisingColored(optimized, None, 10, 10, 7, 21)

    return optimized

def auto_contrast(image_np):
    """Simpler auto-contrast adjustment."""
    alpha = 1.2 # Contrast control
    beta = 10   # Brightness control
    new_image = cv2.convertScaleAbs(image_np, alpha=alpha, beta=beta)
    return new_image
