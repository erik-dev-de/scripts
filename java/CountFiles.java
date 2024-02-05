import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;

public class CountFiles {

    public static void main(String[] args) throws IOException {
        String pathToDirectory = "";
        File directory = new File(pathToDirectory);

        if (directory.exists()) {
            File[] subfolders = directory.listFiles(File::isDirectory);

            if (subfolders != null) {
                Arrays.sort(subfolders, Comparator.comparingInt(CountFiles::countNonHiddenFiles).reversed());

                BufferedWriter writer = new BufferedWriter(new FileWriter("count-output.txt"));
                int index = 0;
                for (File subfolder : subfolders) {
                    String newLineChar = index > 0 ? "\n" :"";
                    index++;
                    int fileCount = countNonHiddenFiles(subfolder);
                    writer.write(newLineChar + subfolder.getName() + ": " + fileCount);
                }
                writer.close();
            }
        } else {
            System.out.println("Invalid directory path");
        }
    }

    private static int countNonHiddenFiles(File directory) {
        File[] files = directory.listFiles(file -> !file.isHidden() && !file.getName().startsWith("."));
        return files != null ? files.length : 0;
    }
}
