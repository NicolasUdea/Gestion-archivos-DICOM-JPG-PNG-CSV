import pydicom
import os


class DICOM:
    def __init__(self, path):
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
        for ds in self.__ds:
            self.__metadata.append(ds.dir())

    def get_metadata(self, file=0):
        """Creates a list of metadata for each DICOM file, returned as a table."""
        table = ""
        iters = [iter(self._DICOM__metadata[file])] * 4
        for columns in zip(*iters):
            for column in columns:
                table += f'{column:40}'
            table += "\n"
        return table

    # Método que identifique los campos que contiene información del paciente y los muestre en pantalla.
    def get_patient_info(self, file=0):
        """Displays fields containing patient information"""
        patient_info = []
        for element in self._DICOM__metadata[file]:
            if 'Patient' in element:
                patient_info.append(element)
        return patient_info

test = DICOM('datos/Sarcoma/')
a = test.get_metadata(1)
print(a)
b = test.get_patient_info(1)
print(b)
