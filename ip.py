import argparse

ap = argparse.ArgumentParser("IP converting utility")
ap.add_argument("-ip", "--ip_address", help="IP to convert", required=True)
parsed = ap.parse_args()

for octet in parsed.ip_address.split("."):
  print("%.2x" % int(octet),end="")