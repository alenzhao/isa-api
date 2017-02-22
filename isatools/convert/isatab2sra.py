import os
from io import BytesIO
from zipfile import ZipFile


def zipdir(path, zip_file):
    """utility function to zip only SRA xmls from a whole directory"""
    # zip_file is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in [f for f in files if f in ['submission.xml', 'project_set.xml', 'run_set.xml',
                                               'experiment_set.xml', 'sample_set.xml']]:
            zip_file.write(os.path.join(root, file),
                           arcname=os.path.join(os.path.basename(root), file))

BASE_DIR = os.path.dirname(__file__)
default_config_dir = os.path.join(BASE_DIR, '..', 'config', 'xml')


def convert(source_path, dest_path, sra_settings=None):
    from isatools import isatab, sra
    import glob
    i_files = glob.glob(os.path.join(source_path, 'i_*.txt'))
    if len(i_files) == 1:
        with open(i_files[0]) as fp:
            ISA = isatab.load(fp)
            sra.export(ISA, dest_path, sra_settings=sra_settings)
            buffer = BytesIO()
            if os.path.isdir(dest_path):
                with ZipFile(buffer, 'w') as zip_file:
                    # use relative dir_name to avoid absolute path on file names
                    zipdir(dest_path, zip_file)
                    print(zip_file.namelist())
                buffer.seek(0)
                return buffer