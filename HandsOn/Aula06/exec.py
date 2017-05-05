# -*- coding: utf-8 -*-

from jenkins_integration import JenkinsManager
from docker_inergration import DockerManager
import json

jen = JenkinsManager()

with open("job.json","r") as f:
	job_json = f.read()

job_json = json.loads(job_json)

