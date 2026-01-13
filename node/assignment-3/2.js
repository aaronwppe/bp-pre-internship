function fetchData() {
    const delaySeconds = 2;

    // async operation 
    // only resolves or rejects after 2 seconds
    return new Promise((resolve, reject) => {

        setTimeout(() => {
            // generate a random number 0 or 1
            const randomNumber = Math.floor(Math.random() * 2);

            // 0 = reject
            if (!randomNumber) {
                return reject(new Error("Failed to fetch data"));
            }

            // 1 = resolve
            return resolve("Data fetched successfully");

        }, delaySeconds * 1000);
    });
}

function main() {
    console.log(`Started executing '${fetchData.name}'`);

    // handle callbacks for promise
    fetchData()
        .then((message) => {
            console.log(`Returned: ${message}`);
        })
        .catch((error) => {
            console.log(`Error: ${error.message}`);
        })
        .finally(() => {
            console.log(`Finished executing '${fetchData.name}'`);
        });
}

main();