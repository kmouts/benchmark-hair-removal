import os


def main():
    path = r'C:\Users\kmout\Downloads\run1-20200911T170710Z-001\run1'
    find_what = 'inpaintcoh' # "regionfill"
    replace_with = 'KDshIN' # "KDshRE"

    for path, subdirs, files in os.walk(path):
        for name in files:
            if (find_what in name.lower()):
                split_name = name.split('_') # IMD006_mask_44no_hair_inpaintcoh.bmp
                file_path = os.path.join(path, name)
                new_name = os.path.join(path, 'modified_'+ replace_with +'_' + split_name[0]+'.bmp') # modified_KDshRE_IMD006
                os.rename(file_path, new_name)


if __name__ == '__main__':
    main()