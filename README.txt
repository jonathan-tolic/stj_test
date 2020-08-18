Hi, as agreed here is my solution for the test task, and the accompanying explanation.

This implementation is focused on an event pattern to regulate communication between various parts. It includes a number of decisions which are my personal preference (since you mention you wanted to understand how I approach problems I thought it would be appropriate), which I will list below:

*There are a number of good event libraries for python however I though that is the most interesting aspect to focus on given your description of the challenges ahead

*Due to the lack of requirements I opted to make the Event pattern as flexible as possible, thus event_data has no universal fixed type. The correctness is enforced through event class types and sanity checks by the manager. This makes it imo easier to extend for a variety of possible future requirements.

*I tried to at least partially demonstrate this by having the webserver show system messages that it acquires through the same event system making it a subscriber as well

*Regarding error handling, while maybe old fashioned I prefer leaving it in the hands of developers, thus my focus on return statements and error querying over exception handling. This is very much my personal preference and I would have no issue if you do not share it.

*I chose IRC over Slack as one of the subscribers as it requires no invites, passwords, signons etc. Think It’ be easier to test.

*another point we might disagree is my preference for strings over constants

Regarding future updates:

*The app atm is monolithic and single threaded (mostly). This is not an issue with the log subscriber but IRC can be a bit of a bottleneck. Ideally I would at least break it into multiple threads and add synchronization to the Event Manager

*I am not a fan of the default way flask handles routes, I would prefer using something like flask-classy and exposing methods as routes. However in this limited example it didnt seem needed

*Naturally a proper frontend

*There are a few notes and todos in the code files explaining some minor choices.


This is a brief summary and I’d be more than happy to discuss this in more detail on our next call.

Looking forward to it.

Regards, STJ 

P.S. I've included a rough docker file however python3 and flask are the only requirements, so building a docker might be a bit of an overkill

