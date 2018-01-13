def read_data(file_name):
  file_object = open(file_name, "r")
  result = []
  for line in file_object.readlines():
    parts = map(lambda part: float(part.strip()),
                line.split(","))
    if len(parts) != 2:
      raise Exception("illegal line format")
    result.append((parts[0], parts[1]))
  file_object.close()
  return result