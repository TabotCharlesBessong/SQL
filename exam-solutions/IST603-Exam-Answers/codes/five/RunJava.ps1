param(
    [Parameter(Mandatory=$true)]
    [string]$FileName
)

# Remove .java extension if provided
$ClassName = $FileName -replace '\.java$', ''

# Check if Java file exists
if (-not (Test-Path "$ClassName.java")) {
    Write-Host "Error: $ClassName.java not found!" -ForegroundColor Red
    exit 1
}

Write-Host "=== Compiling $ClassName.java ===" -ForegroundColor Cyan
javac "$ClassName.java"

if ($LASTEXITCODE -ne 0) {
    Write-Host "Compilation failed!" -ForegroundColor Red
    exit 1
}

Write-Host "=== Running $ClassName ===" -ForegroundColor Cyan
java $ClassName

Write-Host "=== Execution completed with exit code: $LASTEXITCODE ===" -ForegroundColor $(if ($LASTEXITCODE -eq 0) { "Green" } else { "Red" })