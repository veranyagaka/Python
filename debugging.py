#python debugging with pdb
import pdb; pdb.set_trace()
#another way is breakpoint() by default will call the above
#another way is running on the command line
#python-3 -m pdb app.py arg1 arg2
file_name  = __file__
print(f'path={file_name}')