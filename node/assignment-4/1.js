async function fetchData() {
    const delaySeconds = 2;

    // wait for 2 seconds
    await new Promise((resolve) => {
        setTimeout(resolve, delaySeconds * 1000);
    });

    const randomNumber = Math.floor(Math.random() * 2);

    if (!randomNumber) {
        // this is an implicit reject
        throw new Error("Failed to fetch data");
    }

    // implicit resolve
    return "Data fetched successfully";
}

async function main() {
    console.log(`Started executing '${fetchData.name}'`);

    try {
        // blocking call for async method
        // wait until its resolved or rejected
        const message = await fetchData();
        console.log(`Returned: ${message}`);
    } catch (error) {
        console.log(`Error: ${error.message}`);
    } finally {
        console.log(`Finished executing '${fetchData.name}'`);
    }
}

main();