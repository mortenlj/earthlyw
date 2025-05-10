# action will be run in python3 container
FROM python:3@sha256:4e4a245c45b5a930dbff2bd7df20ff73cc3bed7fe9bc7a7efb61cb5e711e3da5
# copying requirements.txt and install the action dependencies
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
# script.py is the file that will contain the codes that we want to run for this action.
COPY script.py /script.py
# we will just run our script.py as our docker entrypoint by python script.py
CMD ["python", "/script.py"]
