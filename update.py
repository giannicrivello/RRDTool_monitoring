import rrdtool
import subprocess

class RRDTool:
    
    def create_database(self):
        rrdtool.create('interface.rrd',
                'DS:packets:COUNTER:600:U:U',
                'RRA:AVERAGE:0.5:1:288',
                'RRA:AVERAGE:0.5:6:336'
                )
    
    def update(self):
        date_time = subprocess.run(['date', '+"%s"'], capture_output=True)
        stdout = date_time.stdout
        decoded_stdout = stdout.decode("ascii").strip()
        N = int(decoded_stdout.split('"')[1])

        for i in range(20):
            rrdtool.update('interface.rrd',
                    '%d:%d' % (N + (1+i)*300, 
                    i*10+200))


def main():
    rrdtool = RRDTool()
    rrdtool.create_database()
    rrdtool.update()

if __name__ == "__main__":
    main()


