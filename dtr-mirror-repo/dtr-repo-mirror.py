from configparser import ConfigParser
import ast
import requests

def setupMirror(repo, config):
    mirror_endpoint = config.get('SOURCE_DTR', 'url') \
                      + "/api/v0/repositories/" \
                      + repo["source"] \
                      + "/pollMirroringPolicies?initialEvaluation=true"
    auth_conf = (config.get('SOURCE_DTR', 'username'), config.get('SOURCE_DTR', 'token'))

    httpPostData = dict(
        username=config.get('TARGET_DTR', 'username'),
        authToken=config.get('TARGET_DTR', 'token'),
        enabled=True,
        remoteHost=config.get('TARGET_DTR', 'url'),
        remoteRepository=repo["target"],
        skipTLSVerification=True)

    ## Posting HTTP Request
    print("Setting up mirror for the repo.." + repo["source"])
    try:
      response = requests.post(mirror_endpoint, auth=auth_conf, json=httpPostData, verify=False)
      if response.status_code == 201:
        print("Mirror configured successfully")
    except requests.ConnectionError:
      print("Failed to connect")

if __name__ == "__main__":
    config = ConfigParser()
    config.read('mirror.cfg')
    repos = ast.literal_eval(config.get('MIRROR', 'repos'))
    for repo in repos:
      setupMirror(repo, config)
