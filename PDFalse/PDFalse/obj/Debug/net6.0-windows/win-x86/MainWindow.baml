   M S B A M L   `   `   `  ����B  >PDFalse, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null!clr-namespace:PDFalsePDFalse  5	   	       PDFalse.MainWindow   5   	   W SPresentationCore, Version=6.0.2.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=6.0.2.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35e aSystem.Windows.Controls.Ribbon, Version=6.0.2.0, Culture=neutral, PublicKeyToken=b77a5c561934e089R NWindowsBase, Version=6.0.2.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35F 9http://schemas.microsoft.com/winfx/2006/xaml/presentation     5   	   R NSystem.Xaml, Version=6.0.2.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   :xctk)http://schemas.xceed.com/wpf/xaml/toolkit     5   	   U QWpfAnimatedGif, Version=2.0.0.0, Culture=neutral, PublicKeyToken=9e7cd3b544a090dc,gif"http://wpfanimatedgif.codeplex.com  5   	   Kmedia?http://schemas.microsoft.com/winfx/2006/xaml/presentation/media  5   	   !localclr-namespace:PDFalse  5	   	   $	��600��5      $	��400��6'   
�������  � WindowStartupLocation$  Manual=�5       � WindowStyle$ 
ToolWindow=�6;    � 
ResizeMode$ CanResizeWithGrip=�6T    � Topmost$
 True��6s    � ShowInTaskbar$ False��6�    � 	Resources 5         FadeInStoryboard �� 
TargetName �� TargetProperty W� From		 W� To
 g� Duration  FadeOutStoryboard  FadeInStoryboardpdf  FadeOutStoryboardpdf  FadeInChecklist  FadeOutScanning  FadeInresult_good  FadeInresult_bad  FadeInButton_good 	 FadeInWarning 
 
FadeInBad2  FadeInbutton_close  FadeInbutton_keep_open��%�  &	        &	 s     &	 �     &	 g    &	 �    &	 S    &	 �    &	 G    &	 �    &		 =    &	
 �    &	 /    &	 �    �� 5   
   .��5      W� $	 gif��6   $ Opacity�6;    06_   	 16h   $
 0:0:0.7D�6o   5      �� 5   
   -   5        .��5      W� $	 gif��6   $ Opacity�6:    16^   	 06g   $
 0:0:0.5D�6n   5      �� 5   
   .��5      W� $	 pdf��6   $ Opacity�6;    06_   	 16h   $
 0:0:0.7D�6o   5      �� 5   
   .��5      W� $	 pdf��6   $ Opacity�6:    16^   	 06g   $
 0:0:0.5D�6n   5      �� 5   
   .��5      W� $ 	checklist��6   $ Opacity�6@    06d   	 16m   $
 0:0:0.5D�6t   5      �� 5   
   .��5      W� $ 	scan_teks��6   $ Opacity�6@    16d   	 06m   $
 0:0:0.5D�6t   5      �� 5    
   .��5!      W� $ result_good��6   $ Opacity�6B    06f   	 16o   $
 0:0:0.5D�6v   5"      �� 5#   
   .��5$      W� $ result_bad1��6   $ Opacity�6B    06f   	 16o   $
 0:0:0.5D�6v   5%      �� 5&   
   .��5'      W� $ button_good��6   $ Opacity�6B    06f   	 16o   $
 0:0:0.5D�6v   5(      �� 5)   
   .��5*      W� $ warning��6   $ Opacity�6>    06b   	 16k   $
 0:0:0.5D�6r   5+      �� 5,   
   .��5-      W� $ result_bad2��6   $ Opacity�6B    06f   	 16o   $
 0:0:0.5D�6v   5.      �� 5/   
   .��50      W� $ button_close��6   $ Opacity�6C    06g   	 16p   $
 0:0:0.5D�6w   51      �� 52   
   .��53      W� $ button_keep_open��6   $ Opacity�6G    06k   	 16t   $
 0:0:0.5D�6{   54      55      .��57      � .+�59   
   �� -   5         ��Name$ 	scan_teks��59      $��Scanning...
��6#   $��Center=�6>   $��	0,325,0,0q�6[   $	��Top=�6n   $��Roboto)�6�   $��20(�6�   �� 5:   
   -   5         ��Name$ 	checklist��5:      $��checklist.png��6#   $��134,182,134,270q�6:    J� Opacity$ 0Q�6S   �� 5;   
   -   5        $ result_good��5;      $!��Looks like the PDF is Safe
��6%   $��Center=�6O   $��	0,325,0,0q�6l   $	��Top=�6   $��Roboto)�6�   $��20(�6�   $ 0Q�6�   �� 5<   
   -   5         ��Name$ button_good��5<      $
��Open��6&   $��Center=�65   $��	0,388,0,0q�6R   $	��Top=�6e   $��45��6}   $	��112��6�   $��Roboto Medium)�6�   $��18(�6�   
�������$ 0Q�6�   $��Normal&�6�   $��0,0,0,0q�6�   ���	#FF3CDB7F6$  �� 5=   
   -   5        $ result_bad1��5=      $)��#The document detected as Malicious!��6%   $��Center=�6S   $��	0,337,0,0q�6p   $	��Top=�6�   $��Roboto)�6�   $��20(�6�   $ 0Q�6�   �� 5>   
   -   5        $ button_keep_open��5>      $��	Keep Open��6,   $
��Left=�6@   $��232,404,0,0q�6[   $	��Top=�6p   $��45��6�   $	��112��6�   $��Roboto Medium)�6�   $��18(�6�   
�������$ 0Q�6�   $��Normal&�6�   $��0,0,0,0q�6�   ���	#FFF3C95D
�������6D  �� 5?   
   -   5        $ button_close��5?      $��Close��6B   $
��Left=�6R   $��
56,404,0,0q�6m   $	��Top=�6�   $��45��6�   $	��112��6�   $��Roboto Medium)�6�   $��18(�6�   
�������$ 0Q�6�   $��Normal&�6�   $��0,0,0,0q�6  ���	#FFEF3D52
�������6@  �� 5@   
   -	   5        $ result_bad2��5@      $.��(Do you still want to open the document ?��6%   $��Center=�6X   $��	0,361,0,0q�6u   $	��Top=�6�   $��Roboto Light)�6�   $��14(�6�   $ 0Q�6�   �� 5A   
   $(��"PDF document scanner powered by AI��6   $��Center=�6=   $��	0,130,0,0q�6Z   $	��Top=�6m   $��Roboto Light)�6�   $��10(�6�   �� 5B   
   $��Center=�6   $��48��6-   $��0,93,0,0q�69   $	��Top=�6K   $	��254��6c   $��/log.png��6o   �� 5C   
   -
   5        $ warning��5C      $��Center=�6!   $	��132��6>   $ 0Q�6K   $	��Top=�6W   $	��132��6o   $��/warning.png��6{   $��	0,182,0,0q�6�   �� 5D   
   -   5        $	 pdf��5D      $��Center=�6   $	��142��6:   $��	0,173,0,0q�6G   $	��Top=�6Z   $	��142��6r   $��/pdf.png��6~   �� 5E   
   -   5        $	 gif��5E      "  WpfAnimatedGif.ImageBehavior   AnimatedSource$ /magnifying.gif��6   $��124,160,124,256q�6P   $ 1Q�6i   $��/magnifying.gif��6u    J� RenderTransformOrigin$ 0.5,0.5&�6�   z�5F      V� 5G      .~�5H      �� �� 5I      �� 5J       �� Angle$ 0Q�6&   T� 5K      5L      5N      5O      5P      