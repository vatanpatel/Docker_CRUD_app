FROM continuumio/anaconda3:4.4.0		# We create a layer of the anaconda docker image
COPY . /app								# We then copy everything that we have in our current directory (which should be ../greendeck_task1) into 
WORKDIR /app							# we set our working directory to /app where this Dockerfile is located whithin the container
RUN pip install -r requirements.txt 	# We then install all the libraries in the requirements.txt file which are necessary for our app to run
EXPOSE 5000								# We expose this to 5000 where our docker image will be hosted on localhost
ENTRYPOINT [ "python" ] 				# We set our entry program as python
CMD [ "app.py" ] 						# And finally in our entrypoint, we run our app