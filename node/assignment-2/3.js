function main() {
    console.log("Started main()");

    console.log("Started setTimeout()");
    setTimeout(() => console.log("Finshed setTimeout()!"), 0);

    console.log("Started setImmediate()");
    setImmediate(() => console.log("Finished setImmediate()!"));

    console.log("Started process.nextTick()");
    process.nextTick(() => console.log("Finished process.nextTick()!"));

    console.log("Finished main()!");
}

main();