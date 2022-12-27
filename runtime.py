import time

def starttime():
    starttime = time.time()
    return starttime


def stoptime(starttime):
    stoptime = time.time()
    run= stoptime-starttime
    hour, minute = divmod(run,3600)
    minutes, sec = divmod(minute, 60)
    output = print( 'Runtime: ',int(hour),':',int(minutes),':',int(sec))
    return output

