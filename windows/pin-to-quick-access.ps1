# Adds folders in folderPath to your quick access

$folderPath = "" # your folder here

$folders = Get-ChildItem -Path $folderPath -Directory

$o = new-object -com shell.application

foreach ($folder in $folders) {
    $o.NameSpace($folder.FullName).Self.InvokeVerb('pintohome')
}
