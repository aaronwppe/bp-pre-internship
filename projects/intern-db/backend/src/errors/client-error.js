export default class ClientError extends Error {
  constructor(message, httpStatusCode) {
    super(message);
    this.httpStatusCode = httpStatusCode;
  }
}
