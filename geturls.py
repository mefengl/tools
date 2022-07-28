import sys
import re
def get_args():
    args = sys.argv
    # 获取-i,-o,--name,--season参数
    input_file,output_file,name,season_number = None,None,None,None
    for i in range(1, len(args)):
        if args[i] == "-i":
            input_file = args[i+1]
        elif args[i] == "-o":
            output_file = args[i+1]
        elif args[i] == "--name":
            name = args[i+1]
        elif args[i] == "--season":
            season_number = int(args[i+1])
    if input_file == None or output_file == None or name == None or season_number == None:
        print("Usage: python geturls.py -i input_file -o output_file --name name --season season_number")
        print("input_file",input_file,"output_file",output_file,"name",name,"season_number",season_number)
        sys.exit()
    return {"input_file": input_file, "output_file": output_file, "name": name, "season_number": season_number}

# 调用get_args函数获取参数
args = get_args()
with open(args["input_file"], 'r') as f:
    contents = f.read()
    # find all urls by re
    all_urls = re.findall(r"'([^\']+?ixigua[^\']+?)'", contents)
    # 去重
    urls = []
    [urls.append(url) for url in all_urls if url not in urls]
#将urls写入文件
with open(args[ "output_file" ], 'w') as f:
    index = 1
    for url in urls:
        f.write(url + '\n')
        f.write(' out='+args["name"]+'_'+str(args["season_number"]).zfill(2)+'_'+str(index).zfill(2)+'.mp4'+'\n')
        # --max-concurrent-downloads limits the number of items which are downloaded concurrently. --split and --min-split-size affect the number of connections inside each item
        f.write(' max-concurrent-downloads=20'+'\n')
        f.write(' split=40\n')
        f.write(' max-connection-per-server=16\n')
        index += 1
