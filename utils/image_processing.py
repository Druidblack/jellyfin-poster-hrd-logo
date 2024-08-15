# utils/image_processing.py

from PIL import Image

def add_hdr_watermark(poster_path: str, watermark_path: str, scale: float = 0.1) -> None:
    """
    Adds an HDR watermark to the top-right corner of the image with dynamic scaling and positioning.

    :param poster_path: Path to the poster file.
    :param watermark_path: Path to the watermark file (hdr.png).
    :param scale: Scale of the watermark relative to the width of the image (default 10%).
    """
    try:
        # Open the poster image and watermark
        poster = Image.open(poster_path)
        watermark = Image.open(watermark_path)

        # Convert the watermark to RGBA (for transparency support)
        watermark = watermark.convert("RGBA")

        # Get the poster dimensions
        poster_width, poster_height = poster.size

        # Calculate the new watermark size proportional to the image width
        new_width = int(poster_width * scale)
        aspect_ratio = watermark.height / watermark.width
        new_height = int(new_width * aspect_ratio)
        watermark = watermark.resize((new_width, new_height), Image.ANTIALIAS)

        # Calculate dynamic positioning based on the size of the poster
        offset_x = int(poster_width * 0.02)  # 2% from the right edge
        offset_y = int(poster_height * 0.02)  # 2% from the top edge
        position = (poster_width - new_width - offset_x, offset_y)

        # Paste the watermark onto the poster
        poster.paste(watermark, position, watermark)

        # Save the result
        poster.save(poster_path)
        print(f"Watermark added to the poster: {poster_path}")
    except Exception as e:
        print(f"Error adding watermark: {e}")
