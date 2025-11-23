//SOAP : Simple Object Access Protocol
// JAX-WS (Java Annotation XML for WEB Service)
// JAXB (Java Architecture XML Building)

// URL: Uniform Resource Locator
// URN: Uniform Resource Name
// URI: Uniform Resource Identifier
// URN+URI= URI

import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.jws.WebService;

@WebService(targetNamespace = "http://www.polytech.fr")
public class MonserviceWeb {

    @WebMethod(operationName = "convertir")
    public double conversion(double mt){
        return mt*0.9;
    }

    public double somme(@WebParam(name = "parametre1") double a, double b ){
        return a+b;
    }

    public Etudiant getEtudiant(int identifiant){
        return new Etudiant(1, "Mario", 19);
    }
}
