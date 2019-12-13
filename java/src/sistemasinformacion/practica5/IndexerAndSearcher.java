package sistemasinformacion.practica5;

import org.apache.lucene.analysis.es.SpanishAnalyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.document.TextField;
import org.apache.lucene.document.StringField;
import org.apache.lucene.document.Field;
import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.core.SimpleAnalyzer;

import org.apache.lucene.search.*;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.MMapDirectory;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.queryparser.classic.ParseException;


import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.Collection;
import java.nio.file.Paths;


/**
 * Clase de ejemplo de un indexador y buscador usando Lucene
 *
 * @author sisinf
 */
public class IndexerAndSearcher {

    public static final String STOPWORDS = "./res/stopwords.txt";
    private final static String INDEXDIR = "./res/indice";


    /**
     * Analizar utilizado por el indexador / buscador
     */
    private Analyzer analyzer;

    private IndexWriter index;

    private int n;

    public IndexerAndSearcher() {
        n = 0;
    }

    /**
     * Añade un fichero al índice
     *
     * @param path ruta del fichero a indexar
     * @throws IOException
     */
    public void addFileToIndex(String path)
            throws IOException {
        InputStream inputStream = new FileInputStream(path);
        BufferedReader inputStreamReader = new BufferedReader(
                new InputStreamReader(inputStream, StandardCharsets.UTF_8));

        Document doc = new Document();
        doc.add(new TextField("contenido", inputStreamReader));
        doc.add(new StringField("path", path, Field.Store.YES));
        index.addDocument(doc);
        n++;
    }

    public void addDirectory(String directory) throws IOException {
        Files.find(Paths.get(directory), 999, (p, bfa) -> bfa.isRegularFile()).forEach(path -> {
            try {
                addFileToIndex(path.toString());
            } catch (IOException e) {
                e.printStackTrace();
            }
        });
    }

    public void useSimpleAnalizer() {
        analyzer = new SimpleAnalyzer();
    }

    public void useStandarAnalyzer() {
        try {
            FileReader reader = new FileReader(STOPWORDS);
            analyzer = new StandardAnalyzer(reader);
        } catch (Exception e) {
            System.out.println("Error leyendo fichero de Stop Words. Usando valor por defecto");
            analyzer = new StandardAnalyzer();
        }
    }

    public void useSpanishAnalizer() {
        analyzer = new SpanishAnalyzer();
    }


    /**
     * Indexa los ficheros incluidos en "ficherosAIndexar"
     *
     * @return un índice (Directory) en memoria, con los índices de los ficheros
     * @throws IOException
     */
    public void createIndex() throws IOException {
        initializeIndex(new MMapDirectory(Paths.get(INDEXDIR)));
    }

    public void useExistingIndex() throws IOException {
        initializeIndex(MMapDirectory.open(Paths.get(INDEXDIR)));
    }

    public void initializeIndex(Directory directory) throws IOException {
        IndexWriterConfig configuracionIndice = new IndexWriterConfig(analyzer);
        index = new IndexWriter(directory, configuracionIndice);
    }


    /**
     * Busca la palabra indicada en queryAsString en el directorioDelIndice.
     *
     * @param queryAsString
     * @throws IOException
     */
    public void search(String queryAsString) throws IOException {

        DirectoryReader directoryReader = DirectoryReader.open(index);
        IndexSearcher buscador = new IndexSearcher(directoryReader);

        QueryParser queryParser = new QueryParser("contenido", analyzer);
        Query query;
        try {

            query = queryParser.parse(queryAsString);

            TopDocs resultado = buscador.search(query, n);
            ScoreDoc[] hits = resultado.scoreDocs;

            System.out.println("\nBuscando " + query + ": Encontrados " + hits.length + " hits.");
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

//    /**
//     * Programa principal de prueba. Rellena las colecciones "ficheros" y "queries"
//     *
//     * @param args
//     * @throws IOException
//     */
//    public static void main(String[] args) throws IOException {
//        // Creamos el idexador / buscador
//        IndexerAndSearcher searcher = new IndexerAndSearcher();
//
//        // Analizer
////        searcher.useStandarAnalyzer();
//        searcher.useSpanishAnalizer();
//
//        // index
//        searcher.createIndex();
////        searcher.addFileToIndex("./res/ficheros/uno.txt");
////        searcher.addFileToIndex("./res/ficheros/dos.txt");
////        searcher.addFileToIndex("./res/ficheros/tres.txt");
////        searcher.addFileToIndex("./res/ficheros/cuatro.txt");
//        searcher.addDirectory("./res/ficheros");
//
//        // search
//        searcher.search("Contaminación");
//        searcher.search("contaminacion");
//        searcher.search("cambio climatico");
//        searcher.search("cambio climático");
//        searcher.search("cambio");
//        searcher.search("climatico");
//        searcher.search("por");
//        searcher.search("aeropuerto");
//
//    }

}


