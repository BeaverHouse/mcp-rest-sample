# How to run or connect to the MCP server

Currently I only use [Cursor](https://www.cursor.com/) to connect to the MCP server.

## Run the MCP server (Development)

You can test the MCP server with the MCP Inspector:

```bash
mcp dev run_mcp.py
```

## Connect to the MCP server

I tested the following configurations on the `.cursor/mcp.json` file, using container and SSE connection.  
Please refer to the [Cursor documentation](https://docs.cursor.com/context/model-context-protocol) for more information.

### Local Docker container

1. Build the docker image with `Dockerfile.stdio` file.  
   It only includes the MCP server with stdio transport.  
   For example:

   ```bash
   docker build -t austinlab/fastmcp-server-stdio -f Dockerfile.stdio .
   ```

2. Use the following configuration to connect to the MCP server.  
   Change the image name and port to the ones you want to use.

   ```json
   {
     "mcpServers": {
       "MCP_SAMPLE": {
         "command": "docker",
         "args": [
           "run",
           "-i",
           "--rm",
           "-p",
           "8001:8001",
           "austinlab/fastmcp-server-stdio"
         ]
       }
     }
   }
   ```

### SSE connection

1. Build the docker image with `Dockerfile` file.  
   It both includes the MCP server with SSE transport and the FastAPI server.  
   For example:

   ```bash
   docker build -t austinlab/fastmcp-server-sse -f Dockerfile .
   ```

2. Run the docker container.

   ```bash
   docker run -d -p 8001:8001 austinlab/fastmcp-server-sse
   ```

3. Use the following configuration to connect to the MCP server.  
   Change the URL to the one you want to use.
   You can also change to the remote URL if you deployed the server to the cloud.

   ```json
   {
     "mcpServers": {
       "MCP_SAMPLE": {
         "url": "http://localhost:8001/api/sse"
       }
     }
   }
   ```
