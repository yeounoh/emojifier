# Emojifier
Emojifier based on [Huggingface deepmoji model](https://github.com/huggingface/torchMoji). This project works strictly with an older version of pytorch (1.0.1) -- I wasn't able to run it with 1.6.1 or newer. If you have any question or suggestions, please let me know, `@yeounoh.chung`

# Deployment
```shell script
ml model deploy --config-dir=./ --description="emojifier"
```

# Online serving
```shell script
ml model predict --name "emojifier" --json-file sample.json
```

The `sample.json` contains sample input parameters,
```json
{
  "featuresMap": {
    "text": "Hello World!",
    "top_n": "5",
    "emojize": "True",
  }
}
```
where `text` key holds the actual text to generate emojis.
