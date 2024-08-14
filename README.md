# Hello there👋

```java
// About me

import java.util.List;
import java.util.Map;

public class BackendDeveloper {
    private String name;
    private String city;

    private String role;

    private List<Map<String, String>> spoken_languages;

    private Map<String, List<String>> stack;


    public BackendDeveloper() {
        this.name = "Mikhail Trifonov";
        this.city = "Innopolis";

        this.role = "Java Backend Developer";

        this.spoken_languages = List.of(
                Map.of(
                        "language", "Russian",
                        "level", "Native"
                ),
                Map.of(
                        "language", "English",
                        "level", "Upper-Intermediate"
                )
        );

        this.stack = Map.of(
            "core", List.of(
                    "OOP", "Collections", "Stream API", "Generics", "Algorithms",
                        "Maven", "Gradle"
                ),
            "backend", List.of(
                    "Spring Boot", "Hibernate", "Swagger", "Lombok", "PostgreSQL",
                        "MongoDB", "GraphQL", "Jakarta", "Slf4j", "JJWT", "JUnit", "Testcontainers"
                ),
                "frontend", List.of(
                        "React", "HTML", "CSS", "Javascript"
                ),
            "misc", List.of(
                    "Git", "SQL", "Docker", "LaTex", "Postman"
                )
        );
    }

    public void say_hi() {
        System.out.println("Hello! My name is " + this.name + " and I am a " + this.role + ".\n" +
        "Currently I live in " + this.city + ".\n" +
        "You can see my projects and my code style here.");
    }

    public static void main(String[] args) {
        BackendDeveloper me = new BackendDeveloper();
        me.say_hi();
    }
}

```

## 📝 Links
* Telegram: https://t.me/LuminiteTime
* Innopolis GitLab: https://gitlab.pg.innopolis.university/users/m.trifonov/projects

## 🔧 Technologies & Tools

### Languages:
![](https://img.shields.io/badge/Java-323330?style=for-the-badge&logo=oracle&logoColor=F80000)
![](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

### Frameworks:
![](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![](https://img.shields.io/badge/Spring-323436?style=for-the-badge&logo=spring&logoColor=6DB33F)

### Tools:
![](https://img.shields.io/badge/docker-369cee?style=for-the-badge&logo=docker&logoColor=white)
![](https://img.shields.io/badge/Postman-1f2021?style=for-the-badge&logo=postman&logoColor=FF6C37)
![](https://img.shields.io/badge/LaTeX-1f425f?style=for-the-badge&logo=latex)
![](https://img.shields.io/badge/Git-5f6870?style=for-the-badge&logo=git&logoColor=F05032)
![](https://img.shields.io/badge/PostgreSQL-3b3e40?style=for-the-badge&logo=postgresql&logoColor=4169E1)
![](https://img.shields.io/badge/MongoDB-1f2021?style=for-the-badge&logo=mongodb&logoColor=47A248)
