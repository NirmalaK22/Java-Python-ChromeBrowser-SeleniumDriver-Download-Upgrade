package PythonPackage;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class chromeBrowserUpgrade {
    public void downloadChromeBrowser() {
        try {
            upgradepython();
            installPyModule("psutil");
            installPyModule("beautifulsoup4"); //it is to use soup,to extract the data from webpages

//chrome browser upgrade
//            List<String> command_browser = new ArrayList<>();
//            command_browser.add("python");
//            command_browser.add("C:\\Users\\NirmalaDeviKaliappan\\Desktop\\QA.Selenium-main_test\\SeleniumTests\\src\\PythonPackage\\chrome_browser_upgrade.py");
//            readLine(command_browser);
//chrome driver download and utilise
            List<String> command_driver = new ArrayList<>();
            command_driver.add("python");
            command_driver.add("C:\\Users\\NirmalaDeviKaliappan\\Desktop\\QA.Selenium-main_test\\SeleniumTests\\src\\PythonPackage\\chrome_driver_download.py");
            readLine(command_driver);


        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void readLine(List<String> command) {
        try {
            ProcessBuilder processBuilder = new ProcessBuilder(command);
            Process process = processBuilder.start();

            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            System.out.println("reading python code");
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            BufferedReader errorReader = new BufferedReader(new InputStreamReader(process.getErrorStream()));
            while ((line = errorReader.readLine()) != null) {
                System.err.println(line);
            }

            int exitCode = process.waitFor();
            System.out.println("Exited with code: " + exitCode);
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    public void upgradepython() {
        try {
            String pythonCmd = "python";
            String[] pythonArgs = {"-m", "pip", "install", "--upgrade", "pip"};
            ProcessBuilder pb = new ProcessBuilder(pythonCmd);
            pb.command().addAll(Arrays.asList(pythonArgs));
            pb.inheritIO();
            Process process = pb.start();
            process.waitFor();
        } catch (Exception e) {
            System.out.println("Exception in upgrading: " + e);
        }
    }

    public void installPyModule(String module_name) {
        try {
            String pythonCmd = "python";
            String[] pythonArgs = {"-m", "pip", "install", module_name};
            ProcessBuilder pb = new ProcessBuilder(pythonCmd);
            pb.command().addAll(Arrays.asList(pythonArgs));
            pb.inheritIO();
            Process process = pb.start();
            process.waitFor();
            System.out.println("installation of Python module- " + module_name + " is in last stage");
        } catch (Exception e) {
            System.out.println("Exception in installing python module: " + e);
        }
    }

}
