def multiple_items(*args):
  print(args)
  print(type(args))

multiple_items("dave", "rafi", "abir")

def multi_name_items(**kwargs):
  print(kwargs)
  print(type(kwargs))

multi_name_items(first="dave", second= "rafi", third = "abir")