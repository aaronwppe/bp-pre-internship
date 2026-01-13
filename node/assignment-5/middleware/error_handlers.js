const notFoundHandler = (req, res, next) => {
    res.status(404)
        .send("Page not found!");
};

const internalErrorHandler = (err, req, res, next) => {
    console.log(err);

    res.status(500)
        .send("Something went wrong!");
}

module.exports = { notFoundHandler, internalErrorHandler };