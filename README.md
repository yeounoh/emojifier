# Emojifier
A simple wrapper class around [deepmoji](https://deepmoji.mit.edu/) model ([Huggingface example](https://github.com/huggingface/torchMoji)) -- the work was also published as a [paper (arXiv)](https://arxiv.org/pdf/1708.00524.pdf).

## Requirements
This assumes that torchMoji is installed following [this](https://github.com/huggingface/torchMoji). The torchMoji installation was tested with an older version of pytorch (1.0.1) -- I wasn't able to run it with 1.6.1 or newer.

# Deployment
```shell script
ml model deploy --config-dir . --description "emojifier"
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
