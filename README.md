# CS 4300 Final Project - TruthTellers

## Contents

- [Summary](#summary)
- [Purpose](#purpose )
- [Input](#Input)
- [Output](#Output)
- [Files](#Files)
- [Debugging Some Basic Errors](#debugging-some-basic-errors)
- [General comments from the author](#general-comments-from-the-author)

## Summary

This is the GitHub repository for **"CS/INFO 4300 final project at Cornell University"** authored by
Michelle Prior, Donna Illukyh, Melissa Psaras, Sheba Sow, and Chike Egbuchulum.

This project takes in a user-determined input and returns an output of three articles from known news sources
where the articles are determined by the user's input.  For more information
on acceptable inputs and expected outputs, go to the respective section below.


## Purpose

The purpose of this project is to give a variety of articles relevant to user input
for the user to choose from while also giving them information about bias for the news 
outlet each article is coming from.  In this way, the user can make their own informed 
judgement about which article to choose and read from the information we give them.


## Input

The user can type into the text box anything they want including but not limited to, a general query,
a couple words, quotes from an articles, an entire article, etc.  However, note that the idea of 
the user input is to input things they want to see within the content of the articles returned.
For example, inputted the name of an NYT columnist would not necessarily return articles related
to the columnist.  On the other hand, inputting "war on Ukraine" would work and give back 
articles relevant to the topic.  The reason for this ties back to the purpose of our 
project which is to display relevant articles across a variety of news sources with a
variety of biases.  Returning all articles from one source because a specific author 
works at that news outlet would defeat the purpose.


## Output

Once the user has inputted something, they press the "Tell Me The Truth!" button
which results in three news article titles being displayed with their respective news outlet 
and bias rating.

## Files

- Firstly, only use MySQL. No Postgres, no MongoDB and no SQLite
  - If you decide to use these, the server can still build them and deploy them with no problem, but you will be responsible for making it work
- A helper class called **MySQLDatabaseHandler.py** has been provided.
  - This class abstracts the process of creating and managing the database, the engine and the connections.
  - It also abstracts the process of querying the database.
  - The query_executor method will handle any non-select queries, like INSERT, UPDATE, DELETE etc. This is useful for modifying the DB as required
  - The query_selector method will return any SELECT queries made on the DB.
  - Preferably, you will not use any of the above two methods and will instead just implement your own in a more efficient way, but these functions have been provided just as an example, or as support for those who may not be comfortable with SQLAlchemy. If you are comfortable with SQLAlchemy, feel free to write the methods using the ORM framework and supported methods.
  - **NOTE: Do not modify the other methods besides the two mentioned. You can add new ones, and override the above two methods, but do not delete or modify the connection class**
- A few things to keep in mind:
  - If your database does not exist, it should automatically be created by the script (if it doesn't, post it up on ED)
  - Your authentication details for the DB are fixed along with the initial DB. 
   - Do not change these params unless you're aware of how the docker-compose file works.
- The **init.sql** file is special, in that as the name suggests, it's your de-facto DB. It will always be built before your service is ready to run, and is helpful in storing pre-existing data, like test users, some configs and anything else that you may want at run-time.
  - It has the ability to detect its environment, and will adapt based on whether you have deployed it on the server or not
  - When running locally, it will be loaded to your local database without any import commands required, and will be re-built each time
  - When deployed on the server however, it will only be run once at the start of deployment. Any changes made to the DB from here on will be permanent, unless destroyed.

## Debugging Some Basic Errors
- After the build, wait a few seconds as the server will still be loading, especially for larger applications with a lot of setup
- **Do not change the Dockerfiles without permission**
- Sometimes, if a deployment doesn't work, you can try logging out and back in to see if it works
- Alternatively, checking the console will tell you what error it is. If it's a 401, then logging in and out should fix it. 
- If it isn't a 401, first try checking the logs or container status. Check if the containers are alive or not, which could cause issues. If the containers are down, try stopping and starting them. If that does not work, you can report it on ED.
- If data isn't important, destroying and then cloning and re-building containers will usually fix the issue (assuming there's no logical error)

## General comments from the author
### Mayank/ms3293

- Since this project was made in the span of a few weeks, it is very likely things will break from time to time. If things break, you can send an email through the course email or post to ED first.
- If you would like to see stuff added to the dashboard you can send an email through the course email and prefix the title with FEATURE REQUEST
- If you REALLY want to go above and beyond, you can make a request for a special Docker template. These will likely be turned down unless there is an exceptional reason to do so, and you will have to be able to debug it yourself to ensure it works.
- You can ask for the allocation of extra port numbers which will be approved or denied on a case-by-case basis.
- You can also email regarding any questions relating to the service itself. If you think things can be improved or some better logic can be implemented for certain portions, or even just want to know more about the project then feel free to do so.

