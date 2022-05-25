from operator import le
from posixpath import split
import re
from typing import Counter

def remove_charecter(line):
    b_ch = "\["
    pattern  = ".*" + b_ch 
    strValue = re.sub(pattern,'', line )

    a_ch = "\]"
    pattern  = a_ch + ".*"  
    strValue = re.sub(pattern,'', strValue )

    pattern="\+0000"
    strValue = re.sub(pattern,'', strValue).strip()

    result=strValue.split(':',1) #string.split(separator, maxsplit) # maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
    return result  #['21/May/2022', '23:02:08']

def analise_date(date_list):
    duplicate_dict={}
    for i in date_list:
        duplicate_dict[i]=date_list.count(i)
    find_max = max(duplicate_dict, key=duplicate_dict.get) #17/Oct/2021
    all_values =max(duplicate_dict.values()) #712
    result_sum=sum(duplicate_dict.values())/len(duplicate_dict.values()) #78.12109375 
    return [duplicate_dict,find_max,all_values,result_sum]
     

def main_function(file_name):
    file=open(file_name,'r')
    date_list=[]
    couter_line=0
    for line in file:
        my_list=remove_charecter(line) #['21/May/2022', '23:02:08']
        date_list.append(my_list[0])   #21/May/2022
        couter_line=couter_line+1

    count_month=analise_date(date_list)
    return count_month,couter_line
    file.close()    



print(main_function('log/access.log'))


#Sample data in the file 
#str='85.41.31.21 5.11.66.158 [18/May/2022:15:05:50 +0000] POST /test/domain.ir/ HTTP/1.1 200 '


