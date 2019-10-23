# Software-Testing-PPA2

Use python3 ppa1.py to run the command-line program and python3 ppa2webservice.py to run the web service. We couldn't get one program to do both things at once.

The database code seen in ppa1.py works fine for a non-Docker MySQL implementation. For reasons unknown, connection to MySQL inside a Docker container is "refused," and a solid day of troubleshooting did nothing to help. We couldn't get tests working, either.

As for the web aspect, it works just fine (besides accessing the database, of course), but tests don't. We tried mocking the request objects used, but the mocks didn't fool the code. It raises an exception because it's not a real request context. And yes, we used the tutorial linked in the assignment description. We also tried any other tutorials we could find, and they didn't work, either.

We got the CI server working, though. The command we used was docker run --rm -u root -p 8080:8080 -p 50000:50000 -v jenkins-data:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock -v "$HOME":/home jenkinsci/blueocean and it worked perfectly.

As for the database, we tried docker run --name PPA2DB -e MYSQL_ROOT_PASSWORD=root -d mysql:latest. The DB name was also PPA2DB.

So far, this project has taken Murphy's Law to new and exciting extremes, and after beating our heads against obtuse and theoretically-impossible errors for literal days on end, we're calling what we have good enough.
