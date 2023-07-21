import inspect
import Functionalities
import JiraTask
from pathlib import Path
from datetime import datetime

#messages
f=inspect.currentframe()
critical_msg="CRITICAL:the internet is not working"
debug_msg="DEBUG:This is just a harmless debug message"
error_message="ERROR:this is an error message"
warning_message="WARNING:this is warning message"
info="INFO:this is info"
file=JiraTask.LogFile.path
line_number=1
Msg_std_list=[critical_msg,debug_msg,info,warning_message,error_message]
#functions calling

Functionalities.Crititcal().critical(inspect.getframeinfo(f).filename,critical_msg,inspect.getframeinfo(f).lineno)
# Functionalities.Debug().debug(inspect.getframeinfo(f).filename,debug_msg,inspect.getframeinfo(f).lineno)
# Functionalities.Information().info(inspect.getframeinfo(f).filename,info,inspect.getframeinfo(f).lineno)
# Functionalities.Warning().warn(inspect.getframeinfo(f).filename,warning_message,inspect.getframeinfo(f).lineno)
# Functionalities.Error().err(inspect.getframeinfo(f).filename,error_message,inspect.getframeinfo(f).lineno)
# LogFile.print_line(status.path,status.line_number)