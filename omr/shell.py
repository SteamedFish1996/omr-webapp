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
        return sout.decode(encoding='utf-8',errors='ignore').split('\n')



if __name__ == '__main__':
    import os
    basepath = os.path.dirname(__file__)  # 当前文件所在路径
    #python27_dir = 'C:/Users/92538/Anaconda3/envs/moonlight/python.exe'
    testfile_dir = basepath+'/../backup/test.py'
    cmd1 = "activate py27"
    cmd2 = 'python' + ' ' +  testfile_dir
    cmd = cmd1 + '&&' + cmd2
    print(cmd)
    shell = Shell()
    returncode, sout, serr, pid = shell.run_cmd(cmd)
    results = shell.cmd_result_list(sout)
    for l in results:
        print(l)



