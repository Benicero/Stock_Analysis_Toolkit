Alrighty
========
589188152968-8o2d7b3ftpmicmcj21825ld1jp1evfku.apps.googleusercontent.com

Gv_VB5oW3Y21dVSM5UdWxaXT

## basic structure as im thinking so far:
1. scripts to scrape sites
    * read actual data of stocks from somewhere  
        (how often? hourly? daily? and how many/what stocks?)
    * scrape investing sites
2. interpret and store site data
    * store stock data in an efficient format, and make it nicely accessible  
        (we can probably store data on our local machines to save github space)
    * extract investing sites' advice, along with author, date & time
3. analyze data
    * look at basic stock performance data, look for trends and patterns
    * see which investing sites and authors are accurate for which stocks


## other:
* i am thinking it would be good to have basically a "control group" thing that would basically pick random stocks each day, and see how well it does, to get a baseline
* make a list of site that we want to scrape as well as any free APIs.
* play with quantifying data that isn't inherently numberical, such as using a sentiment analysis of the nightly business report as a factor in the overall data set.

Random Spontaneous Questions:
- Can we predict the nations sentiment toward the economy by quantifying daily reports and other possibly arbitray media sources. 
