import matplotlib.pyplot as plt
from torchvision.utils import make_grid
from ddpm.config import BaseConfig
from ddpm.data import get_dataloader
from ddpm.data import inverse_transform

if __name__ == '__main__':

    loader = get_dataloader(dataset_name=BaseConfig.DATASET,
                            batch_size=128,
                            device='cpu')

    plt.figure(figsize=(12, 6), facecolor='white')

    for b_image, _ in loader:
        b_image = inverse_transform(b_image).cpu()
        grid_img = make_grid(b_image / 255.0, nrow=16, padding=True, pad_value=1, normalize=True)
        plt.imshow(grid_img.permute(1, 2, 0))
        plt.axis("off")
        plt.show()
        break
