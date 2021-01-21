import glob
import shutil
import tqdm


def main():
    file_lists = glob.glob('./test/**/*.jpg')
    for idx in tqdm.tqdm(file_lists, total=len(file_lists)):
        shutil.copyfile(idx, f"./test_v1/{idx.split('/')[-1]}")


if __name__ == '__main__':
    main()