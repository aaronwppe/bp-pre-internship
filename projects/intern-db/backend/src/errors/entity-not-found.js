import ClientError from "./client-error.js";

export default class EntityNotFound extends ClientError {
  constructor(entityName, fieldName, fieldValue) {
    super(
      `'${entityName}' with '${fieldName}=${fieldValue}' does not exist.`,
      404,
    );
  }
}
