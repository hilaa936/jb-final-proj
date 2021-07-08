In order to run this project in docker, preform the following commands:

####################################
            For Saar
####################################
cd jb-final-proj
docker build . -t forecast:ver1 -f ./Dockerfile_forecast
docker run -p 8082:5001 -v /Users/saarcohen/JBDataScience/FinalProject/jb-final/jb-final-proj/shared_vol:/app/shared_vol -it forecast:ver1

####################################
            For Hila
####################################
docker build . -t forecast:ver1 -f ./Dockerfile_forecast
docker run -p 8082:5001 -v \\"Put Your FULL Path to the 'shared_vol' folder"\\:/app/shared_vol -it forecast:ver1



Run the last line inside a cronjob (LINUX) / task scheduler (WINDOWS) in order to recreate the model repeatedly.
