
import os
import sys
import subprocess
import urllib.request
import pandas as pd
from pathlib import Path


def rebuild_dataset(manifest_path, output_folder):
    manifest = pd.read_csv(manifest_path)

    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    # Keep only images that are not already downloaded
    missing = []

    for _, row in manifest.iterrows():
        image_id = row["image_id"]
        split = row["open_images_split"]
        image_path = output_folder / f"{image_id}.jpg"

        if not image_path.exists():
            missing.append(f"{split}/{image_id}")

    if not missing:
        print("All images are already downloaded.")
        return

    # Download the official Open Images downloader
    downloader_path = output_folder / "downloader.py"
    downloader_url = (
        "https://raw.githubusercontent.com/"
        "openimages/dataset/master/downloader.py"
    )

    urllib.request.urlretrieve(downloader_url, downloader_path)

    # Create the image ID list
    image_list_path = output_folder / "image_list.txt"

    with open(image_list_path, "w") as file:
        file.write("\\n".join(missing))

    # Run the official downloader
    subprocess.run(
        [
            sys.executable,
            str(downloader_path),
            str(image_list_path),
            "--download_folder=" + str(output_folder),
            "--num_processes=5"
        ],
        check=True
    )

    print("Download process finished.")
    print("Images requested:", len(missing))


if __name__ == "__main__":
    rebuild_dataset(
        "data/manifest.csv",
        "data/images/open_images"
    )
