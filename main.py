from funciones import *
from DICOM import *
from CELLS import *


def main():
    print(sep())
    print("Welcome to the DICOM and CELLS program!")
    print(sep())
    while True:
        menu1 = intChecker("""Select an option:
        1. View DICOM info
        2. View CELL images
        3. Exit
        > """)
        print(sep())
        if menu1 == 1:  # View DICOM info
            print("DICOM images")
            dicom = DICOM("datos/Sarcoma/")
            print(sep())
            while True:
                menu2 = intChecker("""Select an option:
                1. View DICOM info (metadata)
                2. View patient info (and anonymize)
                3. Anonymize all DICOM files in a directory
                4. Equalize histogram
                5. Compare images (original and equalized)
                6. Exit to main menu
                > """)
                print(sep())
                if menu2 == 1:  # View DICOM info
                    print("DICOM metadata")
                    print(sep())
                    print(dicom.get_table_metadata())
                    print(sep())
                    pressEnter()
                elif menu2 == 2:  # View patient info
                    print("Patient info")
                    print(sep())
                    dicom.anonymize_patient_info()
                    print(sep())
                    pressEnter()
                elif menu2 == 3:  # Anonymize all DICOM files in a directory
                    print("Anonymize all DICOM files in a directory")
                    print(sep())
                    dicom.anonymize_directory("datos/Sarcoma/", "anon/")
                    print(sep())
                    pressEnter()
                elif menu2 == 4:  # Equalize histogram
                    print("Equalize histogram")
                    print(sep())
                    dicom.equalize_image()
                    print(sep())
                    pressEnter()
                elif menu2 == 5:  # Compare images
                    print("Compare images")
                    print(sep())
                    dicom.compare_images()
                    print(sep())
                    pressEnter()
                elif menu2 == 6:  # Exit to main menu
                    print("Exiting to main menu...")
                    print(sep())
                    break
                else:
                    print("Invalid option.")
                    print(sep())
        elif menu1 == 2:  # View CELL images
            print("CELL images")
            cells = CELLS("cells/")
            print(sep())
            while True:
                menu2 = intChecker("""Select an option:
                1. View histogram
                2. Scale and crop
                3. Compare images (original and cropped)
                4. Exit to main menu
                > """)
                print(sep())
                if menu2 == 1:  # View histogram
                    print("Histogram")
                    print(sep())
                    cells.create_histogram()
                    print(sep())
                    pressEnter()
                elif menu2 == 2:  # Scale and crop
                    print("Scale and crop")
                    print(sep())
                    cells.scale_and_crop()
                    print("Modified image saved in modified_cells/")
                    print(sep())
                    pressEnter()
                elif menu2 == 3:  # Compare images
                    print("Compare images")
                    print(sep())
                    cells.compare_images()
                    print(sep())
                    pressEnter()
                elif menu2 == 4:  # Exit to main menu
                    print("Exiting to main menu...")
                    print(sep())
                    break
                else:
                    print("Invalid option.")
                    print(sep())
        elif menu1 == 3:  # Exit
            print("Exiting...")
            print(sep())
            break
        else:
            print("Invalid option.")
            print(sep())


if __name__ == '__main__':
    main()
