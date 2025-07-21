# myapp/image_mixins.py
from PIL import Image
import os
from django.db import models

class WebImageMixin(models.Model):
    class Meta:
        abstract = True

    def convert_to_webp_and_avif(self, image_field):
        if not image_field:
            return

        image_path = image_field.path
        base_path, ext = os.path.splitext(image_path)

        try:
            img = Image.open(image_path).convert("RGB")

            # Save WebP
            webp_path = base_path + '.webp'
            img.save(webp_path, 'webp', quality=85)

            # Save AVIF (optional)
            avif_path = base_path + '.avif'
            try:
                img.save(avif_path, 'avif', quality=85)
            except Exception as e:
                print("AVIF conversion failed:", e)

        except Exception as e:
            print("Image conversion error:", e)
