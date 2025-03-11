import time

start_time = time.time()

timeout = 5
while time.time() - start_time <= timeout:
  time.sleep(1)
  print(f"Elapsed time: {time.time() - start_time}")

print("\nExited the loop.")
print(f"Total elapsed time: {time.time() - start_time}")


