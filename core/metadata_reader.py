import exifread
import os

def get_metadata(file_path):
    """
    Extracts basic EXIF metadata from a RAW file.
    """
    metadata = {
        'Camera': 'Unknown',
        'ISO': 'Unknown',
        'Shutter Speed': 'Unknown',
        'Aperture': 'Unknown',
        'Lens': 'Unknown',
        'Date': 'Unknown'
    }

    try:
        with open(file_path, 'rb') as f:
            tags = exifread.process_file(f, details=False)
            
            # Common tags mapping
            metadata['Camera'] = str(tags.get('Image Model', 'Unknown'))
            metadata['ISO'] = str(tags.get('EXIF ISOSpeedRatings', 'Unknown'))
            metadata['Shutter Speed'] = str(tags.get('EXIF ExposureTime', 'Unknown'))
            metadata['Aperture'] = str(tags.get('EXIF FNumber', 'Unknown'))
            metadata['Lens'] = str(tags.get('EXIF LensModel', 'Unknown'))
            metadata['Date'] = str(tags.get('Image DateTime', 'Unknown'))
            
    except Exception as e:
        print(f"Error reading metadata from {file_path}: {e}")
    
    return metadata
