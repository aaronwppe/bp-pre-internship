const fs = require("fs");

function runLogger(logFileObject) {
    try {
        // check if file already exists
        if (!fs.existsSync(logFileObject.path)) {

            // create a new file with heading
            fs.writeFileSync(logFileObject.path, logFileObject.header, logFileObject.encoding);
        }

        // Write a log with timestamp
        const message = `${new Date()} - ${__filename} was executed.\n`;
        fs.writeFileSync(logFileObject.path, message, { encoding: logFileObject.encoding, flag: "a" });
    }
    catch (err) {
        console.log("ERROR: Logger failed to run!");
    }
}

const logFile = {
    path: "./log.txt",
    header: "This is a log file.\n",
    encoding: "utf-8",
};

runLogger(logFile);