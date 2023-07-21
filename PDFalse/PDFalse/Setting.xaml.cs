using Microsoft.Win32;
using System;
using System.IO;
using System.Windows;


namespace PDFalse
{
    /// <summary>
    /// Interaction logic for Setting.xaml
    /// </summary>
    public partial class Setting : Window
    {

        public string currentDirectory = AppDomain.CurrentDomain.BaseDirectory;
        
        public Setting()
        {
            InitializeComponent();
            AddHandler(Window.LoadedEvent, new RoutedEventHandler(Window_Loaded));
        }

       

        public string path_name
        {
            get { return path.Text; }
        }

        private async void Window_Loaded(object sender, RoutedEventArgs e)
        {
            try
            {
                string path_name = string.Format("{0}\\user.setting", currentDirectory);
                string temp = File.ReadAllText(path_name);
                path.Text = temp.Replace("\n", String.Empty);
            }
            catch (Exception ex)
            {

            }
            
        }

            private void Button_Click(object sender, RoutedEventArgs e)
        {
            OpenFileDialog fdlg = new OpenFileDialog();
            fdlg.Title = "C# Corner Open File Dialog";
            fdlg.InitialDirectory = @"c:\";
            fdlg.Filter = "All files (*.*)|*.*|All files (*.*)|*.*";
            fdlg.FilterIndex = 2;
            fdlg.RestoreDirectory = true;

            // Show save file dialog box
            Nullable<bool> result = fdlg.ShowDialog();

            // Process save file dialog box results
            if (result == true)
            {
                // Save document
                path.Text = fdlg.FileName;
            }
        }

        private void save(object sender, RoutedEventArgs e)
        {
            string currentDirectory = AppDomain.CurrentDomain.BaseDirectory;
            string path_name = string.Format("{0}\\user.setting", currentDirectory);
            string user_setting = path.Text.Replace("\n",String.Empty);
            using (StreamWriter writer = new StreamWriter(path_name))
            {
                writer.Write(user_setting);
            }
            this.Close();
        }

        
    }
}
