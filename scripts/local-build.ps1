param (
    [string]$mode = $(Read-Host "Enter the mode (stdio or sse)"),
    [string]$tag = $(Read-Host "Enter the tag (default is latest)")
)

if ($tag -eq "") {
    $tag = "latest"
}

if ($mode -eq "stdio") {
    $ImageName = "fastmcp-server-stdio"
    $Dockerfile = "Dockerfile.stdio"
}
elseif ($mode -eq "sse") {
    $ImageName = "fastmcp-server-sse"
    $Dockerfile = "Dockerfile"
} 
else {
    Write-Host "Invalid mode"
    exit 1
}

docker build -t austinlab/${ImageName}:${Tag} -f ${Dockerfile} .
