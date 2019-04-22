"""ping sweep

usage: ping_sweep.py [-h] -n <netcidr>

options:
    -h, --help      show this help message and exit
    -n <netcidr>    ping_sweep target range (require) 

"""

from docopt import docopt
from netaddr import IPNetwork
import pings

if __name__ == '__main__':

    args = docopt(__doc__)

    for ip in IPNetwork(args["-n"]).iter_hosts():
        p = pings.Ping()
        res = p.ping(str(ip))

        if res.is_reached():
            print '%s' % ip

