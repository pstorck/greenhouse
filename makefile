stop:
	pkill -f "python3"

start:
	python3 data_gather.py &
	python3 app.py > log.txt 2>&1 &
