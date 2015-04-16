## PyCon 2015 résumé of interesting content

The big news in Python development is the introduction of a non-binding system of types in function declarations:

 * [Guido van Rossum — Type Hints](https://www.youtube.com/watch?v=2wDvzy6Hgxg)

[PEP-483](https://www.python.org/dev/peps/pep-0483/) and [PEP-484](https://www.python.org/dev/peps/pep-0484/) discuss the ideas behind this development, and there is some conversation on Reddit [here](http://www.reddit.com/r/Python/comments/2pveeq/guido_van_rossum_the_theory_of_type_hinting_for/). Type hinting has definite application to testing, and there was a keynote on this subject by Gary Bernhardt, but to my chagrin it doesn't seem to have been recorded.

---

I attended the two tutorials on Scikit-Learn, the one on Pyspark, and the one on the mobile framework Kivy. I had a great deal of trouble with packages and environments. 

 * The Scikit-Learn tutorials recommended the use of Anaconda; I experienced a persistent error, until I eventually installed all the dependencies manually or through `pip`. That ate up quite a bit of the first tutorial, and I wish the installation instructions had included steps for ensuring that everything was working correctly.
 
I prepared my own Vagrantfiles for use with Pyspark and Kivy, and shared them with the instructors.

 * The Pyspark Vagrantfile turned out to work perfectly, and it was a real education to construct. My sense is that Pyspark may be useful if one absolutely has to use Spark within Python, but for many purposes where parallelism is not required, Scikit-Learn or Pandas would be better tools. Pyspark is kind of clunky.
 * The Kivy Vagrantfile worked correctly until I realized that it would not be easy to display the graphical output, since X11-forwarding is hard to get working with VirtualBox and X11/Quartz on OS X. Kivy, in addition, seems to require so many dependencies, and their relationships are so brittle, that I think it would be hard to develop for it regularly. Though, of course, if one uses it regularly, configuring the environment probably becomes second-nature.

---

Most of the talks are now on line; a few very good ones were not recorded, though. Various topics that may be of interest to MediaMath's M/I and QA groups are listed here (I haven't included everything I liked, though). It was striking to me how many talks there were on data science this year.

I took detailed notes only on the four tutorials, but I think the content in the public slide-sets would be sufficient for anyone wanting exposure to this content. 

### Testing

 * [Dan Crosta — Good Test, Bad Test](https://www.youtube.com/watch?v=RfR_QRoNZxo)
 * [Itamar Turner Trauring — A Beginner's Guide to Test driven Development](https://www.youtube.com/watch?v=dM7N6PFP3uo)
 * [Ian Cordasco — Cutting Off the Internet: Testing Applications that Use Requests](https://www.youtube.com/watch?v=YHbKxFcDltM)
 * [Katie Cunningham — Usability Testing on the Cheap](https://www.youtube.com/watch?v=zZx2l3BTCrg)
 
### Data Science

 * [Jake VanderPlas — Machine Learning with Scikit-Learn (I)](https://www.youtube.com/watch?v=L7R4HUQ-eQ0) (tutorial)
 * [Olivier Grisel — Machine Learning with Scikit-Learn (II)](https://www.youtube.com/watch?v=oGqGxvqA9-k) (tutorial)
 * [Orlando Karam — Introduction to Spark with python](https://www.youtube.com/watch?v=9xYfNznjClE) (tutorial)
 * [Soups Ranjan — Data Science in Advertising: Or a future when we love ads](https://www.youtube.com/watch?v=HZTgLuOpFU8)
 * [Brandon Rhodes — Pandas From The Ground Up](https://www.youtube.com/watch?v=5JnMutdy6Fw) (tutorial)
 * [Kyle Kastner — Machine Learning 101](https://www.youtube.com/watch?v=r-1XJBHot58)
 * [Allen Downey — Bayesian statistics made simple](https://www.youtube.com/watch?v=5W715nfJNJw) (tutorial)
 * [Allen Downey — Statistical inference with computational methods](https://www.youtube.com/watch?v=5Vjrqnk7Igs) (tutorial)

### Reproducible environments

 * [Luke Sneeringer — Ansible 101](https://www.youtube.com/watch?v=-i1pZ6vvMX8) (tutorial)
 * [Andrew T. Baker — Demystifying Docker](https://www.youtube.com/watch?v=GVVtR_hrdKI)
 * [Renee Chu, Matt Makai — Don't Make Us Say We Told You So: virtualenv for New Pythonistas](https://www.youtube.com/watch?v=Xdv7vwIIThY)
 
### Python education and best practices

 * [Amy Hanlon — Investigating Python Wats](https://www.youtube.com/watch?v=sH4XF6pKKmk)
 * [Stuart Williams - Python Epiphanies](https://www.youtube.com/watch?v=Ug0iDjbMPVg)
 * [Stuart Williams — Python by Immersion](https://www.youtube.com/watch?v=RVNIdoepdzU) (tutorial)
 * [Raymond Hettinger — Beyond PEP 8: Best practices for beautiful intelligible code](https://www.youtube.com/watch?v=wf-BqAjZb8M)
 * [Ned Batchelder — Facts and Myths about Python names and values](https://www.youtube.com/watch?v=_AEJHKGk9ns)

### Self-development for coders

 * [Sasha Laundy — Your Brain's API: Giving and Getting Technical Help](https://www.youtube.com/watch?v=hY14Er6JX2s)
 * [Alex Gaynor — Techniques for Debugging Hard Problems](https://www.youtube.com/watch?v=ij99SGGEX34)

### Python internals

 * [Allison Kaptur - Bytes in the Machine: Inside the CPython interpreter](https://www.youtube.com/watch?v=HVUTjQzESeo)
 * [Carol Willing - Finding Your Groove: Contributing to CPython and Beyond](https://www.youtube.com/watch?v=szeo1XgmuEk)
 * [Philip James, Asheesh Laroia — Type python, press enter. What happens?](https://www.youtube.com/watch?v=XVhSjZYwZJo)

## Inspiring Pythonist speakers
 
 * [Brandon Rhodes — Oh, Come On Who Needs Bytearrays](https://www.youtube.com/watch?v=z9Hmys8ojno)
 * [David Beazley — Modules and Packages: Live and Let Die!](https://www.youtube.com/watch?v=0oTh1CXRaQ0)
 * [David Beazley — Python Concurrency From the Ground Up: LIVE!](https://www.youtube.com/watch?v=MCs5OvhV9S4)
 * [Raymond Hettinger — Super considered super!](https://www.youtube.com/watch?v=EiOglTERPEo)

### Other miscellaneous topics of interest

 * [Andrew Montalenti — streamparse: real-time streams with Python and Apache Storm](https://www.youtube.com/watch?v=ja4Qj9-l6WQ)
 * [Brett Cannon — How to make your code Python 2/3 compatible](https://www.youtube.com/watch?v=KPzDX5TX5HE)
 * [Clayton Parker — So you think you can PDB?](https://www.youtube.com/watch?v=P0pIW5tJrRM)
 * [Jim Baker — A Winning Strategy with The Weakest Link: how to use weak references to make your code more robust](https://www.youtube.com/watch?v=NknSssmLk4w)
 * [Laura Rupprecht — Describing Descriptors](https://www.youtube.com/watch?v=h2-WPwGnHqE)
 * [Dan Tracy — Ship it: Deployments with Pip](https://www.youtube.com/watch?v=aD2CfKQB5xM) 
 * [Mike Müller — Descriptors and Metaclasses — Understanding and Using Python's More Advanced Features](https://www.youtube.com/watch?v=v2WTVCyTYMw)
 * [David Baumgold — Advanced Git](https://www.youtube.com/watch?v=4EOZvow1mk4)
 * [Jake VanderPlas — Losing your Loops: Fast Numerical Computing with NumPy ](https://www.youtube.com/watch?v=EEUXKG97YRw)
 * [Michael Scherer — Ansible beyond YAML](https://www.youtube.com/watch?v=igJTEugHozM)
 * [Richard Jones — Introduction to game programming with Kivy](https://www.youtube.com/watch?v=U14P8gtjQmU)

[end]