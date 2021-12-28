import rrdtool

def fetch():
    for i in rrdtool.fetch('interface.rrd', 'AVERAGE'):
        print(i)
        

def main():
    fetch()

if __name__ == "__main__":
    main()


    
