package com.example.H2demo;

import com.example.H2demo.repository.AdherentRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class H2demoApplication {

	public static void main(String[] args) {
		SpringApplication.run(H2demoApplication.class, args);
	}

    @Bean
    CommandLineRunner runner(AdherentRepository repository){
        return args -> {
            repository.save(null, "A", "B", 29);
            repository.save(null, "A", "B", 29);
            repository.save(null, "A", "B", 29);
            repository.save(null, "A", "B", 29);
            repository.save(null, "A", "B", 29);

        };
    }
}
