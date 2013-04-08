def skipLines(current_file,strip_lines):
  for i in range(strip_lines):
    current_file.next()
  return current_file
