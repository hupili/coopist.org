coopist.org
===========

**Archive** of <http://coopist.org>

The product of [SWHK2013](http://hongkong.startupweekend.org/)

SWHK was my first hackathon. 
I was the sole developer in the team of five. 
The majority of the time was spent on discussing the rough idea of "coopist". 
The effective coding time is about 2~4 hours.

Since we intended to make coopist a movement (which lost moment later), 
the basic idea is to be able to aggregate people's suffering from different social platforms. 
A hashtag is much easier than registering on a new site.

Stack
-----

   * Collect related status by using [twitter search](https://github.com/hupili/snsapi/commit/27d57906c8e6fbbe6d49601eb66d985bc2973775) channel of SNSAPI,
   which is also added during SWHK.
   * Store statuses in MongoDB.
   * Use `jinja2` to render each project page.
   
The user-facing part is purely static.
See `gh-pages` branch for the generated pages.

No web framework is used -- It's a "hackathon" anyway..

Run `auto.sh` as cron job.

Caveats
-------

   * The source repo is not maintained.
   This is just an archive for those who are interested in the codes behind.
   * `master` and `gh-pages` contain different stuffs.
   * In case coopist.org expires,
   checkout the alternative GH-Pages link:
   <http://project.hupili.net/coopist.org/>
   * Python dependencies are not checked. Just run the code and `pip install` anything that is missing.
   We should only rely on a few things `snsapi`, `pymongo`, `jinja2`, etc.

License
-------

MIT for codes in this repo.

External resources retain their own license.
