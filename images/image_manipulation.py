import tempfile

from PIL import Image


class ImageResizing:
    @staticmethod
    def reduceImageSize(image):
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
        temp_file_name = temp_file.name
        image_resize = Image.open(image)
        image_resize.save(temp_file_name, quality=50, optimize=True)
        return temp_file_name

    @staticmethod
    def close_image(image):
        """
        Closes opened image
        :param image: An image
        :return: None
        """
        image.close()

    @staticmethod
    def removing_file(path):
        """
        Removing file by path
        :param path: The path of a file
        :return: None
        """
        # Try/except library import
        try:
            import os  # Miscellaneous OS library
        except ImportError as ImportException:
            raise ImportError("Cannot import needed libraries. Please contact administrator and give the code FN0001")
        os.remove(path)

