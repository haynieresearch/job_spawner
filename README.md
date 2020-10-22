# Job Spawner
Just a simple program to execute jobs/commands and retry if result code is greater than 0.

## USAGE
job.py command.sh\
job.py command.sh 3

If you specify a number after the command, that is how many retries will be attempted if the result code is greater than 0.

## GOAL
Simplify the execution process of scheduled jobs that sometimes fail for reasons that can be resolved by simply resubmitting the job. Generally, this is used to submit SAS jobs that sometimes fail due to API call failures that are resolved by a second attempt.

## LICENSE
Copyright (c) 2020 Haynie IPHC, LLC\
Developed by Haynie Research & Development, LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
