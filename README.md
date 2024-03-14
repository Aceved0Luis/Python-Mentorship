# Python Mentorship

### First steps:

To run each set of scripts individually, first add the environment **`PYTHONPATH`** with the following command: <br>

```bash
> export PYTHONPATH="$PWD/"
```

As an alternative you can use an **`.env`** file. Generate it with the following command: <br>

```bash
>  echo "PYTHONPATH=$PWD/" >> .env 
```

And then export all the environments inside of it each time that you will need it with the command:

```bash
> export $(cat .env | xargs)
```

And then you will be able to run the scripts without any problem.