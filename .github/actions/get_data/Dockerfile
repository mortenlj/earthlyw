# action will be run in python3 container
FROM python:3@sha256:589ed6659c0e4aac182f309131cd35e85452d21072570b1f6abc45b7687093a3
# copying requirements.txt and install the action dependencies
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
# script.py is the file that will contain the codes that we want to run for this action.
COPY script.py /script.py
# we will just run our script.py as our docker entrypoint by python script.py
CMD ["python", "/script.py"]
