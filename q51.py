def Err():
	return 5/0

try:
	Err()
except ZeroDivisionError:
	print("Division by Zero")
#except Exception, err:
	print("Caught an Exception")
finally:
	print("In finally block for cleanup")