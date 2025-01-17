package sistemasinformacion.practica5;

import java.io.IOException;
import java.util.Scanner;

public class Menu {

    private IndexerAndSearcher indSear;

    void showMenu() throws IOException {
        indSear = new IndexerAndSearcher(IndexerAndSearcher.AnalyzerType.Spanish, true);

        Scanner scanner = new Scanner(System.in);

        while (true) {
            try {

                System.out.println();
                System.out.println("Elige una opción:");
                System.out.println("1-Indexar directorio");
                System.out.println("2-Añadir documento al indice");
                System.out.println("3-Buscar término");
                System.out.println("4-Salir");

                switch (scanner.nextLine().trim()) {
                    case "1":
                        System.out.println("Introduzca el directorio para indexar:");
                        printCurrentDir();
                        indSear.addDirectory(scanner.nextLine());
                        indSear.commit();
                        break;
                    case "2":
                        System.out.println("Introduzca el fichero a indexar:");
                        printCurrentDir();
                        indSear.addFileToIndex(scanner.nextLine());
                        indSear.commit();
                        break;
                    case "3":
                        System.out.println("Introduzca la secuencia a buscar:");
                        indSear.search(scanner.nextLine());
                        break;
                    case "4":
                        System.out.println("Adiós!");
                        indSear.close();
                        return;
                    default:
                        System.out.println("Opción inválida");
                }
            }catch (IOException e){
                e.printStackTrace();
            }
        }
    }

    private void printCurrentDir() {
        System.out.print(System.getProperty("user.dir").replaceAll("\\\\","/")+'/');
    }

    //------------------------------------------------

    public static void main(String[] args) throws IOException {

//        IndexerAndSearcher.example();

        new Menu().showMenu();
    }
}
