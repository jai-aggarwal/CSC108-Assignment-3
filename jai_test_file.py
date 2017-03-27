data_file = open("data.txt", "r")
good_read = data_file.readlines()
def list_clean_up(lst):
    for i in lst:
        lst[lst.index(i)] = i.strip()
    return lst
def data_preprocess(data_file):
    list_clean_up(data_file)
    new_list=[]
    while data_file != []:
        index = data_file.index("END")
        sub_list = data_file[:index]
        data_file = data_file[index+1:]  
        new_list.append(sub_list)
    return new_list
def process_data(data):
    new_data = data_preprocess(data)
    twitter_dict = {}
    for sub_list in new_data:
        sub_dict = {}
        sub_dict["name"] = sub_list[1]
        sub_dict["location"] = sub_list[2]
        sub_dict["web"] = sub_list[3]
        #bio in list form, fix
        sub_dict["bio"] = sub_list[4 : sub_list.index("ENDBIO")]
        sub_dict["following"] = sub_list[sub_list.index("ENDBIO") + 1:]
        twitter_dict[sub_list[0]] = sub_dict
    return twitter_dict
#hello
        

        
        
        
    
    

print(process_data(good_read))
