from winreg import *
#Disable CMD
key = CreateKey(HKEY_CURRENT_USER,"Software\Policies\Microsoft\Windows\System")
SetValueEx(key,"DisableCMD",0,REG_DWORD,1)
#Remove clock
key = CreateKey(HKEY_CURRENT_USER,"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer")
SetValueEx(key,"HideClock",0,REG_DWORD,1)
#Screen Saver
key = CreateKey(HKEY_CURRENT_USER,"Software\Policies\Microsoft\Windows\ControlPanel\Desktop")
SetValueEx(key,"SCRNSAVE.EXE",0,REG_SZ,"Ribbons.scr")
#Password after screen saver
key = CreateKey(HKEY_CURRENT_USER,"Software\Policies\Microsoft\Windows\ControlPanel\Desktop")
SetValueEx(key,"ScreenSaverIsSecure",0,REG_SZ,1)
#Disables the theme gallery in the Personalization Control Panel
key = CreateKey(HKEY_CURRENT_USER,"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer")
SetValueEx(key,"NoThemesTab",0,REG_DWORD,1)
#Time untill screen saver appears
key = CreateKey(HKEY_CURRENT_USER,"Software\Policies\Microsoft\Windows\ControlPanel\Desktop")
SetValueEx(key,"ScreenSaveTimeOut",0,REG_DWORD,60)
#Remote shared folders are not added to My Network Places when you open a document in the shared folder
key = CreateKey(HKEY_CURRENT_USER,"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer")
SetValueEx(key,"NoRecentDocsNetHood",0,REG_DWORD,1)
#Specifies which theme file is applied to the computer the first time a user logs on
key = CreateKey(HKEY_CURRENT_USER,"Software\Policies\Microsoft\Windows\Personalization")
SetValueEx(key,"ThemeFile",0,REG_SZ,1)
#Removes the Desktop Cleanup Wizard
key = CreateKey(HKEY_CURRENT_USER,"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer")
SetValueEx(key,"NoDesktopCleanupWizard",0,REG_DWORD,1)
#Prevents users from saving certain changes to the desktop.
key = CreateKey(HKEY_CURRENT_USER,"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer")
SetValueEx(key,"NoSaveSettings",0,REG_DWORD,1)
#In worst case use this - Removes icons, shortcuts, and other default and user-defined items from the desktop, including Briefcase, Recycle Bin, Computer, and Network Locations.
key = CreateKey(HKEY_CURRENT_USER,"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer")
SetValueEx(key,"NoDesktop",0,REG_DWORD,1)