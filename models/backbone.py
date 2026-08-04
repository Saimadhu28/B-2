import torch.nn as nn
from torchvision.models import resnet50, ResNet50_Weights


class Backbone(nn.Module):

    def __init__(self):

        super().__init__()

        model = resnet50(weights=ResNet50_Weights.DEFAULT)

        # Remove the final classification layer
        self.feature_extractor = nn.Sequential(
            *list(model.children())[:-1]
        )

    def forward(self, x):

        x = self.feature_extractor(x)

        x = x.view(x.size(0), -1)

        return x