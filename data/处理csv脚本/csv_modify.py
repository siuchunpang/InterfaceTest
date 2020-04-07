import re, json

file_list = []
file_name = input("需要处理的csv文件:")

print("处理中...")
with open("../" + file_name, "r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        file_list.append(line)
    # print(file_list)

for index, file_list_str in enumerate(file_list):
    try:
        is_json = 0
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

    except Exception as e:
        # print(e)
        pass

print(file_list)
for i in range(len(file_list)):
    file_list[i] = file_list[i] + "\n"
# print(file_list)


with open("../" + file_name, "w") as f:
    f.writelines(file_list)

print("处理成功")
