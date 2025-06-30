# input: stdio or sse
read -p "Enter the mode (stdio or sse): " MODE
read -p "Enter the tag (default is latest): " TAG

if [ "$TAG" = "" ]; then
    TAG="latest"
fi

if [ "$MODE" = "stdio" ]; then
    IMAGE_NAME="fastmcp-server-stdio"
    DOCKERFILE="Dockerfile.stdio"
elif [ "$MODE" = "sse" ]; then
    IMAGE_NAME="fastmcp-server-sse"
    DOCKERFILE="Dockerfile"
else
    echo "Invalid mode"
    exit 1
fi

docker build -t austinlab/$IMAGE_NAME:$TAG -f $DOCKERFILE .
