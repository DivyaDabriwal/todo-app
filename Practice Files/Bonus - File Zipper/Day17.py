import zipfile
import pathlib


def archive_creator(destination_dir, filepaths):
    destination_path = pathlib.Path(destination_dir, 'compressed.zip')
    with zipfile.ZipFile(destination_path, 'w') as archive:
        for file in filepaths:
            filepath = pathlib.Path(file)
            archive.write(file, arcname=filepath.name)


if __name__ == '__main__':
    archive_creator('D:/Udemy Courses/Python/Workspace/files',
                    ['D:/Udemy Courses/Python/Workspace/files/a.txt',
                     'D:/Udemy Courses/Python/Workspace/files/b.txt',
                     'D:/Udemy Courses/Python/Workspace/files/c.txt'])
