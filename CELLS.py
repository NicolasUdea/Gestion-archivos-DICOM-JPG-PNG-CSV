import cv2
import matplotlib.pyplot as plt
import os


class CELLS:
    def __init__(self, dir_path):
        self.__images = [
            cv2.imread(os.path.join(dir_path, img)) for img in os.listdir(dir_path) if img.endswith(".jpg")
        ]
        self.__image_names = [img for img in os.listdir(dir_path) if img.endswith(".jpg")]

    def create_histogram(self, file=0):
        """Creates a histogram of the image matrix."""
        img = self.__images[file]
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            histr = cv2.calcHist([img], [i], None, [256], [0, 256])
            plt.plot(histr, color=col)
            plt.xlim([0, 256])
        plt.title('Histograma')
        plt.show()

    def scale_and_crop(self, file=0, scale_percent=60, x=0, y=0, w=250, h=250):
        """Scales and crops the image, and saves the modified image."""
        img = self.__images[file]

        # Scale
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        # Crop
        crop_img = resized[y:y+h, x:x+w]

        # Save the image
        if not os.path.exists('modified_cells'):
            os.makedirs('modified_cells')
        cv2.imwrite(f'modified_cells/modified_{self.__image_names[file]}', crop_img)

    def compare_images(self, file=0, scale_percent=60, x=0, y=0, w=250, h=250):
        """Creates a figure with two subplots to compare the original and cropped images."""
        img = self.__images[file]

        # Scale
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        # Crop
        crop_img = resized[y:y + h, x:x + w]

        # Create a figure with two subplots
        fig, axs = plt.subplots(1, 2, figsize=(10, 5))

        # Display the original image in the first subplot
        axs[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        axs[0].set_title('Imagen Original')

        # Display the cropped image in the second subplot
        axs[1].imshow(cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB))
        axs[1].set_title('Imagen Recortada')

        # Save the figure
        plt.savefig(f'modified_cells/comparison_{self.__image_names[file]}')
        print(f"Comparison image saved as comparison_{self.__image_names[file]}")


cell = CELLS('cells')
cell.create_histogram()
cell.scale_and_crop()
cell.compare_images()
