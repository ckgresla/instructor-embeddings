#!/usr/bin/env python3
# Demo an Embedding Comparison Workflow

import numpy as np
from tqdm import tqdm

from pkg.config import *
from pkg.instructor import *


# Init the model
model_name = "hkunlp/instructor-large"  # see- https://github.com/HKUNLP/instructor-embedding#model-list
model = INSTRUCTOR(model_name)

vec = model.compute_embedding("this is my swag")


# Toy Task
print("lets say we want to compare the following sequence of strings:")
demo_data = [
    "the market is the place for people who love fresh food"
    "coffee is delightful",
    "did you know that penguins swim to MELBOURNE!",
    "I absolutely love seagulls",
    "what kind of cafe is your favorite?",
    "tea is okay, but only if we are talking proper Chai or Green Tea",
    "should we have a Croissant with this beverage?",
    "whom are you?",
    "asdf hjkl",
    "safsdafh sdkljsdkja fkjlsda jsdajiuvhcuqgikcnxz,mvnpeqrgj eqrioxcnvkjxcvhopigjer,vmn,.xzcn",
]

print("[")
for d in demo_data:
    print(f"    {d},")
print("]\n")

target_string = "the cafe is THE place for people who love conversation and drinks"
print(f"to the string: '{target_string}'")


# Do some math
print(
    "We can calculate the similarities between each data string's vector and our target string"
)

demo_embeddings = []
target_embedding = model.compute_embedding(target_string)

for i, s in enumerate(tqdm(demo_data)):
    embedded = model.compute_embedding(s)
    demo_embeddings.append(embedded)

    sim = np.dot(target_embedding[0], embedded[0]) / np.linalg.norm(target_embedding) * np.linalg.norm(embedded)
    print(f"    {sim :2f} similarity for: {demo_data[i]}")


# Pass 2 -- w a better prompt!
print("those scores look rather mid as a semantic similarity between the strings, can we do better?")
print("we might be able to by *prompting* this model!")
new_prompt = "Embed these strings to capture relationships with the following keywords (coffee, cafe, drinking), make anything not related to these keywords very disimilar, this will be used for semantic similarity calculations: "


print(f"lets retry calculating the similarities with the following as our model prompt: {new_prompt}")
demo_embeddings = []
target_embedding = model.compute_embedding(target_string)

for i, s in enumerate(tqdm(demo_data)):
    embedded = model.compute_embedding(s, prompt=new_prompt)
    demo_embeddings.append(embedded)

    sim = np.dot(target_embedding[0], embedded[0]) / np.linalg.norm(target_embedding) * np.linalg.norm(embedded)
    print(f"    {sim :2f} similarity for: {demo_data[i]}")



