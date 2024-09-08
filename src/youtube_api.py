
import os
import json
import googleapiclient.discovery
import google_auth_oauthlib.flow
import googleapiclient.errors


with open('../conf/youtube.json', 'r') as fh:
    cnfg = json.load(fh)


youtube_read_obj = googleapiclient.discovery.build(
    cnfg['API_SERVICE_NAME'],
    cnfg['API_VERSION'],
    developerKey=cnfg['DEVELOPER_KEY']
)

youtube_write_obj = youtube_read_obj


def refresh_credentials_obj():
    global youtube_write_obj

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        cnfg['CLIENT_SECRETS_FILE'],
        cnfg['OAUTH_SCOPES']
    )
    credentials = flow.run_console()
    youtube_write_obj = googleapiclient.discovery.build(
        cnfg['API_SERVICE_NAME'],
        cnfg['API_VERSION'],
        credentials=credentials
    )


def get_comments_for_video(video_id):
    cmd = youtube_read_obj.commentThreads().list(
        part='snippet,replies',
        videoId=video_id
    )
    response = cmd.execute()
    return response['items']


def write_comment_to_video(video_id, comment_txt):
    refresh_credentials_obj()
    request = youtube_write_obj.commentThreads().insert(
        part="snippet",
        body={
          "snippet": {
            "videoId": video_id,
            "topLevelComment": {
              "snippet": {
                "textOriginal": comment_txt
              }
            }
          }
        }
    )
    try:
        response = request.execute()
    except googleapiclient.errors.HttpError as http_err:
        print("Error posting comment.  HTTP status code: {}".format(
              http_err.resp.status))
        print(http_err)
        raise http_err

    print("Successfully wrote comment")

