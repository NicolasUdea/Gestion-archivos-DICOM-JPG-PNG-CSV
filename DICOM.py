import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import pydicom
import cv2
import os


class DICOM:
    def __init__(self, path):
        self._DICOM__metadata = None
        self.patient_info_tags = ['PatientID', 'PatientName', 'PatientBirthDate', 'PatientSex']  # Define patient_info_tags here
        folders = os.listdir(path)
        file_names = []
        for folder in folders:
            file_names.append(os.listdir(path + folder))
        file_paths = []
        for i in range(len(folders)):
            for file in file_names[i]:
                file_paths.append(path + folders[i] + '/' + file)
        self.__ds = []
        for file in file_paths:
            self.__ds.append(pydicom.dcmread(file))
        self.__metadata = []
        for i in self.__ds:
            self.__metadata.append(i.dir())

    def get_table_metadata(self, file=0):
        """Creates a list of metadata for each DICOM file, returned as a table."""
        table = ""
        iters = [iter(self._DICOM__metadata[file])] * 4
        for columns in zip(*iters):
            for column in columns:
                table += f'{column:40}'
            table += "\n"
        return table

    def anonymize_patient_info(self, file=0):
        """Prints patient information, replaces it with N/A, and saves the modified DICOM file."""
        ds = self.__ds[file]
        print("Patient Information:")
        for tag in self.patient_info_tags:
            if tag in ds:
                print(f"{tag}: {ds.data_element(tag).value}")
                if tag == 'PatientBirthDate':
                    ds.data_element(tag).value = "00000000"  # Use a dummy date
                elif tag == 'PatientSex':
                    ds.data_element(tag).value = "O"  # Use 'O' (Other) for sex
                else:
                    ds.data_element(tag).value = ""  # Use empty string
        ds.save_as(f"anon/anonymized_{file}.dcm")
        print(f"Anonymized DICOM file saved as anonymized_{file}.dcm")

    def anonymize_directory(self, input_dir, output_dir):
        """Anonymizes all DICOM files in a directory and saves them to another directory."""
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        for root, dirs, files in os.walk(input_dir):
            for file in files:
                if file.endswith(".dcm"):
                    ds = pydicom.dcmread(os.path.join(root, file))
                    for tag in self.patient_info_tags:
                        if tag in ds:
                            if tag == 'PatientBirthDate':
                                ds.data_element(tag).value = "00000000"  # Use a dummy date
                            elif tag == 'PatientSex':
                                ds.data_element(tag).value = "O"  # Use 'O' (Other) for sex
                            else:
                                ds.data_element(tag).value = ""  # Use empty string
                    ds.save_as(os.path.join(output_dir, f"anonymized_{file}"))
        print(f"All DICOM files in {input_dir} have been anonymized and saved to {output_dir}.")

    def equalize_image(self, file=0):
        """Equalizes the histogram of the image matrix, adds 'imagen ecualizada' text, and saves the image."""
        ds = self.__ds[file]
        img_array = ds.pixel_array  # Extract the image matrix

        # Apply histogram equalization
        img_array_equalized = cv2.equalizeHist(img_array.astype(np.uint8))

        # Convert to PIL Image for drawing text
        img_pil = Image.fromarray(img_array_equalized)

        # Draw 'imagen ecualizada' on the image
        plt.imshow(img_pil, cmap=plt.cm.bone)

        # Define the text properties
        text = 'imagen ecualizada'
        position = (img_pil.width // 2, 20)  # Adjust the y-coordinate to place the text at the top
        color = 'black'
        size = 20
        weight = 'bold'
        box_color = 'lime'

        # Add the text to the image
        plt.text(*position, text, color=color, fontsize=size, weight=weight,
                 bbox=dict(facecolor=box_color, alpha=0.5, edgecolor='black'), ha='center')

        # Save the image
        plt.savefig(f'equalized/equalized_{file}.png')
        print(f"Equalized image saved as equalized_{file}.png")


test = DICOM('datos/Sarcoma/')
test.equalize_image()
