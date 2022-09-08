#create a new workspace and create a new app
# add two permissions : chat:write, files:write
# go to integrations tab of channel(slack-message-automation) >>> add app(analytics app)


from slack_sdk import WebClient
from pathlib import Path
from slack_sdk.errors import SlackApiError


client = WebClient(token="")

try:
    filepath = "./dataframe.png"
    response = client.files_upload(channels='slack-message-automation', file=filepath)
    assert response["file"]  # the uploaded file
except SlackApiError as e:
    assert e.response["ok"] is False
    assert e.response["error"]
    print(f"Got an error: {e.response['error']}")
