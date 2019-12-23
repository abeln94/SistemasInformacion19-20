package sistemasinformacion.practica5;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.core.SimpleAnalyzer;
import org.apache.lucene.analysis.es.SpanishAnalyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.document.StringField;
import org.apache.lucene.document.TextField;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.queryparser.classic.ParseException;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.MMapDirectory;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.InvalidParameterException;


/**
 * Clase de ejemplo de un indexador y buscador usando Lucene
 *
 * @author sisinf
 */
public class IndexerAndSearcher {

    enum AnalyzerType {
        Simple,
        Standard,
        Spanish
    }

    public static final String STOPWORDS = "./res/stopwords.txt";
    private final static String INDEXDIR = "./res/indice";

    private IndexWriter index;

    public IndexerAndSearcher(AnalyzerType type, boolean keepIndex) throws IOException {
        Analyzer analyzer;
        switch (type) {
            case Simple:
                // Use SimpleAnalyzer
                analyzer = new SimpleAnalyzer();
                break;
            case Standard:
                // Use StandardAnalizer
                try {
                    FileReader reader = new FileReader(STOPWORDS);
                    analyzer = new StandardAnalyzer(reader);
                } catch (Exception e) {
                    System.out.println("Error leyendo fichero de Stop Words. Usando valor por defecto");
                    analyzer = new StandardAnalyzer();
                }
                break;
            case Spanish:
                // Use SpanishAnalyzer
                analyzer = new SpanishAnalyzer();
                break;
            default:
                throw new InvalidParameterException("Unknown analyzer type: " + type);
        }

        // Initialize index
        MMapDirectory directory = new MMapDirectory(Paths.get(INDEXDIR));
        IndexWriterConfig configuracionIndice = new IndexWriterConfig(analyzer);
        index = new IndexWriter(directory, configuracionIndice);
        if (keepIndex) {
            System.out.println("Índice cargado con " + index.numDocs() + " fichero" + (index.numDocs() == 1 ? "" : "s") + ".");
        } else {
            System.out.println("Índice nuevo creado.");
            index.deleteAll();
        }
    }

    /**
     * Añade un fichero al índice
     *
     * @param path ruta del fichero a indexar
     */
    public void addFileToIndex(String path) {
        try {
            BufferedReader inputStreamReader = new BufferedReader(new InputStreamReader(new FileInputStream(path)));

            Document doc = new Document();
            doc.add(new TextField("contenido", inputStreamReader));
            doc.add(new StringField("path", path, Field.Store.YES));
            index.addDocument(doc);
            System.out.println("El fichero " + path + " se ha añadido al índice.");
        } catch (FileNotFoundException e) {
            System.out.println("El fichero " + path + " no se ha podido encontrar.");
        } catch (IOException e) {
            System.out.println("El fichero " + path + " no se ha podido añadir al índice.");
        }
    }

    /**
     * Añade todos los ficheros en el directorio recursivamente al índice
     *
     * @param directory directorio a añadir
     * @throws IOException
     */
    public void addDirectory(String directory) throws IOException {
        Files.find(Paths.get(directory), 999,
                (p, bfa) -> bfa.isRegularFile())
                .forEach(path -> addFileToIndex(path.toString())
                );
    }

    /**
     * Guarda los cambios en el índice.
     */
    public void commit() throws IOException {
        index.commit();
    }

    /**
     * Cierra el índice.
     *
     * @throws IOException
     */
    public void close() throws IOException {
        index.close();
    }


    /**
     * Busca una palabra
     *
     * @param queryAsString palabra a buscar
     * @throws IOException
     */
    public void search(String queryAsString) throws IOException {

        if (index.numDocs() == 0) {
            System.out.println("No hay ficheros en el índice, no se puede buscar");
            return;
        }

        DirectoryReader directoryReader = DirectoryReader.open(index);
        IndexSearcher buscador = new IndexSearcher(directoryReader);

        QueryParser queryParser = new QueryParser("contenido", index.getAnalyzer());
        Query query;
        try {

            query = queryParser.parse(queryAsString);
            TopDocs resultado = buscador.search(query, index.numDocs());
            ScoreDoc[] hits = resultado.scoreDocs;

            String _s = hits.length == 1 ? "" : "s";
            System.out.println("\nBuscando " + queryAsString + ": Encontrado" + _s + " " + hits.length + " hit" + _s + ".");
            int i = 0;
            for (ScoreDoc hit : hits) {
                int docId = hit.doc;

                Document doc = buscador.doc(docId);
                System.out.println((++i) + ". " + doc.get("path") + "\t" + hit.score);
            }

        } catch (ParseException e) {
            throw new IOException(e);
        }
    }

    //----------------------------------------------------------------------

    /**
     * Programa principal de prueba.
     */
    public static void example() throws IOException {
        // Creamos el idexador / buscador
        IndexerAndSearcher searcher = new IndexerAndSearcher(

                // Analizador:
//                AnalyzerType.Simple,
//                AnalyzerType.Standard,
                AnalyzerType.Spanish,

                // index
//                true
                false
        );

        // files
//        searcher.addFileToIndex("./res/ficheros/uno.txt");
//        searcher.addFileToIndex("./res/ficheros/dos.txt");
//        searcher.addFileToIndex("./res/ficheros/tres.txt");
//        searcher.addFileToIndex("./res/ficheros/cuatro.txt");
        searcher.addDirectory("./res/ficheros");

        // search
//        searcher.search("Contaminación");
        searcher.search("contaminacion");
        searcher.search("contaminación");
        searcher.search("cambio climatico");
        searcher.search("cambio climático");
//        searcher.search("cambio");
//        searcher.search("climatico");
        searcher.search("por");
        searcher.search("aeropuerto");

        searcher.close();

        System.out.println("-------------------------------------------------------");
    }

}


