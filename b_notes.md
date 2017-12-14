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


### copyspecial/copyspecial.py ...

- Purpose seems to be to learn how to write a module that:
    - captures passed-in arguments
    - validates required arguments
    - shows the user a usage statement if validation fails
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
