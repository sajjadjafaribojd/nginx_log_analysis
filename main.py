import re

def remove_charecter(line):
    try:
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
    except Exception as e:
          return e     

def remove_charecter_time(line):
    try:
        b_ch = "\["
        pattern  = ".*" + b_ch 
        strValue = re.sub(pattern,'', line )

        a_ch = "\]"
        pattern  = a_ch + ".*"  
        strValue = re.sub(pattern,'', strValue )

        pattern="\+0000"
        strValue = re.sub(pattern,'', strValue).strip()

        result=strValue.split(':',1) #string.split(separator, maxsplit) # maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"

        c_ch = "\:"
        pattern  = c_ch + ".*"  
        trValue = re.sub(pattern,'', result[1] )
        return trValue  #['23']
    except Exception as e:
          return e    

def remove_charecter_with_hour(line): 
    try:
        b_ch = "\["  #09/Sep/2021:11:09:31 +0000]
        pattern  = ".*" + b_ch 
        strValue = re.sub(pattern,'', line )

        a_ch = "\]" # 9/Sep/2021:11:09:31 +0000
        pattern  = a_ch + ".*"  
        strValue = re.sub(pattern,'', strValue )

        pattern="\+0000" # 9/Sep/2021:11:09:31
        strValue = re.sub(pattern,'', strValue).strip()

        result=strValue.split(':',1) #string.split(separator, maxsplit) # maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences" ['9/Sep/2021','11:09:31']
        
        c_ch = "\:" 
        pattern  = c_ch + ".*" 
        strValue=re.sub(pattern,'', result[1]).strip() #11
        final=result[0]+':'+strValue # 9/Sep/2021 + 11 = 9/Sep/2021:11
    except Exception as e:
          return e      

    return final  #['9/Sep/2021:11']

def analise_date(date_list):
    try:
        duplicate_dict={}
        for i in date_list:
            duplicate_dict[i]=date_list.count(i)
        find_max = max(duplicate_dict, key=duplicate_dict.get) #17/Oct/2021
        find_min = min(duplicate_dict, key=duplicate_dict.get) #17/Oct/2021
        all_values =max(duplicate_dict.values()) #712
        all_values_min =min(duplicate_dict.values()) #712
        result_sum=sum(duplicate_dict.values())/len(duplicate_dict.values()) #78.12109375 
        return [duplicate_dict,find_max,all_values,find_min,all_values_min,result_sum]
    except Exception as e:
          return e 

def requestsـperـday(file_name):
    try:
        file=open(file_name,'r')
        date_list=[]
        couter_line=0
        for line in file:
            my_list=remove_charecter(line) #['21/May/2022', '23:02:08']
            date_list.append(my_list[0])   #21/May/2022
            couter_line=couter_line+1
        count_month=analise_date(date_list)
        return count_month  
    except Exception as e:
          return e       

def requestsـperـsecond(file_name):
    try:
        file=open(file_name,'r')
        time_list=[]
        for line in file:
            my_list=remove_charecter(line) #['21/May/2022', '23:02:08']
            time_list.append(my_list[1])   #23:02:08      

        count_month=analise_date(time_list)
        return count_month
        #return time_list
        file.close()
    except Exception as e:
          return e         

def Frequencyـrequestsـbyـhour(file_name):
    try:
        file=open(file_name,'r')
        time_list=[]
        for line in file:
            my_list=remove_charecter_time(line) #['23']
            time_list.append(my_list)  

        count_month=analise_date(time_list)
        return count_month
        file.close() 
    except Exception as e:
          return e

def requestsـperـhour(file_name):
    try:
        file=open(file_name,'r')
        date_list=[]
        couter_line=0
        for line in file:
            my_list=remove_charecter_with_hour(line) #09/Sep/2021:11
            date_list.append(my_list)   #21/May/2022:23
            couter_line=couter_line+1
        count_month=analise_date(date_list)
        file.close()
        return count_month    
    except Exception as e:
          return e

result=requestsـperـday('log/waitress.txt')
print(
    '******************************************************************************************************************************\n'
    #'Number of requests per day:'+str(result[0]) +'\n'
    'The busiest day:          ' +result[1] +' - With the number of requests: '+str(result[2])+'\n'
    'The most secluded day:    ' +result[3] +' - With the number of requests: '+str(result[4])+'\n'
    'Average requests per day: ' +str(result[5])+'\n'
    '******************************************************************************************************************************'
)

result=requestsـperـhour('log/waitress.txt')
print(
    #'Number of requests per hour:'+str(result[0]) +'\n'
    'The busiest hour:          ' +result[1] +' - With the number of requests: '+str(result[2])+'\n'
    'The most secluded hour:    ' +result[3] +' - With the number of requests: '+str(result[4])+'\n'
    'Average requests per hour: ' +str(result[5])+'\n'
    '******************************************************************************************************************************'
)

result=requestsـperـsecond('log/waitress.txt')
print(
    #'Number of requests per second:'+str(result[0]) +'\n'
    'The busiest second:          ' +result[1] +' - With the number of requests: '+str(result[2])+'\n'
    'The most secluded second:    ' +result[3] +' - With the number of requests: '+str(result[4])+'\n'
    'Average requests per second: ' +str(result[5])+'\n'
    '******************************************************************************************************************************'
)

result=Frequencyـrequestsـbyـhour('log/waitress.txt')
print(
    #'Number of requests per hour:'+str(result[0]) +'\n'
    'The busiest hour in a year:          ' +result[1] +' - With the number of requests: '+str(result[2])+'\n'
    'The most secluded hour in a year:    ' +result[3] +' - With the number of requests: '+str(result[4])
)




#Sample data in the file 
#str='85.41.31.21 5.11.66.158 [18/May/2022:15:05:50 +0000] POST /test/domain.ir/ HTTP/1.1 200 '


