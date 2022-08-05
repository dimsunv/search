import glob
import mmap

trgFolder = r'e:\terraform-provider-aws-main\**\*.go'
trgExpr = b'DataSourcesMap'
for item in glob.glob(f'{trgFolder}', recursive=True):
    with open(item, 'rb', 0) as file:
        try:
            s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
            if s.find(trgExpr) != -1:
                print(item)
        except ValueError:
            print(item, "Пустой файл")