def alarmHandler(signum,frame):
	raise AlarmException


def input_to(timeout=1):
	signal.signal(signal.SIGALRM,alarmHandler)
	signal.alarm(timeout)
	try:
		text = getch()
		signal.alarm(0)
		return text
	except AlarmException:
		print("\n Prompt timeout. Continuing")
	signal.signal(signal.SIGALRM,signal.SIG_IGN)
	return ''




	                                                                   
