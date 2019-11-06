import sys
import math

# update_progress() : Displays or updates a console progress bar
# Accepts a float between 0 and 1. Any int will be converted to a float.
# A value under 0 represents a 'halt'.
# A value at 1 or bigger represents 100%
def update_progress(progress,label=None):
    barLength = 40 # Modify this to change the length of the progress bar
    status = ""
    if label is None:
        label = "Percent"
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
#        status = "\r\nDone...\r\n"
        status = ""
    block = int(round(barLength*progress))
    text = "\r" + label + ": [{0}] {1:.1f}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()

def frac_pi_str(t):
    ret_str = "{0:.2f}".format(t/math.pi)

    # remove trailing zeros
    if ret_str.endswith(".00"):
        ret_str = ret_str.replace(".00","")
    if ret_str.endswith(".0"):
        ret_str = ret_str.replace(".0","")
    if ("." in ret_str) and (ret_str.endswith("0")):
        ret_str = ret_str[:-1]

    if ret_str == "1":
        return "\\pi"
    else:
        return ret_str + "\\pi"
