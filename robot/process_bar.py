import sys, time
def process_bar():
    print("loading......")
    for i in range(11):
        if i != 10:
            sys.stdout.write("==")
        else:
            sys.stdout.write("== " + str(i*10)+"%/100%")
        sys.stdout.flush()
        time.sleep(0.2)
    print("\n"+"loading......ok")
