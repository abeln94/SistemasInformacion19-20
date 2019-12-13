package sistemasinformacion.practica5;

import java.io.IOException;
import java.util.Scanner;

public class Menu {

    private IndexerAndSearcher indSear;

    void showMenu() throws IOException {
        indSear = new IndexerAndSearcher();
        indSear.useSpanishAnalizer();
        indSear.createIndex();

        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Elige una opción:");
            System.out.println("1-Indexar directorio");
            System.out.println("2-Añadir documento al indice");
            System.out.println("3-Buscar termino");
            System.out.println("4-Salir");

            switch (scanner.nextLine()) {
                case "1":
                    indSear.addDirectory(scanner.nextLine());
                    break;
                case "2":
                    indSear.addFileToIndex(scanner.nextLine());
                    break;
                case "3":
                    indSear.search(scanner.nextLine());
                    break;
                case "4":
                    return;
            }
        }
    }

    public static void main(String[] args) {
        try {
            new Menu().showMenu();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
