import os
import cv2

from torch.utils.data import Dataset

from datasets.parser import read_json
from datasets.pair_generator import create_pairs
from datasets.cropper import crop_building
from datasets.transforms import train_transform

from configs.classes import CLASS_MAPPING

from utils.file_utils import get_image_pairs


class BuildingDamageDataset(Dataset):

    def __init__(self, image_folder, label_folder):

        self.samples = []

        image_pairs = get_image_pairs(image_folder)

        for pre_image_name, post_image_name in image_pairs:

            pre_image_path = os.path.join(image_folder, pre_image_name)
            post_image_path = os.path.join(image_folder, post_image_name)

            pre_json_path = os.path.join(
                label_folder,
                pre_image_name.replace(".png", ".json")
            )

            post_json_path = os.path.join(
                label_folder,
                post_image_name.replace(".png", ".json")
            )

            # Read JSON files
            pre_data = read_json(pre_json_path)
            post_data = read_json(post_json_path)

            # Match buildings using UID
            pairs = create_pairs(pre_data, post_data)

            for pair in pairs:

                # Skip buildings without valid damage labels
                if pair["label"] not in CLASS_MAPPING:
                    continue

                self.samples.append({

                    "pre_image_path": pre_image_path,

                    "post_image_path": post_image_path,

                    "pair": pair

                })

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):

        sample = self.samples[index]

        # Read images only when needed
        pre_image = cv2.imread(sample["pre_image_path"])
        post_image = cv2.imread(sample["post_image_path"])

        pair = sample["pair"]

        # Crop same building
        pre_crop = crop_building(
            pre_image,
            pair["pre"]
        )

        post_crop = crop_building(
            post_image,
            pair["post"]
        )

        # Transform to tensor
        pre_crop = train_transform(pre_crop)
        post_crop = train_transform(post_crop)

        label = CLASS_MAPPING[pair["label"]]

        return pre_crop, post_crop, label