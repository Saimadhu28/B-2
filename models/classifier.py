import torch.nn as nn

from models.siamese import SiameseNetwork


class DamageClassifier(nn.Module):

    def __init__(self):

        super().__init__()

        self.siamese = SiameseNetwork()

        self.classifier = nn.Sequential(

            nn.Linear(2048, 512),

            nn.ReLU(),

            nn.Dropout(0.3),

            nn.Linear(512, 128),

            nn.ReLU(),

            nn.Dropout(0.3),

            nn.Linear(128, 4)

        )

    def forward(self, pre, post):

        features = self.siamese(pre, post)

        output = self.classifier(features)

        return output