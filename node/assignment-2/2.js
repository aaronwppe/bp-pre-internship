const fs = require("fs");

// blocking read method
function readLogFileSync(filePath, fileEnconding) {
    console.log('Starting Blocking Read:');

    try {
        const data = fs.readFileSync(filePath, { encoding: fileEnconding });
        console.log(data);
    } catch (err) {
        console.log(`ERROR: Unable to read ${filePath} '${filePath}' - ${err.message}`);
    }

    console.log('Ending Blocking Read:');
}

// non-blocking read method
async function readLogFileAsync(filePath, fileEnconding) {
    console.log('Starting Non-Blocking Read:');

    // handle async operation using callback
    fs.readFile(filePath, fileEnconding, (err, data) => {
        if (err) {
            console.log(`ERROR: Unable to read '${filePath}' - ${err.message}`);
            return;
        }

        console.log(data);
        console.log('Ending Non-Blocking Read:');
    });
}

const logFile = {
    path: "./log.txt",
    encoding: "utf-8",
};


readLogFileAsync(logFile.path, logFile.encoding);
readLogFileSync(logFile.path, logFile.encoding);

