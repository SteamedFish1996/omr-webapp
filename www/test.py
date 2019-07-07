from omr.shell import Shell
from util import os_tool

import os

basepath = os.path.dirname(__file__)  # 当前文件所在路径


def omr(image_name):
    # moonlight START
    # bazel-bin/moonlight/omr --output_type=MusicXML --output=$HOME/mozart.xml corpus/56/IMSLP56442-*.png
    #
    omr_dir = '/home/ps/zzy/music/moonlight/bazel-bin/moonlight/omr'
    output_dir = basepath + '/result'
    input_dir = basepath +  '/static/images/'
    cmd1 = "activate py27"
    if os_tool.system() == 'Linux':
        cmd1 = "source activate py27"
    cmd2 = omr_dir + ' ' + '--output_type=MusicXML'+ ' ' + '--output=' + output_dir + ' ' + input_dir + image_name
    cmd = cmd1 + ' && ' + cmd2 + ' && ' +  'python -V'
    print(cmd)
    shell = Shell()
    shell.run_cmd(cmd)
    # moonlight END
    # cnn-lstm START
    model_dir = basepath + '/../omr/cnn_rnn'
    images_dir = basepath + '/static/images/'
    cmd1 = "activate tensorflow "
    if os_tool.system() == 'Linux':
        cmd1 = "source activate tensorflow"
    cmd2 = "cd " +model_dir
    cmd3 = " python standalone_inference_over_image.py \
        --detection_inference_graph muscima-pp.pb \
        --input_image " + image_name + "--detection_label_map category_mapping.txt \
        --output_image result.jpg \
        --output_result output_transcript.txt"
    cmd = cmd1 + ' && ' + cmd2 + ' && ' +  'python -V'
    shell = Shell()
    shell.run_cmd(cmd)


if __name__ == '__main__':
    image_name = 'IMSLP00747-000.png'
    omr(image_name)


"""


pb_dir = basepath + '/../omr/cnn_rnn'
input_dir = basepath + '/images/'
output_dir = basepath + '/result'
# cnn-lstm END

testfile_dir = basepath + '/../omr/cnn_rnn'

cmd = 'python -V'
returncode, sout, serr, pid = shell.run_cmd(cmd)
results = shell.cmd_result_list(sout)
for l in results:
    print(l)
"""