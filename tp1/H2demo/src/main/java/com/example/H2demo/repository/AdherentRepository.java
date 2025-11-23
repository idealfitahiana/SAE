package com.example.H2demo.repository;

import com.example.H2demo.entities.Adherent;
import org.springframework.data.jpa.repository.JpaRepository;

public interface AdherentRepository extends JpaRepository<Adherent , Long> {
    void save(Object o, String a, String b, int i);
}
