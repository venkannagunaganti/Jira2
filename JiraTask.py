from datetime import datetime
from pathlib import Path
class LogFile:
#writing to the log file function
  path = 'C:/Users/GUNAGANTI VENKANNA/Documents/file.txt'
  msg = ''
  with open(path,'w') as file:
    file.write(msg)

    @staticmethod
    def write_to_log_file(file_name,msg,line_number):
        p = Path(LogFile.path)
        time_stamp = datetime.fromtimestamp(p.stat().st_mtime).isoformat()
        with open(LogFile.path,'a+') as file:
            file.write(time_stamp+' '+file_name+' '+str(line_number)+' '+msg+'\n')
    @staticmethod
    def print_line(path,line_number):
        with open(path,'r') as file:
            lines=file.readlines()
            file.close()
            line=lines[line_number-1]
            print(line+'')


