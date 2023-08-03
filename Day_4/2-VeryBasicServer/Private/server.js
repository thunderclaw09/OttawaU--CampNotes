// REQUIRE is basically "import"
// Note that this is unfinished because it would take too much time to finish. 

const http = require('http') // importing http and other things
const fs = require('fs') // need to read static files
const url = require('url') // to parse url strings

const ROOT_DIR = '../Public/' // Defining a root directory

const MIME_TYPES = 
{
    'css': 'text/css',
    'gif': 'image/gif',
    'htm': 'text/html',
    'html': 'text/html',
    'ico': 'image/x-icon',
    'jpeg': 'image/jpeg',
    'jpg': 'image/jpeg',
    'js': 'application/Scripts',
    'json': 'application/json',
    'png': 'image/png',
    'svg': 'image/svg+xml',
    'txt': 'text/plain'
}

function get_mime(filename) // This goes through and returns the type of file (I forgot why)
{
    for (let ext in MIME_TYPES)
    {
        if (filename.indexOf(ext, filename.length - ext.length) !== -1)
        {
            return MIME_TYPES[ext];
        }
    }
    return MIME_TYPES['txt']
}

http.createServer(function(request, response) { // Shows every single URL we visit / every request
    let urlObj = url.parse(request.url, true, false) // Helpful for debugging
    console.log("\n==========================")
    console.log("PATHNAME: " + urlObj.pathname)
    console.log("REQUEST: " + ROOT_DIR + urlObj.pathname)
    console.log("METHOD: " + request.method)

    let receivedData = ''

    //attached event handlers to collect the message data
    request.on('data', function(chunk) {
        receivedData += chunk
    })

}).listen(3000) // Starts server and puts it on port 3000


console.log('Server Running at http://127.0.0.1:3000 CNTL-C to quit')
console.log('To Test')
console.log('http://localhost:3000/index.html')