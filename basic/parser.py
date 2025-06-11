import argparse

# parser = argparse.ArgumentParser(description="Process some integers.")
# parser.add_argument(
#   "--integers","-i",
#   metavar="N",
#   type=int,
#   nargs="+",
#   help="an integer for the accumulator (default: find the max)",
# )
# parser.add_argument(
#   "--sum",
#   dest="accumulate",
#   action="store_const",
#   const=sum,
#   default=max,
#   help="sum the integers",
# )
# def parse_args():
#   """
#   Parse command line arguments.

#   Returns:
#       argparse.Namespace: Parsed arguments.
#   """
#   return parser.parse_args()

# args = parse_args()

name_parser = argparse.ArgumentParser(description="Process a name of a person.")
name_parser.add_argument(
  "--name","-n",
  type=str,
  metavar="NAME",
  required=True,
  help="the name of the person"
)
name_parser.add_argument(
  "--lang","-l",
  type=str,
  metavar="LANGUAGE",
  choices=["en", "fr", "es"],
  default="en",
  help="the language of the greeting (default: en)"
)
name_parsed = name_parser.parse_args()
def parse_name_args():
  greetings = {
      "en": "Hello",
      "fr": "Bonjour",
      "es": "Hola"
  }
  """
  Parse command line arguments for name processing.

  Returns:
      argparse.Namespace: Parsed arguments.
  """
  return f"{greetings[name_parsed.lang]}, {name_parsed.name}!"
name_args = parse_name_args()
if __name__ == "__main__":
  # print(args.accumulate(args.integers))
  print(name_args)
  # Example usage: python parser.py --integers 1 2 3 --sum
  # Output: 6
  # Example usage: python parser.py --integers 1 2 3
  # Output: 3
