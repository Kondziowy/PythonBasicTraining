import os

file_to_remove = os.path.join(os.getcwd(), "non_existent_file") 

print("Do you want to remove %s? Please answer yes or no" % file_to_remove)

answer = input()
answer_is_true = bool(answer)

if answer_is_true:
  print("Removing file %s" % file_to_remove)
  os.unlink(file_to_remove)