#!/usr/bin/env python

import argparse

#______________________________________
def cli_options():
  parser = argparse.ArgumentParser(description='Build the DNS record associated to an IP address')
  parser.add_argument('-i', '--ip', dest='ip', help='The IP address')
  parser.add_argument('-p', '--prefix', dest='prefix', help='DNS record prefix')
  parser.add_argument('-s', '--suffix', dest='suffix', help='DNS record suffix')
  parser.add_argument('-d', '--dot-replacement', dest='dot_replacement', help='Dot replacement in DNS record')
  return parser.parse_args()


#______________________________________
def build_dns_record():

  options = cli_options()

  dns_record = options.prefix + options.ip.replace(".",options.dot_replacement) + options.suffix
  print(dns_record)

#______________________________________
if __name__ == '__main__':
  build_dns_record()
