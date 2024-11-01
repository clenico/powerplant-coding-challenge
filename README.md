# powerplant-coding-challenge

## build
``` bash
docker build -t powerplant_load_planner -f build/Dockerfile .
```

## run
``` bash
docker run -p 8888:8888 powerplant_load_planner
```

## tests

``` bash
docker run --entrypoint python powerplant_load_planner -m unittest discover tests/unit

docker run --entrypoint python powerplant_load_planner -m unittest discover tests/integration
```
