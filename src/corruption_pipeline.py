
import cv2
import numpy as np


def apply_corruption(image, corruption, severity, seed=42):
    """Apply one of five image corruptions."""

    if severity not in (1, 2, 3):
        raise ValueError("Severity must be 1, 2, or 3")

    if corruption == "low_brightness":
        factors = {1: 0.7, 2: 0.5, 3: 0.3}
        result = image.astype(np.float32) * factors[severity]
        return np.clip(result, 0, 255).astype(np.uint8)

    elif corruption == "gaussian_noise":
        strengths = {1: 10, 2: 20, 3: 30}
        rng = np.random.default_rng(seed)
        noise = rng.normal(0, strengths[severity], image.shape)
        result = image.astype(np.float32) + noise
        return np.clip(result, 0, 255).astype(np.uint8)

    elif corruption == "motion_blur":
        sizes = {1: 5, 2: 9, 3: 15}
        size = sizes[severity]
        kernel = np.zeros((size, size), dtype=np.float32)
        kernel[size // 2, :] = 1.0 / size
        return cv2.filter2D(image, -1, kernel)

    elif corruption == "defocus_blur":
        sizes = {1: 3, 2: 7, 3: 11}
        size = sizes[severity]
        kernel = np.zeros((size, size), dtype=np.float32)
        center = size // 2

        for y in range(size):
            for x in range(size):
                if (x-center)**2 + (y-center)**2 <= center**2:
                    kernel[y, x] = 1

        kernel /= kernel.sum()
        return cv2.filter2D(image, -1, kernel)

    elif corruption == "jpeg_compression":
        qualities = {1: 70, 2: 40, 3: 15}
        success, encoded = cv2.imencode(
            ".jpg", image,
            [cv2.IMWRITE_JPEG_QUALITY, qualities[severity]]
        )
        if not success:
            raise RuntimeError("JPEG encoding failed")

        return cv2.imdecode(encoded, cv2.IMREAD_COLOR)

    else:
        raise ValueError("Unknown corruption type")


def corrupt_image_file(input_path, output_path, corruption, severity, seed=42):
    """Load, corrupt, and save an image."""
    image = cv2.imread(input_path)

    if image is None:
        raise FileNotFoundError(input_path)

    result = apply_corruption(image, corruption, severity, seed)

    if not cv2.imwrite(output_path, result):
        raise RuntimeError("Could not save corrupted image")

    return output_path
