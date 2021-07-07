In order to run this project in docker, preform the following commands:

cd jb-final-proj
docker build . -t ml_model:ver1 -f ./Dockerfile_model
docker run -v "/Users/saarcohen/JB - Data Science/FinalProject/jb-final/jb-final-proj":/app/shared_vol -it ml_model:ver1

Run the last line inside a cronjob (LINUX) / task scheduler (WINDOWS) in order to recreate the model repeatedly.
