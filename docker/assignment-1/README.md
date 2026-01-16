# Commands

1. Build the image

    docker build -t node-application .


2. Run the container (locally)

    docker run -it -p 9000:3000 node-application


3. Login

    docker login


4. Tag the image

    docker tag node-application:latest aaronwppe/express-app:latest


4. Push on docker hub

    docker push aaronwppe/express-app:latest