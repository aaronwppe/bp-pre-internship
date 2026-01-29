import { body, validationResult } from "express-validator";
import { ValidationError } from "../errors/index.js";

function requiredStringValidator(field) {
  return body(field)
    .exists()
    .withMessage(`'${field}' is a required 'field'.`)
    .bail()
    .isString()
    .withMessage(`${field} field should be of type 'string'.`)
    .bail()
    .trim()
    .notEmpty()
    .withMessage(`${field} field cannot be empty.`)
    .bail();
}

function evaluateValidationResult(req, res, next) {
  const errors = validationResult(req);

  if (!errors.isEmpty()) {
    throw new ValidationError(errors.array().map((e) => e.msg));
  }

  next();
}

export const internBodyValidator = [
  requiredStringValidator("name"),
  requiredStringValidator("githubUsername"),
  requiredStringValidator("stream"),
  requiredStringValidator("college"),
  evaluateValidationResult,
];

export const batchDeleteValidator = [
  body("internIds")
    .exists()
    .withMessage("`internIds` is a required field.")
    .bail()
    .isArray({ min: 2 })
    .withMessage(
      "'internIds' field should be of type 'array' with atleast 2 ids.",
    ),
  evaluateValidationResult,
];
