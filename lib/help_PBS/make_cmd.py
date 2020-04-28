#!/usr/bin/env python3

import os
import re

CMD = "{}\n"
CD_CMD = "cd {}\n"
INITIAL_LINE = "#!/usr/bin/env sh\n\n"
REP_KWORDS = "^#*replace command#*"
RE_INS_FOR_CMD = re.compile(REP_KWORDS)


class AdminCmd(object):
    def __init__(self, cmd_line):
        cmd = cmd_line.strip()
        self.cmd = cmd
        self.dirs_list = []

    def add_working_dirs(*dirs):
        for dnm in dirs:
            if not os.path.isdir(dnm):
                raise OSError("")
            dirs_list.append(
                         os.path.abspath(dnm)
                            )

    def add_cmds(self, add_fpath):
        cmd_line = CMD.format(self.cmd)
        with open(add_fpath, "a") as add:
            for abs_dnm in self.dirs_list:
                cd_line = CD_CMD.format(abs_dnm)
                add.write(cd_line)
                add.write(cmd_line)

    def write_cmds(self, write_fnm):
        cmd_line = CMD.format(self.cmd)
        with open(add_fpath, "w") as write:
            write.write(INITIAL_LINE)
            for abs_dnm in self.dirs_list:
                cd_line = CD_CMD.format(abs_dnm)
                write.write(cd_line)
                write.write(cmd_line)

    def replace_cmd_from_file(fnm, new_file=None):
        with open(fnm) as read:
            tot_str = read.read()
        tot_txts = []
        cmd_line = CMD.format(self.cmd)
        tot_txts.append(cmd_line)
        for abs_dnm in self.dirs_list:
            cd_line = CD_CMD.format(abs_dnm)
            tot_txts.append(cd_line)
            tot_txts.append(cmd_line)
