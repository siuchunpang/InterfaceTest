import re, json, os


def modify(file_name):
    file_list = []
    print("处理中...")
    with open("../" + file_name, "r") as f:
        for line in f.readlines():
            line = line.strip('\n')
            file_list.append(line)
        # print(file_list)

    is_modify = 0
    for index, file_list_str in enumerate(file_list):
        try:
            json_str = re.findall("{.*}", file_list_str)
            if json_str:
                json_loads = json.loads(json_str[0])
                if json_loads:
                    new_dict = {}
                    for k, v in json_loads.items():
                        new_k = "\"" + k + "\""
                        new_v = "\"" + str(json_loads["%s" % k]) + "\""
                        new_dict[new_k] = new_v

                    json_dumps = json.dumps(new_dict)
                    json_new = str(new_dict)
                    str_new = "\"" + json_new.replace("\'", "\"") + "\""
                    file_list[index] = file_list_str.replace(json_str[0], str_new)
                    is_modify += 1

        except Exception as e:
            # print(e)
            pass

    # print(file_list)
    # 加\n
    for i in range(len(file_list)):
        file_list[i] = file_list[i] + "\n"

    with open("../" + file_name, "w") as f:
        f.writelines(file_list)

    print("处理[%s]成功，处理了%d条数据" % (file_name, is_modify))


if __name__ == '__main__':
    print("输入以下指令执行对应操作：")
    print("输入1：处理data目录所有的csv文件")
    print("输入2：指定处理的csv文件")
    chance = input("请输入指令：")

    if chance == "1":
        print("输入的是1")
        files = os.listdir("../")
        for file in files:
            if ".csv" in file:
                modify(file)

    elif chance == "2":
        file = input("需要处理的csv文件:")
        modify(file)
    else:
        print("输入有误，请重新输入")
