In order to run this project in docker, preform the following commands:

####################################
            For Saar
####################################
cd jb-final-proj
docker build . -t ml_model:ver1 -f ./Dockerfile_model
docker run -v /Users/saarcohen/JBDataScience/FinalProject/jb-final/jb-final-proj/shared_vol:/app/shared_vol -it ml_model:ver1

####################################
            For Hila
####################################
docker build . -t ml_model:ver1 -f ./Dockerfile_model
docker run -v \\"Put Your FULL Path to the 'shared_vol' folder"\\:/app/shared_vol -it ml_model:ver1


Run the last line inside a cronjob (LINUX) / task scheduler (WINDOWS) in order to recreate the model repeatedly.
