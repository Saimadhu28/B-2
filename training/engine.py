import torch


def train_one_epoch(model,
                    dataloader,
                    criterion,
                    optimizer,
                    device):

    model.train()

    running_loss = 0.0

    total_samples = 0

    correct_predictions = 0

    for pre, post, label in dataloader:

        pre = pre.to(device)
        post = post.to(device)
        label = label.to(device)

        # Clear previous gradients
        optimizer.zero_grad()

        # Forward pass
        outputs = model(pre, post)

        # Calculate loss
        loss = criterion(outputs, label)

        # Backpropagation
        loss.backward()

        # Update weights
        optimizer.step()

        # Statistics
        running_loss += loss.item()

        predictions = torch.argmax(outputs, dim=1)

        correct_predictions += (predictions == label).sum().item()

        total_samples += label.size(0)

    epoch_loss = running_loss / len(dataloader)

    epoch_accuracy = (correct_predictions / total_samples) * 100

    return epoch_loss, epoch_accuracy