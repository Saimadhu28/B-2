import torch
import torch.nn as nn

from models.backbone import Backbone


class SiameseNetwork(nn.Module):

    def __init__(self):

        super().__init__()

        self.backbone = Backbone()

    def forward(self, pre, post):

        pre_features = self.backbone(pre)

        post_features = self.backbone(post)

        difference = torch.abs(pre_features - post_features)

        return difference