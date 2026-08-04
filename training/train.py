import torch
from torch.utils.data import DataLoader

from datasets.dataset_loader import BuildingDamageDataset
from models.classifier import DamageClassifier
from training.engine import train_one_epoch


# ==========================================
# DEVICE
# ==========================================

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("Device :", device)


# ==========================================
# DATASET
# ==========================================

dataset = BuildingDamageDataset(

    image_folder=r"D:\Building-Damage-Assessment-2\dataset\train\images",

    label_folder=r"D:\Building-Damage-Assessment-2\dataset\train\labels"

)


# ==========================================
# DATALOADER
# ==========================================

train_loader = DataLoader(

    dataset,

    batch_size=32,

    shuffle=True,

    num_workers=0

)


# ==========================================
# MODEL
# ==========================================

model = DamageClassifier().to(device)


# ==========================================
# LOSS
# ==========================================

criterion = torch.nn.CrossEntropyLoss()


# ==========================================
# OPTIMIZER
# ==========================================

optimizer = torch.optim.Adam(

    model.parameters(),

    lr=0.0001

)


# ==========================================
# TRAINING
# ==========================================

EPOCHS = 5


for epoch in range(EPOCHS):

    loss, accuracy = train_one_epoch(

        model,

        train_loader,

        criterion,

        optimizer,

        device

    )

    print()

    print(f"Epoch {epoch+1}/{EPOCHS}")

    print(f"Loss : {loss:.4f}")

    print(f"Accuracy : {accuracy:.2f}%")