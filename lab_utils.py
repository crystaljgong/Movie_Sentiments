import PIL, torch
from PIL import Image
import numpy as np
import IPython.display
from io import BytesIO
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

class UnNormalize(object):
    def __init__(self, mean, std):
        self.mean = mean
        self.std = std
    def __call__(self, tensor):
        for t, m, s in zip(tensor, self.mean, self.std):
            t.mul_(s).add_(m)
        return tensor
    
def pil2tensor(img):
    return transforms.ToTensor()(img)

def tensor2pil(tensor):
    return transforms.ToPILImage()(tensor)

def show_image(input_image):
    f = BytesIO()
    if type(input_image) == torch.Tensor:
        input_image = np.uint8(input_image.mul(255).numpy().transpose(1, 2, 0)) 
        Image.fromarray(input_image).save(f, 'png')
    else:
        input_image.save(f, 'png')
    IPython.display.display(IPython.display.Image(data = f.getvalue()))

def plot_loss(trainingLoss, validationLoss, epochs):
    plt.figure(1)
    plt.plot(epochs,trainingLoss, label='Training loss')
    plt.plot(validationLoss, label='Validation loss')
    plt.legend(loc='upper right')
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Training and validation loss over each epoch")

def plot_accuracy(trainingAccuracy, validationAccuracy, epochs):
    plt.figure(2)
    plt.plot(epochs, trainingAccuracy, label='Training accuracy')
    plt.plot(validationAccuracy, label='Validation accuracy')
    plt.legend(loc='lower right')
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.title("Training and validation accuracy over each epoch")
    
def generate_plots(trainingLoss, validationLoss, trainingAccuracy, validationAccuracy, epochs):
    epochs = np.arange(0,epochs)
    plot_loss(trainingLoss, validationLoss, epochs)
    plot_accuracy(trainingAccuracy, validationAccuracy, epochs)
