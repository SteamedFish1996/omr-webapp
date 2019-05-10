import subprocess
import shlex

class Shell(object):

    def run_cmd(self,cmd):
        args = shlex.split(cmd)
        res = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        res.wait()
        sout ,serr = res.communicate() 
        return res.returncode, sout, serr, res.pid

    def cmd_result_list(self,sout):
        return sout.decode(encoding='utf-8').split('\n')  



if __name__ == '__main__':
    python27_dir = 'C:/Users/92538/Anaconda3/envs/moonlight/python.exe'
    testfile_dir = 'F:/omr-webapp/backup/test.py'
    cmd = python27_dir + ' ' + testfile_dir
    print(cmd)
    shell = Shell()
    returncode, sout, serr, pid = shell.run_cmd(cmd)
    results = shell.cmd_result_list(sout)
    for l in results:
        print(l)



