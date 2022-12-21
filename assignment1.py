#1.1 create  directory
import os
os.makedirs("/Users/zicheng/Desktop/czc")
print("success")
#1.2 delete  directory
os.rmdir("/Users/zicheng/Desktop/czc")
print("success")
#1.3 List files and subdiectories
import os
list1 = os.listdir("/Users/zicheng/Desktop")
print(list1)
# os.path.split("/Users/zicheng/Desktop")
# 1.4 Move file or subdirectory to another location
os.makedirs("/Users/zicheng/Desktop/czc_1")
shutil.move('/Users/zicheng/Desktop/czc_1','/Users/zicheng/Desktop/czc')

#2.1 Create binary file
import os
f=open('/Users/zicheng/Desktop/hello_1.docx','rb')
print(f.read())
f.close()
msg = "hello py"
data = msg.encode("utf-8")
print(data, type(data))

file = open('/Users/zicheng/Desktop/hello_1.docx','wb')
file.write(data)
file.close()

# 2.2 Delete binary file
os.remove('/Users/zicheng/Desktop/test.pdf')

# 2.3 Move binary file
import shutil
shutil.move('/Users/zicheng/Desktop/test_1.png','/Users/zicheng/Desktop/test')

# 2.4 Move binary file

f= open('/Users/zicheng/Desktop/test_2.docx','rb+')
print(f.readlines())
f.close()

# 3.1 Create log text file
f=open('/Users/zicheng/Desktop/test_log_2.txt','w+')
print(f.read())
f.close()

# 3.2 delete log text file
os.remove('/Users/zicheng/Desktop/test_log_2.txt','w+')

# 3.3  Move log text file
import shutil
shutil.move('/Users/zicheng/Desktop/test_log_2.txt','/Users/zicheng/Desktop/test')

# 3.4 Readfile (returns file content)
f= open('/Users/zicheng/Desktop/test/test_log_2.txt','w+')
f.write("hi py")
print(f.readlines())
f.close()

# 3.5 Append a line to the end of the log text file
f = open('/Users/zicheng/Desktop/test/test_log_2.txt','a+', encoding = 'utf-8')
f.writelines('mamami')
f.close()


def _init_(self, name, max_q_length=10086, max_data_size=13800, memory_limit=13800138, fs=None, persist_method=None,
           persist_params=None, file_io=None, db_io=None):
    self.name = name
    self.max_q_length = max_q_length
    self.max_data_size = max_data_size
    self.memory_limit = memory_limit
    self.fs = fs
    self.persist_method = persist_method
    self.persist_params = persist_params
    self.file_io = file_io
    self.db_io = db_io
    self.is_io = fs.not_bad(file_io)
    self.queue = []
    self.status = True
    self.meta_dict = {}
    self.usage_pct = 0
f7 = open('/Users/zicheng/Desktop/test/test_log_2.txt','a+', encoding = 'utf-8')
buffer = Buffer('test', fs = f7 )
# Push element
for i in range (10):
    buffer.push(i, meta_dict = {'pkey':i},verbose=True)
