# US Protests Analysis

Name: **Quan Phan**

Linkedin: [linkedin.com/in/leopha/](https://www.linkedin.com/in/leopha/)

## Setup

Create pip enviroment

```bash
python3 -m venv .venv
```

Activate enviroment

```bash
source ./.venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.text
```

## Analysis

To check out the protest analysis notebook, click here [analysis.ipynb](analysis.ipynb)

## Extract Protest Message

Before running message extraction, need to ensure that you have **ollama** installed and running

To check if your machine has ollama, type this into terminal

```bash
ollama -h
```

if you have ollama then you would see this output:

```bash
Large language model runner

Usage:
  ollama [flags]
  ollama [command]

Available Commands:
  serve       Start ollama
  create      Create a model from a Modelfile
  show        Show information for a model
  run         Run a model
  pull        Pull a model from a registry
  push        Push a model to a registry
  list        List models
  cp          Copy a model
  rm          Remove a model
  help        Help about any command

Flags:
  -h, --help      help for ollama
  -v, --version   Show version information
```

If you receive an error, visit <https://ollama.com> to downlaod one.

I use `llama2:latest` (7 billion params) to extract protest message from notes.

If you don't already have one, you can install it by running this command:

```bash
ollama pull llama2
```

Once you have `llama2` via `ollama`, you're ready to run [protest_message.py](protest_message.py) by enter this to your terminal:

```bash
python3 protest_message.py
```

Depend on your computer, a dataset of 44k row can take a few hours to finsh extracting. Therefore, it is recommended to run it in a `tmux` or `screen` session (if you're running on a ssh server)
