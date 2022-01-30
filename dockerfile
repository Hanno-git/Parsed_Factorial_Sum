#FROM directive specifies a base image upon which to build.
FROM python:3.9
# the add directive copies the files from a source destination inside the container at build time.
ADD Parsed_Factorial_Sum.py .
# the run directive runs a command at build time.
RUN pip install numpy
# the CMD directive runs a command at run time
CMD [ "python", "./Parsed_Factorial_Sum.py" ]