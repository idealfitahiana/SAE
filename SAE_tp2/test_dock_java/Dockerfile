FROM eclipse-temurin:21-jdk AS build
WORKDIR /app
COPY Hello.java .
RUN javac Hello.java
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY --from=build /app/Hello.class .
CMD ["java", "Hello"]
