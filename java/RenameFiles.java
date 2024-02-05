import java.io.File;
import java.io.IOException;

public class RenameFiles {
    public static void main(String[] args) throws IOException {
        String pathToDirectory = "";
        File directory = new File(pathToDirectory);
        File[] filesInDirectory = directory.listFiles();
        int i = 0;
        for(File file:filesInDirectory) {
            i++;
            String name = file.getName();
            String newName = "parasyte-the-maxim-" + name;
            String newPath = pathToDirectory + "\\" + newName;
            file.renameTo(new File(newPath));
            System.out.println(name + " changed to " + newName);
        }
    }
}