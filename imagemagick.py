import sh

def check_binaries():
    sh.ensure('convert')

def convert(from_path, to_path, filters=[]):
    result = sh.execute(['convert', from_path, *filters, to_path])
    # TODO: Error handling