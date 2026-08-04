import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_PATH = os.path.join(PROJECT_ROOT, "data", "xbd")

TRAIN_PATH = os.path.join(DATASET_PATH, "train")

TEST_PATH = os.path.join(DATASET_PATH, "test")

TIER3_PATH = os.path.join(DATASET_PATH, "tier3")

IMAGE_SIZE = 224

BATCH_SIZE = 16

EPOCHS = 30

LEARNING_RATE = 1e-4

NUM_CLASSES = 4

DEVICE = "cuda"