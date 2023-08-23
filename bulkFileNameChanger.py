import os


def change(path, new_name, new_type):
    i = 1
    for filename in os.listdir(path):
        updated_name = new_name+str(i)+new_type
        my_source = path+filename
        my_updated_dest = path+updated_name
        os.rename(my_source, my_updated_dest)
        i += 1


if __name__ == "__main__":
    change("E:/animated/Attack on titan/Attack on titan Season-02/",
           "Attack On Titan Season 2 Episode ", ".mp4")
