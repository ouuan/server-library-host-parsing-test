const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, {
    'Content-Type': 'text/plain',
    'Connection': 'close',
  });
  res.end(`[${req.headers.host}]`);
});

const port = 3000;
server.listen(port, () => {
  console.log(`Node server running on http://localhost:${port}`);
});
