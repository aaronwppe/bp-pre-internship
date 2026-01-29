import ClientError from "./client-error.js";

export default class DuplicateField extends ClientError {
  constructor(name, value) {
    super(`Duplicate field ${name}=${value}.`, 409);
    this.fieldName = name;
  }
}
