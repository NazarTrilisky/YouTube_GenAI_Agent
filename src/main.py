
from chatgpt_api import get_chat_gpt_completion
from youtube_api import get_comments_for_video, write_comment_to_video


LAST_N_COMMENTS = 10
VIDEO_ID = "abc123updateMe"


if __name__ == '__main__':
    comments = get_comments_for_video(video_id=VIDEO_ID)
    prompt = ""
    for item in comments[-LAST_N_COMMENTS:]:
        #item['snippet']['topLevelComment']['snippet']['publishedAt']
        #item['snippet']['topLevelComment']['snippet']['updatedAt']
        prompt += "\n{} said:\n".format(
            item['snippet']['topLevelComment']['snippet']['authorDisplayName'])
        prompt += '"""\n{}\n"""\n'.format(
            item['snippet']['topLevelComment']['snippet']['textOriginal'])

    prompt += "Respond to the above YouTube video comments\n"
    prompt += "The last comment is the most recent\n"
    prompt += "The name of user follows '@', e.g. '@<user-name>'"

    completion = get_chat_gpt_completion(prompt)
    write_comment_to_video(VIDEO_ID, completion)
    print("Successfully wrote comment '{}' to video".format(completion))

