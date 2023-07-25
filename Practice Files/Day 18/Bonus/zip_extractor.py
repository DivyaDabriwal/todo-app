import zipfile
import pathlib


def archive_extractor(file, path):
    destination_path = pathlib.Path(path, 'compressed')
    with zipfile.ZipFile(file, 'r') as archive:
        archive.extractall(destination_path)


if __name__ == '__main__':
    archive_extractor('D:/Udemy Courses/Python/Workspace/files/compressed.zip',
                      'D:/Udemy Courses/Python/Workspace/files')
