# Disable confirmation prompts for the Set-DisplayResolution cmdlet
$ConfirmPreference = 'None'

# Change the display resolution
Set-DisplayResolution -Width 1920 -Height 1080 -Force
