package PythonPackage;

import org.python.util.PythonInterpreter;

import java.util.ArrayList;
import java.util.List;

public class chromeBrowserUpgrade_test {
    public static void main(String[] args) {

        try {
            chromeBrowserUpgrade chromeBrowserUpgrade = new chromeBrowserUpgrade();
            chromeBrowserUpgrade.installPyModule("beautifulsoup4");

            List<String> command_driver = new ArrayList<>();
            command_driver.add("python");
            command_driver.add("C:\\Users\\NirmalaDeviKaliappan\\Desktop\\QA.Selenium-main_test\\SeleniumTests\\src\\PythonPackage\\chrome_driver_download.py");
            chromeBrowserUpgrade.readLine(command_driver);

        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
