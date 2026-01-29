import { ClientError } from "../errors/index.js";

const errorHandler = (err, req, res, next) => {
  if (!err) {
    next();
  }

  console.log(err);

  if (err instanceof ClientError) {
    return res.status(err.httpStatusCode).json({
      success: false,
      message: err.message,
    });
  }

  return res.status(500).json({
    success: false,
    message: "Internal Server Error.",
  });
};

export default errorHandler;
