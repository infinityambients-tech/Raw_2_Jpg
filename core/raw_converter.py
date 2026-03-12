import rawpy
from PIL import Image
import numpy as np
import os

def convert_raw_to_jpg(raw_path, output_path, quality=95, resize=None):
    """
    Converts a RAW file to JPG using rawpy and Pillow.
    resize: tuple (width, height) or None
    """
    try:
        with rawpy.imread(raw_path) as raw:
            # Postprocess: use_camera_wb=True often gives better results,
            # no_auto_bright=False lets rawpy handle initial exposure.
            rgb = raw.postprocess(use_camera_wb=True, no_auto_bright=False, bright=1.0)
            
            # Convert to PIL Image
            image = Image.fromarray(rgb)
            
            if resize:
                image.thumbnail(resize, Image.Resampling.LANCZOS)
            
            # Save as JPG
            image.save(output_path, "JPEG", quality=quality, optimize=True)
            return True, None
    except Exception as e:
        return False, str(e)

def get_raw_preview(raw_path):
    """
    Extracts a fast preview/thumbnail from RAW if available, 
    otherwise renders a low-res version.
    Returns a numpy array (RGB).
    """
    try:
        with rawpy.imread(raw_path) as raw:
            try:
                # Try to extract the embedded thumbnail
                thumb = raw.extract_thumb()
                if thumb.format == rawpy.ThumbFormat.JPEG:
                    # It's a JPEG, decode it
                    from io import BytesIO
                    image = Image.open(BytesIO(thumb.data))
                    return np.array(image.convert("RGB"))
                elif thumb.format == rawpy.ThumbFormat.BITMAP:
                    # It's a bitmap, already RGB
                    return thumb.data
            except rawpy.LibRawNoThumbnailError:
                pass
            
            # Fallback: render at half size
            rgb = raw.postprocess(use_camera_wb=True, half_size=True, no_auto_bright=False)
            return rgb
    except Exception as e:
        print(f"Error getting preview for {raw_path}: {e}")
        return None
