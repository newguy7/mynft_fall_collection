import os
import json
from scripts.upload_to_pinata import pinata_upload, get_pinned


def create_metadata():
    imgDir = ".\\imgs"
    metadatas = []

    pinnedFiles = get_pinned()

    for idx, file in enumerate(os.listdir(imgDir)):
        filepath = os.path.join(imgDir, file)
        logoName = file.split(".")[0]
        metadataFile = f"{logoName}.json"
        metadataFilePath = f".\\metadata\\{metadataFile}"

        if metadataFile in pinnedFiles:
            metadatas.append(
                {"filename": metadataFile, "CID": pinnedFiles[metadataFile]}
            )
            continue

        result = pinata_upload(filepath)
        imgCID = result["IpfsHash"]

        metadata = {
            "name": logoName,
            "description": f"The fall images collection: {logoName}",
            "image": imgCID,
            "attributes": [
                {"trait_type": "Quality", "value": "HD"},
                {"trait_type": "beauty_level", "value": 100},
                {"trait_type": "collection_rank", "value": idx + 1},
            ],
        }

        with open(metadataFilePath, "w") as f:
            json.dump(metadata, f)

        result = pinata_upload(metadataFilePath)
        metadatas.append({"filename": metadataFile, "CID": result["IpfsHash"]})

    return metadatas


def main():
    create_metadata()
