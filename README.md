# Embeddings w Instructor


This is a simple reference repo that makes use of the Instructor-series models introduced in the [One Embedder, Any Task: Instruction-Finetuned Text Embeddings](https://arxiv.org/abs/2212.09741) work. Similar to how one might take a swing; at prompt engineering in a "playgrounds" like UI to test LLM prompting, a jupyter notebook to test some simple hypothesis or misc script for feature testing in a codebase -- this repo serves as a quick way to get set up and testing semantic similarity workflows.

The model leveraged here is a good first pass at any semantic similarity task, given that you can "prompt" it for the kind of comparisons you are hoping to do -- minimal examples are provided in `demo.py`. 

You can build up a suitable env for testing with `pip install -r requirements.txt` or `conda env create -f env.yaml` depending on your package manager of choice.

