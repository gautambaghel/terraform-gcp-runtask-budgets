import requests
import json


def attach_comment(comment: str, tfc_api_key: str, run_id: str) -> dict:
    """
    Download Terraform plan from TFC API

    :param comment: The comment to attach to the run
    :param tfc_api_key: TFC API access token
    :param run_id: The run id to attach the comment
    :return: response as dict
    """

    headers = {
        "Authorization": f"Bearer {tfc_api_key}",
        "Content-Type": "application/vnd.api+json",
    }

    data = json.dumps({
        "data": {
        "attributes": {
            "body": f"{comment}"
        },
        "type": "comments"
        }
    })

    url = f"https://app.terraform.io/api/v2/runs/{run_id}/comments"
    response = requests.post(url, headers=headers, data=data)
    if 200 <= response.status_code < 300:
        return response.json()
    else:
        return dict()


if __name__ == "__main__":

    tfc_api_key = ""
    run_id = ""
    comment = ""

    comment_response = attach_comment(comment, tfc_api_key, run_id)
    # Convert the dictionary to JSON and pretty print it
    comment_response_json = json.dumps(comment_response, indent=4)
    # Print the JSON
    print(comment_response_json)
