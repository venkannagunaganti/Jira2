import JiraTask
critical_msg="CRITICAL:the internet is not working"
debug_msg="DEBUG:This is just a harmless debug message"
error_message="ERROR:this is an error message"
warning_message="WARNING:this is warning message"
info="INFO:this is infoo"
class Crititcal:
# function to write critical msg
    @staticmethod
    def critical(file_name,msg,line_number):
        while False:
            if msg==critical_msg or msg==debug_msg or msg==error_message or msg==warning_message or msg==info:
               JiraTask.LogFile.write_to_log_file(file_name,msg,line_number)
            else:
             break
class Debug:
    @staticmethod
    def debug(file_name,msg,line_number):
        JiraTask.LogFile.write_to_log_file(file_name,msg,line_number)
class Error:
#funtion to pass error message
    @staticmethod
    def err(file_name,msg,line_number):
       JiraTask.LogFile.write_to_log_file(file_name,msg,line_number)
class Warning:
#function to pass warning message
    @staticmethod
    def warn(file_name,msg,line_number):
        JiraTask.LogFile.write_to_log_file(file_name,msg,line_number)

class Information:
#function to pass information
    @staticmethod
    def info(file_name,msg,line_number):
        JiraTask.LogFile.write_to_log_file(file_name,msg,line_number)
