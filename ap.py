import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-ip", "--ip_address", help="IP to convert", required=True)
parsed = ap.parse_args()
print(parsed.ip_address)
