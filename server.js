const express = require('express');
   const fs = require('fs');
   const path = require('path');
   const app = express();
   const port = 3000;

   // Middleware to parse form data
   app.use(express.urlencoded({ extended: true }));

   // Serve the HTML form
   app.get('/', (req, res) => {
       res.sendFile(path.join(__dirname, 'index.html'));
   });

   // Handle form submission
   app.post('/append', (req, res) => {
       const file1 = req.body.file1;
       const file2 = req.body.file2;

       // Read the contents of the first file
       fs.readFile(file1, 'utf8', (err, data) => {
           if (err) {
               return res.status(500).send(`Error reading ${file1}: ${err.message}`);
           }

           // Append the contents to the second file
           fs.appendFile(file2, data, (err) => {
               if (err) {
                   return res.status(500).send(`Error appending to ${file2}: ${err.message}`);
               }

               res.send(`Contents of ${file1} have been appended to ${file2}`);
           });
       });
   });

   // Start the server
   app.listen(port, () => {
       console.log(`Server is running on http://localhost:${port}`);
   });
