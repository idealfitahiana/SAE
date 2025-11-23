package com.example.demo;

import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@RestController
public class MyApi {

    public static List<Etudiant> liste = new ArrayList<>();

    static{
        liste.add(new Etudiant(0, "A", 19));
        liste.add(new Etudiant(1, "A", 19));
        liste.add(new Etudiant(2, "A", 19));
        liste.add(new Etudiant(3, "A", 19));
    }

    @GetMapping(value = "/liste")
    public List<Etudiant> getAllEtudiant(){
        return liste;
    }

    @GetMapping(value = "/b")
    public String bonjour(){
        return "Bonjour";
    }

    @GetMapping(value = "/bn")
    public String bonsoir(){
        return "Bonsoir";
    }

    @GetMapping(value = "/etudiant")
    public Etudiant getEtudiant(){
        return new Etudiant(1,"A", 19);
    }

    @GetMapping(value = "/somme")
    public double somme(double a, double b){
        return a+b;
    }

    @GetMapping(value = "getEtudiant")
    public Etudiant getEtudiant(int identifiant){
        return liste.get(identifiant);
    }

    @PostMapping(value = "addEtudiant")
    public Etudiant addEtudiant(Etudiant etudiant){
        liste.add(etudiant);
        return etudiant;
    }

    @DeleteMapping(value = "/delete")
    public void supprimerEtudiant(int identifiant){
        liste.remove(identifiant);
    }

    @PutMapping(value = "/modifier")
    public Etudiant modifierEtudiant(int identifiant, String nom){
        liste.get(identifiant).setNom(nom);
        return liste.get(identifiant);
    }
}
