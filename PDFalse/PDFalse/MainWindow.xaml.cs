using System;
using System.Windows;
using System.Windows.Input;
using System.Windows.Media.Animation;
using System.Threading;
using System.Diagnostics;
using System.IO;

namespace PDFalse
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public int scan_result =3;
        public string pdf_opener;
        public string currentDirectory = AppDomain.CurrentDomain.BaseDirectory;


        public MainWindow()
        {
            InitializeComponent();
            AddHandler(Window.LoadedEvent, new RoutedEventHandler(Window_Loaded));
        }
        
        private void StartStoryboard()
        {
            // Use the Dispatcher to execute the code on the UI thread
            Dispatcher.Invoke(() =>
            {
                Storyboard storyboard = (Storyboard)FindResource("FadeInStoryboard");
                storyboard.Begin();
                Storyboard storyboardpdf = (Storyboard)FindResource("FadeInStoryboardpdf");
                storyboardpdf.Begin();
            });

        }

        private void Window_MouseDown(object sender, MouseButtonEventArgs e)
        {
            try
            {
                if (e.ChangedButton == MouseButton.Left)
                    this.DragMove();
            }
            catch (Exception ex)
            {

            }
            
        }

        private async void Window_Loaded(object sender, RoutedEventArgs e)
        {
            string[] args = Environment.GetCommandLineArgs();
            if (args.Length == 1)
            {
                this.idle();
            }
            else
            {
                // Thread untuk loading screen
                Thread loading = new Thread(StartStoryboard);
                loading.Start();

                // Thread untuk proses scan
                Thread scan = new Thread(FadeInStoryboard_Completed);
                scan.Start();

            }


        }

        private void idle()
        {
            Storyboard fadeOutStoryboard = (Storyboard)FindResource("FadeOutStoryboardIdle");
            fadeOutStoryboard.Begin();
            Storyboard fadeOutScanning = (Storyboard)FindResource("FadeOutScanning");
            fadeOutScanning.Begin();
            Storyboard fadeinTeks = (Storyboard)FindResource("FadeinNofileTeks");
            fadeinTeks.Begin();

        }

        private void FadeInStoryboard_Completed()
        {
            string[] args = Environment.GetCommandLineArgs();
            string arg1 = args[1];
            /*Thread.Sleep(1000);*/
            string command = "python";
            string arguments3 = string.Format(@"-W ignore ""{0}\script.py"" ""{1}"" ""{0}",currentDirectory,arg1);
            /*string arguments = "dir";*/
            ProcessStartInfo startInfo3 = new ProcessStartInfo();
            startInfo3.FileName = command;
            startInfo3.Arguments = arguments3;
            startInfo3.UseShellExecute = false;
            startInfo3.RedirectStandardError = true;
            startInfo3.RedirectStandardOutput = true;
            startInfo3.CreateNoWindow = true;

            Process process3 = new Process();
            process3.StartInfo = startInfo3;
            process3.Start();
            
            string output = process3.StandardOutput.ReadToEnd();
            string error = process3.StandardError.ReadToEnd();
           /* MessageBox.Show(output);
            MessageBox.Show(error);*/
            try
            {
                scan_result = int.Parse(output);   // Error
            }
            catch (Exception ex)
            {
                MessageBox.Show("An Error Occured, please report to developer");
                MessageBox.Show(error);
                Environment.Exit(0);
                this.Close();
            }
            
            process3.WaitForExit();

            //
            //
            //--------------------------------------------------------------------------

            Dispatcher.Invoke(() =>
            {
                Storyboard fadeOutStoryboard = (Storyboard)FindResource("FadeOutStoryboard");
                fadeOutStoryboard.Begin();
                Storyboard fadeOutStoryboardpdf = (Storyboard)FindResource("FadeOutStoryboardpdf");
                fadeOutStoryboardpdf.Begin();
                Storyboard fadeOutScanning = (Storyboard)FindResource("FadeOutScanning");
                fadeOutScanning.Begin();

            });

            
        }

        private void FadeOutStoryboard_Completed(object sender, EventArgs e)
        {

            if (scan_result == 0) // if safe
            {
                Storyboard fadeInChecklist = (Storyboard)FindResource("FadeInChecklist");
                fadeInChecklist.Begin();
                Storyboard fadeInresult_good = (Storyboard)FindResource("FadeInresult_good");
                fadeInresult_good.Begin();
                Storyboard fadeInButton_good = (Storyboard)FindResource("FadeInButton_good");
                fadeInButton_good.Begin();
            }
            else if(scan_result == 1) // if Malicious
            {
                Storyboard FadeInWarning = (Storyboard)FindResource("FadeInWarning");
                FadeInWarning.Begin();
                Storyboard FadeInresult_bad = (Storyboard)FindResource("FadeInresult_bad");
                FadeInresult_bad.Begin();
                Storyboard FadeInBad2 = (Storyboard)FindResource("FadeInBad2");
                FadeInBad2.Begin();
                Storyboard FadeInbutton_close = (Storyboard)FindResource("FadeInbutton_close");
                FadeInbutton_close.Begin();
                Storyboard FadeInbutton_keep_open = (Storyboard)FindResource("FadeInbutton_keep_open");
                FadeInbutton_keep_open.Begin();
            }
            else
            {
                MessageBox.Show("Error Occured, please report to developer");
                Environment.Exit(0);
                this.Close();
            }
            
        }

        // Tombol Buka
        private void Button_Click(object sender, RoutedEventArgs e)
        {
            string[] args = Environment.GetCommandLineArgs();
            string arg1 = args[1];
            string path_name = string.Format("{0}\\user.setting", currentDirectory);
            string temp = File.ReadAllText(path_name);
            string command = string.Format(@"""{0}""",temp);
            string arguments3 = String.Format(@"""{0}""",arg1);
            ProcessStartInfo startInfo = new ProcessStartInfo();
            startInfo.FileName = command;
            startInfo.Arguments = arguments3;
            startInfo.UseShellExecute = false;
            startInfo.RedirectStandardError = true;
            Process process = new Process();
            process.StartInfo = startInfo;
            try
            {
                process.Start();
                Environment.Exit(0);
                this.Close();

            }
            catch (Exception ex)
            {
                MessageBox.Show("An Error Occured, please report to developer");
                MessageBox.Show("Make sure you already specified PDF reader in Setting...");
                Setting popup = new Setting();
                popup.ShowDialog();

            }
       

            //Jika terjadi Error, Mungkin dari 
            if(process.ExitCode != 0)
            {
                string error = process.StandardError.ReadToEnd();
                MessageBox.Show("An Error Occured, please report to developer");
                MessageBox.Show(error);
            }
            
            Environment.Exit(0);
            this.Close();
        }

        // Tombol Exit
        private void Button_Close_Click(object sender, RoutedEventArgs e)
        {

            Environment.Exit(0);
            this.Close();
        }

        private void Button_Setting_Click(object sender, RoutedEventArgs e)
        {

            Setting popup = new Setting();
            popup.ShowDialog();
            
        }

    }
}
