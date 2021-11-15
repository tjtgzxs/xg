import gzip
import shutil
import os
import time

import wget
import csv
import linecache
from shutil import copyfile
import ipywidgets as widgets
import numpy as np
import pandas as pd
import getContent
import datetime


def get_ids(country,date):

    # dataset_URL = "https://github.com/thepanacealab/covid19_twitter/blob/master/dailies/{date}/{date}_clean-dataset.tsv.gz?raw=true".format(date=date) #@param {type:"string"}
    #Downloads the dataset (compressed in a GZ format)
    #!wget dataset_URL -O clean-dataset.tsv.gz
    # wget.download(dataset_URL, out='clean-dataset.tsv.gz')
    RESOURCE_DIR="/home/ubuntu/resources/covid19_twitter/dailies/"
    if os.path.exists(f'{date}.tsv')==False:
        #Unzips the dataset and gets the TSV dataset
        with gzip.open(RESOURCE_DIR+f'{date}/{date}_clean-dataset.tsv.gz', 'rb') as f_in:
            with open(f'{date}.tsv', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
    else:
        print(f"{date}.已经存在了")

    #Deletes the compressed GZ file
    # os.unlink("clean-dataset.tsv.gz")

    #Gets all possible languages from the dataset
    df = pd.read_csv(f'{date}.tsv',sep="\t")
    lang_list = df.lang.unique()
    lang_list= sorted(np.append(lang_list,'en'))
    lang_picker = widgets.Dropdown(options=lang_list, value="en")
    filtered_language = lang_picker.value
    # If no language specified, it will get all records from the dataset
    if filtered_language == "":
        copyfile(f'{date}.tsv', f'{date}-filtered.tsv')

    # If language specified, it will create another tsv file with the filtered records
    else:
        filtered_tw = list()
        current_line = 1

        with open(f"{date}.tsv") as tsvfile:
            tsvreader = csv.reader(tsvfile, delimiter="\t")

            if current_line == 1:
                pass

                for line in tsvreader:
                    if line[3] == filtered_language and line[4]==country:
                        try:
                            content=getContent.get_content(line[0])
                            filtered_tw.append(str(content)+"\n")
                            current_line += 1
                            if current_line>=70:
                                print(f'c_line{current_line}')
                                break
                        except:
                            continue

        with open(f'pdf/{date}-filtered.tsv', 'w') as f_output:
            for item in filtered_tw:
                f_output.write(item)
if __name__=="__main__":
    t1 = time.time()
    begin=datetime.date(2020,7,26)
    end=datetime.date(2021,10,31)
    for i in range((end - begin).days + 1):
        day = begin + datetime.timedelta(days=i)
        try:
            get_ids("US", str(day))
            print(f"{day}的数据跑完")
        except Exception as e:
            print(f"{day}的数据没有跑 原因{e}")

            continue


    t2=time.time()
    print(int(t2)-int(t1))
