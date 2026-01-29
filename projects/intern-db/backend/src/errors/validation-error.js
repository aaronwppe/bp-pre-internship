import ClientError from "./client-error.js";

export default class ValidationError extends ClientError {
  constructor(errors) {
    super(errors.toString(), 400);
  }
}
