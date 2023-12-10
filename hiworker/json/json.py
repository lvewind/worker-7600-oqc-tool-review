# -*- coding: UTF-8 -*-
# JSON数据读写模块
import os
import json
import zipfile


class JsonReadWrite:
    def __init__(self, file_path: str, json_file="", zip_file="", zip_pwd="U2FsdGVkX1826P+lqv/SP5kHh4PcuUpf1OgQF4CeuZg="):
        """
        初始化Json文件读写类
        :param file_path: 文件路径
        :param json_file: 文件名称
        :param zip_file: 压缩包名称
        :param zip_pwd: zip解压密码
        """
        self.file_path = file_path
        self.json_file = json_file
        self.zip_file = zip_file
        self.zip_pwd = zip_pwd

    def load_single_json_file(self):
        """
        # 加载单个JSON文件(返回任意数据类型)
        :return:
        """
        if self.json_file:
            json_data = []
            # 路径不存在时，创建路径
            if not os.path.exists(self.file_path):
                os.makedirs(self.file_path, exist_ok=True)

            try:
                main_path = os.path.abspath("..")
                main_path = '/'.join(main_path.split('\\'))
                file = main_path + "/" + self.file_path + self.json_file
                if os.path.exists(file):
                    with open(file, "r", encoding="UTF-8") as fr:
                        json_data = json.loads(fr.read())
                else:
                    print(file, "文件不存在")
                    self.save_json(json_data)
                    print(file, "文件创建成功")

            except json.decoder.JSONDecodeError:
                print("未能成功读取" + self.file_path + self.json_file + "文件数据")
            return json_data
        else:
            return []

    def load_multiple_json_file_from_path(self):
        """
        # 加载目录下所有JSON文件
        :return: 返回JSON数据字典
        """
        # 定义用于载入当前目录所有JSON数据的字典
        all_data_dict = {}
        # 路径不存在时，创建路径
        if not os.path.exists(self.file_path):
            os.makedirs(self.file_path, exist_ok=True)
            return False
        else:
            json_file_list = os.listdir(self.file_path)
            for json_file_name in json_file_list:
                if ".json" in json_file_name:
                    try:
                        with open(self.file_path + json_file_name, "r", encoding="utf-8") as fr:
                            temp_dict = json.loads(fr.read())
                    except json.decoder.JSONDecodeError:
                        pass
                    if temp_dict:
                        all_data_dict.update(temp_dict)
        return all_data_dict

    def load_multiple_json_file_from_zip(self):
        """
        # 加载目录下所有zip中的所有JSON文件
        :return:
        """
        # 定义用于载入当前目录所有JSON数据的字典
        all_data_dict = {}
        # 路径不存在时，创建路径
        if not os.path.exists(self.file_path):
            os.makedirs(self.file_path, exist_ok=True)
            print("路径不存在")
            return False
        elif os.path.exists(self.file_path + self.zip_file):  # 压缩包存在
            zf = zipfile.ZipFile(self.file_path + self.zip_file)
            # 列出压缩包内的JSON文件
            json_file_list = zf.namelist()
            # 解压文件并读取内容转为字典
            for json_file_name in json_file_list:
                if ".json" in json_file_name:
                    source_binary = zf.read(json_file_name, pwd=self.zip_pwd.encode('utf-8'))
                    json_decode = source_binary.decode()
                    try:
                        temp_dict = json.loads(json_decode)
                        all_data_dict.update(temp_dict)
                    except json.decoder.JSONDecodeError:
                        pass
            # print(all_data_dict)
            return all_data_dict
        else:
            print("压缩包不存在")
            return False

    def save_json(self, new_data):
        """
        # 将数据写入JSON文件
        :param new_data:
        :return:
        """
        # 路径不存在时，创建路径
        if not os.path.exists(self.file_path):
            os.makedirs(self.file_path, exist_ok=True)

        # 打开用于写入数据的JSON文件
        fw = open(self.file_path + self.json_file, "w", encoding="utf-8")
        # 把字典转化为json写入到文件
        fw.write(str(json.dumps(new_data, ensure_ascii=False)))
        fw.close()
