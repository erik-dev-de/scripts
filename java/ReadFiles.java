import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class ReadFiles {

    private static boolean isReactFile(File file) {
        if (file.isFile()) {
            String fileName = file.getName();
            return fileName.endsWith(".ts") || fileName.endsWith(".tsx");
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        Path rootPath = Paths.get("");

        Files.walk(rootPath)
                .filter(path -> isReactFile(path.toFile()))
                .forEach(file -> {
                    try {
                        readAndPrintLines(file);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                });
    }

    private static void readAndPrintLines(Path filePath) throws IOException {
        try (BufferedReader reader = Files.newBufferedReader(filePath)) {
            String line;
            while ((line = reader.readLine()) != null) {
                if (line.contains("ETipDrept.")) {
                    String result = filePath.getFileName().toString().replaceAll(".tsx", "").replaceAll(".ts", "z`") + ": " + line;
                    System.out.println(result);
                }
            }
        }
    }
}
