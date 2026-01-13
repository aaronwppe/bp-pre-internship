import fetch from "node-fetch";

async function fetchResource(baseUrl, resource) {
    const response = await fetch(new URL(resource, baseUrl));
    return response.json();
}

async function main() {
    const url = "https://jsonplaceholder.typicode.com";
    const postsResource = "posts";
    const commentsResource = "comments";

    let errorMessages = [];
    const onError = (error) => {
        errorMessages.push(error.message);
        return [];
    }

    // destructuring the result
    const [posts, comments] = await Promise.all([
        fetchResource(url, postsResource)
            .catch(onError),

        fetchResource(url, commentsResource)
            .catch(onError),
    ]);

    console.log(`Posts: ${posts.length}`);
    console.log(`Comments: ${comments.length}`);
    console.log(`Errors: ${errorMessages.length}`);
}

main();