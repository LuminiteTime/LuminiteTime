<div align="center">
<h1>Немного обо мне •ᴗ• </h1>
</div>

```java
// About me
import java.util.List;
import java.util.Map;

public class BackendDeveloper {
    private String name;
    private String city;
    private String role;
    private List<Map<String, String>> spokenLanguages;
    private Map<String, List<String>> stack;

    public BackendDeveloper() {
        this.name = "Mikhail Trifonov";
        this.city = "Innopolis";
        this.role = "Java & Scala Backend Developer";
        this.spokenLanguages = List.of(
                Map.of("language", "Russian", "level", "Native"),
                Map.of("language", "English", "level", "Upper-Intermediate")
        );
        this.stack = Map.of(
            "backend", List.of("Java", "Scala", "Spring Boot", "Hibernate", "gRPC", "GraphQL"),
            "databases", List.of("PostgreSQL", "MongoDB", "Redis"),
            "devops", List.of("Docker", "Kafka", "RabbitMQ", "Nginx", "Grafana", "Prometheus"),
            "tools", List.of("Git", "Maven", "Gradle", "JUnit", "Testcontainers")
        );
    }

    public void sayHi() {
        System.out.println("Hi! My name is " + this.name + " and I am a " + this.role + ".\n" +
        "Currently I live in " + this.city + ".\n" +
        "You can see my projects and my code style here.");
    }
    
    public static void main(String[] args) {
        BackendDeveloper me = new BackendDeveloper();
        me.sayHi();
    }
}
```


---

<div align="center">
<h3>Tech Stack</h3>
<p>
    <a href="#"><img src="https://skillicons.dev/icons?i=java,scala,spring,hibernate&perline=4" alt="languages"></a>
</p>
<p>
    <a href="#"><img src="https://skillicons.dev/icons?i=gradle,maven,docker,git,kafka,rabbitmq&perline=9" alt="devops"></a>
</p>
<p>
    <a href="#"><img src="https://skillicons.dev/icons?i=nginx,prometheus,grafana&perline=9" alt="devops"></a>
    <img src="https://go-skill-icons.vercel.app/api/icons?i=mysql" width="48" height="48" alt="SQL">
    <img src="https://skillicons.dev/icons?i=githubactions" width="48" height="48" alt="CI/CD">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/junit/junit-original.svg" width="48" height="48" style="background: #25A162; border-radius: 4px; padding: 8px;" alt="JUnit">
</p>
<p>
    <a href="#"><img src="https://skillicons.dev/icons?i=postgres,mongodb,redis&perline=3" alt="databases"></a>
    <a href="#"><img src="https://skillicons.dev/icons?i=graphql&perline=1" alt="GraphQL"></a>
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width="48" height="48" style="background: #009688; border-radius: 4px; padding: 8px;" alt="REST API">
    <img src="https://logo.svgcdn.com/l/grpc.svg" width="48" height="48" style="background: #244c5a; border-radius: 4px; padding: 8px;" alt="gRPC">
</p>
</div>

<div align="center">
<h3>Процессы</h3>
<p>
    <code style="background: linear-gradient(135deg, #0052CC, #0066FF); color: white; padding: 8px 12px; border-radius: 6px; font-weight: bold;">🔄 Agile</code>
    <code style="background: linear-gradient(135deg, #6DB33F, #8CC152); color: white; padding: 8px 12px; border-radius: 6px; font-weight: bold;">⚡ Scrum</code>
    <code style="background: linear-gradient(135deg, #0079BF, #00A3E0); color: white; padding: 8px 12px; border-radius: 6px; font-weight: bold;">📋 Kanban</code>
    <code style="background: linear-gradient(135deg, #F05032, #FF6B47); color: white; padding: 8px 12px; border-radius: 6px; font-weight: bold;">🔀 Git Workflow</code>
    <code style="background: linear-gradient(135deg, #0052CC, #2684FF); color: white; padding: 8px 12px; border-radius: 6px; font-weight: bold;">📊 Jira</code>
</p>
</div>

---

<div align="center">
<a href="https://t.me/LuminiteTime">
    <img src="https://img.icons8.com/color/48/telegram-app--v1.png" alt="Telegram" style="border-radius: 50%; box-shadow: 0 4px 8px rgba(0,0,0,0.3); transition: transform 0.2s;">
</a>
</div>
