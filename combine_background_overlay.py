import torch
import numpy as np
from PIL import Image

class CombineBackgroundOverlay:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "background": ("IMAGE",),
                "overlay_alpha": ("IMAGE",),
                "horizontal_position": ("FLOAT", {"default": 50, "min": -50, "max": 150, "step": 0.1}),
                "vertical_position": ("FLOAT", {"default": 50, "min": -50, "max": 150, "step": 0.1}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "combine_background_overlay"
    CATEGORY = "Bjornulf"

    def combine_background_overlay(self, background, overlay_alpha, horizontal_position, vertical_position):
        # Convert background from torch tensor to numpy array
        bg = background[0].numpy()
        bg = (bg * 255).astype(np.uint8)
        bg_img = Image.fromarray(bg, 'RGB')

        results = []

        for overlay in overlay_alpha:
            # Convert overlay from torch tensor to numpy array
            ov = overlay.numpy()
            ov = (ov * 255).astype(np.uint8)

            # Create PIL Image for overlay
            if ov.shape[2] == 4:
                ov_img = Image.fromarray(ov, 'RGBA')
            else:
                ov_img = Image.fromarray(ov, 'RGB')
                ov_img = ov_img.convert('RGBA')

            # Calculate horizontal position
            x = int((horizontal_position / 100) * (bg_img.width - ov_img.width))

            # Calculate vertical position
            y = int((vertical_position / 100) * (bg_img.height - ov_img.height))

            # Create a new image for this overlay
            result = Image.new('RGBA', bg_img.size, (0, 0, 0, 0))

            # Paste the background
            result.paste(bg_img, (0, 0))

            # Paste the overlay in the calculated position
            result.paste(ov_img, (x, y), ov_img)

            # Convert back to numpy array and then to torch tensor
            result_np = np.array(result)
            
            # If the result is RGBA, convert to RGB
            if result_np.shape[2] == 4:
                result_np = result_np[:,:,:3]

            result_tensor = torch.from_numpy(result_np).float() / 255.0

            results.append(result_tensor)

        # Stack all results into a single tensor
        final_result = torch.stack(results)

        return (final_result,)