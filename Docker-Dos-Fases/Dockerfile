# Construir .war
FROM maven:3.9.9-eclipse-temurin-17 AS build
WORKDIR /app 
COPY my-webapp/ .
RUN mvn clean package

# Construir imagen con Tomcat
FROM tomcat:11.0.2-jdk17-temurin
COPY --from=build /app/target/my-webapp.war /usr/local/tomcat/webapps/