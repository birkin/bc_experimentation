### resources...

- <https://github.com/mlafeldt/google-python-class>

- <https://developers.google.com/edu/python/exercises/basic>

---


### commands...

- use-local, for access to default anaconda packages

        $ conda create --use-local --name clps1950_bc

- to remove an environment

        $ conda remove --name clps1950_bc --all

- to check environments

        $ conda info --envs

---


### thoughts...

- `import` -- Most of the imports the students will use will either be built-in python packages, or packages installed by conda. But it might be useful for them to be aware that any code they create can become a package simply by adding to the directory an empty __init__.py file.

- logging

        import logging

        logging.basicConfig(
            # filename=LOG_PATH,
            level=logging.DEBUG,
            format='[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s',
            datefmt='%d/%b/%Y %H:%M:%S' )
        log = logging.getLogger(__name__)
        log.debug( 'log configured' )

- testing

---


### wordcount/basic.py ...

- Purpose seems to be to...
    - deal with passed-in arguments
    - learn about dicts
        - sorting by comparators -- even though the single example here doesn't fully invite grokking
    - benefit of having manage-functions call worker-functions.

- basic words and count...

        python ./basic/solution/wordcount.py --count "/Users/birkin/Desktop/clps1950_stuff/CLPS1950_python/basic/alice.txt"

- top count...

        python ./basic/solution/wordcount.py --topcount "/Users/birkin/Desktop/clps1950_stuff/CLPS1950_python/basic/alice.txt"

---


### copyspecial/copyspecial.py ...

- Purpose seems to be to learn how to write a module that:
    - does the above argument stuff
    - passes the arguments to functions that do work
    - and also shows the built-in python 'commands' module -- though it should perhaps be noted there are different ways to do this.

-just prints out found special paths...

        python ./copyspecial/solution/copyspecial_b.py /Users/birkin/Desktop/clps1950_stuff/test_from_dir

- copies 'special' files from 'from-dir' to 'to-dir'...

        python ./copyspecial/solution/copyspecial_b.py --todir /Users/birkin/Desktop/clps1950_stuff/test_to_dir /Users/birkin/Desktop/clps1950_stuff/test_from_dir

- copies the two 'special' file from 'from-dir' into a zip file in 'to-dir'...

        python ./copyspecial/solution/copyspecial_b.py --tozip /Users/birkin/Desktop/clps1950_stuff/test_to_dir/the_zip.zip /Users/birkin/Desktop/clps1950_stuff/test_from_dir

---


### babynames/babynames.py ...

Purpose seems to be:
- to explore using regex (though I'd use beautifulsoup)
- to hack data-sources
- thought: consider introducing testing

---


### logpuzzle/logpuzzle.py ...

- outputs list of jpg urls...

        python ./logpuzzle/solution/logpuzzle_b.py "/Users/birkin/Desktop/clps1950_stuff/CLPS1950_python/logpuzzle/animal_code.google.com"

        python ./logpuzzle/solution/logpuzzle_b.py "/Users/birkin/Desktop/clps1950_stuff/CLPS1950_python/logpuzzle/place_code.google.com"

- _tries_ to download images to specified directory...

        python ./logpuzzle/solution/logpuzzle_b.py --todir "/Users/birkin/Desktop/clps1950_stuff/test_to_dir" "/Users/birkin/Desktop/clps1950_stuff/CLPS1950_python/logpuzzle/animal_code.google.com"

        python ./logpuzzle/solution/logpuzzle_b.py --todir "/Users/birkin/Desktop/clps1950_stuff/test_to_dir" "/Users/birkin/Desktop/clps1950_stuff/CLPS1950_python/logpuzzle/place_code.google.com"

---

---
