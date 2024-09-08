
import requests
import json
import os


with open('../conf/chat_gpt.json', 'r') as fh:
    cnfg = json.load(fh)

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {}".format(cnfg['CHAT_GPT_KEY'])
}


def get_chat_gpt_completion(prompt):
    json_data = {
        "model": cnfg['MODEL'],
        "messages": [
            {
                "role": "system",
                "content": cnfg['SYSTEM_PROMPT']
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(
        cnfg['CHAT_GPT_URL'],
        headers=headers,
        json=json_data
    )

    if response.status_code != 200:
        msg = "Non-200 response code from OpenAI"
        msg += "\nReason: {}".format(response.reason)
        msg += "\nText: {}".format(response.text)
        raise Exception(msg)

    return response.json()['choices'][0]['message']['content']

