import fetch from 'node-fetch';

async function getPosts(url, count) {
    try {
        // fetch the data from the url
        const response = await fetch(url);

        // convert to json
        let posts = await response.json();

        if (!Array.isArray(posts)) {
            throw new Error();
        }

        // pop elements starting from count
        posts.splice(count);

        // extract title and body
        posts = posts.map((post) => {
            return {
                title: post.title,
                body: post.body
            }
        });

        return posts;

    } catch (error) {
        throw new Error(`Unable to fetch posts from '${url}'`);
    }

}

async function main() {
    const url = "https://jsonplaceholder.typicode.com/posts";
    const posts = await getPosts(url, 5);
    console.log(posts);
}

main();