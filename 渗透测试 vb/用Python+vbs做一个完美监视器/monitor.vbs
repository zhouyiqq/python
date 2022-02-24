Set colArgs = WScript.Arguments
If WScript.arguments.count < 3 then
WScript.Echo "USAGE:" & vbCrLf & " Monitor Computer User Password files"
WScript.quit
End If
strComputer = wscript.arguments(0)
strUser = wscript.arguments(1)
strPwd = wscript.arguments(2)
strFile = wscript.arguments(3)
set olct=createobject("wbemscripting.swbemlocator")
set wbemServices=olct.connectserver(strComputer,"root/cimv2",strUser,strPwd)
Set colMonitoredProcesses = wbemServices. _
ExecNotificationQuery("select * from __instancecreationevent " _
& " within 1 where TargetInstance isa 'Win32_Process'")
i = 0
Do While i = 0
Set objLatestProcess = colMonitoredProcesses.NextEvent
Wscript.Echo now & " " & objLatestProcess.TargetInstance.CommandLine
Set objFS = CreateObject("Scripting.FileSystemObject")
Set objNewFile = objFS.OpenTextFile(strFile,8,true)
objNewFile.WriteLine Now() & " " & objLatestProcess.TargetInstance.CommandLine
objNewFile.Close
Loop
