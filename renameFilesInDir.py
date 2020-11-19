import os
from shutil import copyfile, copy

PATH2GO = r'C:\Users\kmout\projects\REM_HAIR\benchmark-hair-removal\my_images_test2_shallow_ann'


# 010210
# 033439
# 033439b
# 233750
# run_20201011_032429-20201028T163120Z-001\run_20201011_032429
# drive-download-20201028T163559Z-001\20201024_032650
# 20201024_215502
# 20201025_030235
# 20201025_031526 #
# same: 20201113_024346, 20201113_013929,20201113_020930, 20201113_015508


def main():
    path = r'C:\Users\kmout\Downloads\20201113_015508-20201113T074341Z-001\20201113_015508'
    find_what = 'inpaintcoh'  # "regionfill" 'inpaintcoh'
    replace_with = 'KD508'  # "KDshRE"
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
