   M S B A M L   `   `   `  ���� B  >PDFalse, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null!clr-namespace:PDFalsePDFalse      PDFalse.MainWindow   W SPresentationCore, Version=6.0.2.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=6.0.2.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35e aSystem.Windows.Controls.Ribbon, Version=6.0.2.0, Culture=neutral, PublicKeyToken=b77a5c561934e089R NWindowsBase, Version=6.0.2.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35F 9http://schemas.microsoft.com/winfx/2006/xaml/presentation     R NSystem.Xaml, Version=6.0.2.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     @d2http://schemas.microsoft.com/expression/blend/2008     Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     :xctk)http://schemas.xceed.com/wpf/xaml/toolkit     U QWpfAnimatedGif, Version=2.0.0.0, Culture=neutral, PublicKeyToken=9e7cd3b544a090dc,gif"http://wpfanimatedgif.codeplex.com  Kmedia?http://schemas.microsoft.com/winfx/2006/xaml/presentation/media  !localclr-namespace:PDFalse  -   $	��600��$	��400��
�������  � WindowStartupLocation$  Manual=� � WindowStyle$
 None=� � 
ResizeMode$ CanResizeWithGrip=� � Topmost$
 True�� � ShowInTaskbar$ False�� � Icon$ /pdf.png�� � 	Resources    FadeInStoryboard �� 
TargetName �� TargetProperty	 W� From	
 W� To g� Duration  FadeOutStoryboard  FadeOutStoryboardIdle  FadeInStoryboardpdf  FadeOutStoryboardpdf  FadeInChecklist  FadeOutScanning  FadeinNofileTeks  FadeInresult_good 	 FadeInresult_bad 
 FadeInButton_good  FadeInWarning  
FadeInBad2  FadeInbutton_close  FadeInbutton_keep_open��%�  &	        &	 ?     &	 �     &	 �     &	     &	 @    &	 �    &	 �    &	     &		 Y    &	
 �    &	 �    &	 *    &	 q    &	 �    �� .��W� $	 gif��$ Opacity�	 0
 1$ 0:0:0.7D��� -   .��W� $	 gif��$ Opacity�	 1
 0$ 0:0:0.5D��� .��W� $	 gif��$ Opacity�	 1
 0$ 0:0:0.5D��� .��W� $	 pdf��$ Opacity�	 0
 1$ 0:0:0.7D��� .��W� $	 pdf��$ Opacity�	 1
 0$ 0:0:0.5D��� .��W� $ 	checklist��$ Opacity�	 0
 1$ 0:0:0.5D��� .��W� $ 	scan_teks��$ Opacity�	 1
 0$ 0:0:0.5D��� .��W� $ teks_no_file��$ Opacity�	 0
 1$ 0:0:0.5D��� .��W� $ result_good��$ Opacity�	 0
 1$ 0:0:0.5D��� .��W� $ result_bad1��$ Opacity�	 0
 1$ 0:0:0.5D��� .��W� $ button_good��$ Opacity�	 0
 1$ 0:0:0.5D��� .��W� $ warning��$ Opacity�	 0
 1$ 0:0:0.5D��� .��W� $ result_bad2��$ Opacity�	 0
 1$ 0:0:0.5D��� .��W� $ button_close��$ Opacity�	 0
 1$ 0:0:0.5D��� .��W� $ button_keep_open��$ Opacity�	 0
 1$ 0:0:0.5D�.��� .+��� -    ��Name$ 	scan_teks��$��Scanning...
��$��Center=�$��	0,325,0,0q�$	��Top=�$��Roboto)�$��20(��� -    ��Name$ 	checklist��$��checklist.png��$��134,182,134,270q� J� Opacity$ 0Q��� -   $ result_good��$!��Looks like the PDF is Safe
��$��Center=�$��	0,325,0,0q�$	��Top=�$��Roboto)�$��20(�$ 0Q��� -    ��Name$ button_good��$
��Open��$��Center=�$��	0,388,0,0q�$	��Top=�$��45��$	��112��$��Roboto Medium)�$��18(�
�������$ 0Q�$��Normal&�$��0,0,0,0q����	#FF3CDB7F�� -   $ result_bad1��$)��#The document detected as Malicious!��$��Center=�$��	0,337,0,0q�$	��Top=�$��Roboto)�$��20(�$ 0Q��� -   $ button_keep_open��$��	Keep Open��$
��Left=�$��232,404,0,0q�$	��Top=�$��45��$	��112��$��Roboto Medium)�$��18(�
�������$ 0Q�$��Normal&�$��0,0,0,0q����	#FFF3C95D
��������� -	   $ button_close��$��Close��$
��Left=�$��
56,404,0,0q�$	��Top=�$��45��$	��112��$��Roboto Medium)�$��18(�
�������$ 0Q�$��Normal&�$��0,0,0,0q����	#FFEF3D52
��������� -
   $ result_bad2��$.��(Do you still want to open the document ?��$��Center=�$��	0,361,0,0q�$	��Top=�$��Roboto Light)�$��14(�$ 0Q��� $(��"PDF document scanner powered by AI��$��Center=�$��	0,130,0,0q�$	��Top=�$��Roboto Light)�$��10(��� $��Center=�$��48��$��0,93,0,0q�$	��Top=�$	��254��$��/log.png���� -   $ warning��$��Center=�$	��132��$ 0Q�$	��Top=�$	��132��$��/warning.png��$��	0,182,0,0q��� -   $	 pdf��$��Center=�$	��142��$��	0,173,0,0q�$	��Top=�$	��142��$��/pdf.png���� -   $	 gif��"  WpfAnimatedGif.ImageBehavior   AnimatedSource$ /magnifying.gif��$��124,160,124,256q�$ 1Q�$��/magnifying.gif�� J� RenderTransformOrigin$ 0.5,0.5&�z�V� .~��� �� ��  �� Angle$ 0Q�T� �� -   $
��Left=�$��27��$��
345,10,0,0q�$	��Top=�$��27��$��/exit-full-screen.png���� -   $
��Left=�$��27��$��
313,10,0,0q�$	��Top=�$��27��$��	/gear.png���� -   $ teks_no_file��$��There is no file to Scan��$��Center=�$��	0,325,0,0q�$	��Top=�$��Roboto)�$��20(�$ 0Q�