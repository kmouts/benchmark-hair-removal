import os
from shutil import copyfile, copy

PATH2GO = r'C:\Users\kmout\projects\REM_HAIR\benchmark-hair-removal\my_images_test2_shallow_ann'


# 010210
# 033439
# 033439b
# 233750

def main():
    path = r'C:\Users\kmout\Downloads\drive-download-20201012T062758Z-001\run_20201011_010210'
    find_what = 'regionfill'  # "regionfill" 'inpaintcoh'
    replace_with = 'KD10RE'  # "KDshRE"
    count_files = 0

    for path, subdirs, files in os.walk(path):
        for name in files:
            if (find_what in name.lower()):
                split_name = name.split('_')  # IMD006_mask_44no_hair_inpaintcoh.bmp
                file_path = os.path.join(path, name)
                new_name = os.path.join(path, 'modified_' + replace_with + '_' + split_name[
                    0] + '.bmp')  # modified_KDshRE_IMD006
                os.rename(file_path, new_name)
                copy(new_name, os.path.join(PATH2GO, split_name[0]))
                count_files = count_files + 1

    print('Files copied: {}'.format(count_files))


if __name__ == '__main__':
    main()
