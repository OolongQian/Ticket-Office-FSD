from subprocess import Popen, PIPE, STDOUT


class PipeLine(object):

    def __init__(self, exec_path):
        self.proc = Popen([exec_path], stdin=PIPE, stdout=PIPE)

    # encode has two default parameters: UTF-8, and strict
    def write(self, cmd):
        self.proc.stdin.write((cmd + '\n').encode())
        self.proc.stdin.flush()

    # get rid of output newline character
    def readline(self):
        return self.proc.stdout.readline().decode().strip('\n')


def main():
    prog_exec_path = './backend/prog'
    db = PipeLine(prog_exec_path)
    while True:
        cmd = input()

        if cmd == "exit":
            break

        db.write(cmd)
        print(db.readline())
        print(db.readline())


if __name__ == "__main__":
    main()
