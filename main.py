import torch

from models.classifier import DamageClassifier

model = DamageClassifier()

pre = torch.randn(4, 3, 224, 224)

post = torch.randn(4, 3, 224, 224)

output = model(pre, post)

print(output.shape)

print(output)