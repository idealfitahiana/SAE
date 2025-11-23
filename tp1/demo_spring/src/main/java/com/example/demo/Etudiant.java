package com.example.demo;

public class Etudiant {
    private int identifiant;
    private String nom;
    private double moyenne;

    public Etudiant(){}

    public Etudiant(int identifiant,  String nom, double moyenne) {
        this.identifiant = identifiant;
        this.moyenne = moyenne;
        this.nom = nom;
    }

    public int getIdentifiant() {
        return identifiant;
    }

    public void setIdentifiant(int identifiant) {
        this.identifiant = identifiant;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public double getMoyenne() {
        return moyenne;
    }

    public void setMoyenne(double moyenne) {
        this.moyenne = moyenne;
    }
}
