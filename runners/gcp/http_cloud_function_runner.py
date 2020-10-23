import yaml

config = yaml.load('conf.yaml', yaml.SafeLoader())

def run(request):
    args = request.args
    payload = request.content

