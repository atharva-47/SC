const http = require('http');
const fs = require('fs');
const path = require('path');

const server = http.createServer((req, res) => {
    // Extract the file name from the URL
    const fileName = req.url.slice(1); // Remove the leading '/'
    if (!fileName) {
        res.writeHead(400, { 'Content-Type': 'text/plain' });
        res.end('File name is required');
        return;
    }

    // Construct the file path
    const filePath = path.join(__dirname, fileName);

    // Check if the file exists and is accessible
    fs.access(filePath, fs.constants.F_OK, (err) => {
        if (err) {
            // File not found or inaccessible
            res.writeHead(404, { 'Content-Type': 'text/plain' });
            res.end('404 Not Found');
            return;
        }

        // Read the file and send its content to the client
        fs.readFile(filePath, 'utf8', (err, data) => {
            if (err) {
                // Error reading the file
                res.writeHead(500, { 'Content-Type': 'text/plain' });
                res.end('500 Internal Server Error');
                return;
            }

            // Send the file content
            res.writeHead(200, { 'Content-Type': 'text/plain' });
            res.end(data);
        });
    });
});

// Start the server
const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
