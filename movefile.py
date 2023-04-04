import os
import shutil
#from glob import glob
class File():
    
    def __init__(self):
        self.fileList = []

    """
    递归列表文件
    """
    def recursion_file(self, filepath):
        files = os.listdir(filepath)
        for file in files:
            fi_d = os.path.join(filepath, file)
            if os.path.isdir(fi_d):
                self.recursion_file(fi_d)
            else:
                self.fileList.append(fi_d)

    """
    获取文件列表
    """
    def get_file_list(self, filepath):
        self.recursion_file(filepath)
        return self.fileList


#指定文件路径获取文件最后文件的路径包含文件
#如：D:\test\file.txt 返回的结果为：file.txt
def get_file_name(path):
    return os.path.basename(path)
    
   
# 创建目录
def mkdir(path):
    # 去除尾部 \ 符号 
    pathx = path.strip().rstrip("\\")
    #print(f'pathx={pathx}')
    
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(pathx)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False

#移动文件,移动文件比拷贝文件速度快
#src_dir 指定要拷贝或者移动文件的源目录
#dst_dir 指定要拷贝或者移动文件的目标目录
#flag True为拷贝，False 代表移动
#return True为成功，False 代表失败
def copy_or_move_files(src_dir,dst_dir,flag):
    fileObj = File()
    #指定新的路径不存在就创建
    mkdir(dst_dir)
    cout = 0
    try:
        for file_path in fileObj.get_file_list(src_dir):
            # 判断是拷贝就处理
            if(flag==True ):
                shutil.copy(file_path, dst_dir+'\\' + get_file_name(file_path))
                cout +=1
            else:
                shutil.move(file_path, dst_dir+'\\' + get_file_name(file_path))
                cout +=1
        
        print(f'file cout {cout}')
        return True
    except Exception as e:
        print(f'处理文件失败,失败原因为:{e}' )
        return False
      
