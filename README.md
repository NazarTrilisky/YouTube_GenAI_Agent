# YouTube_GenAI_Agent
LLM Agent to auto-comment on YouTube videos

## How to Run
1. `pip install -r requirements.txt`
2. Fill in all the placeholders in the `conf` folder
   - YouTube details: video ID, etc.
   - OpenAI details: e.g. access key
3. `python main.py`

The code should pull comments from your video, prompt the LLM, get a completion, and write the completion as a response to the YouTube comments.

## Helpful links
These have instructions for generating OpenAI and YouTube access keys
* https://developers.google.com/youtube/v3/docs/comments
* https://platform.openai.com/docs/api-reference/introduction

