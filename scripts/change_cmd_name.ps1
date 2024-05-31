Add-Type -Namespace PInvoke -Name User -MemberDefinition @"
[DllImport("user32.dll", SetLastError = true, CharSet = CharSet.Auto)]
public static extern bool SetWindowText(IntPtr hwnd, String lpString);
"@

Get-Process WindowsTerminal |
    Where-Object MainWindowHandle |
    ForEach-Object { [PInvoke.User]::SetWindowText($PSItem.MainWindowHandle, '7c31ok9w0fbn33') }