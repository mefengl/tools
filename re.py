import sys
import re
def get_args():
    args = sys.argv
    # 获取-i,-o,--regex参数
    input_file,output_file,regex = None,None,None
    for i in range(1, len(args)):
        if args[i] == "-i":
            input_file = args[i+1]
        elif args[i] == "-o":
            output_file = args[i+1]
        elif args[i] == "--regex":
            regex = args[i+1]
    if input_file == None or output_file == None or regex == None:
        print("Usage: del.py -i input_file -o output_file --regex regex")
        sys.exit(1)
    # 返回字典
    return {"input_file":input_file, "output_file":output_file, "regex":regex} 

# 调用get_args函数获取参数
args = get_args()
with open(args["input_file"], 'r') as f:
    contents = f.read()
    # find all urls by re
    all_urls = re.findall(r''+args["regex"], contents)
    # 去重
    urls = []
    [urls.append(url) for url in all_urls if url not in urls]
#将urls写入文件
with open(args[ "output_file" ], 'w') as f:
    for url in urls:
        f.write(url + '\n')
