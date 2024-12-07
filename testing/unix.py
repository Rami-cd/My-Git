
import sys
import argparse


argparser = argparse.ArgumentParser(description="this is pain")

argsubparsers = argparser.add_subparsers(title='Commands', dest="var1")
argsubparsers.required = True

argsp = argsubparsers.add_parser("ping", help="ping")
argsp.add_argument("--args",
                   nargs="?",
                   help="ping the arguments")





def main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)
    match args.var1:
        case "ping" : cmd_add(args)
        case "-"    : print("invalide command")
        

def cmd_add(args):
    print("add function.\n")
