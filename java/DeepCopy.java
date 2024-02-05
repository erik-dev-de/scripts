import java.io.IOException;
import java.nio.file.*;
import java.nio.file.attribute.BasicFileAttributes;

public class DeepCopy {
    public static void main(String[] args) {
        Path sourceFolder = Paths.get("");
        Path targetFolder = Paths.get("");


        try {
            Files.walkFileTree(sourceFolder, new SimpleFileVisitor<Path>() {
                @Override
                public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
                    Path relativePath = sourceFolder.relativize(file);
                    Path targetFile = targetFolder.resolve(relativePath.getFileName());
                    Files.copy(file, targetFile, StandardCopyOption.REPLACE_EXISTING);
                    return FileVisitResult.CONTINUE;
                }
            });
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
