export default class ApiError extends Error {
  constructor({ requestUrl, httpCode, httpMessage, apiMessage, message }) {
    super(
      `${requestUrl} - ${httpCode} - ${httpMessage} - ${apiMessage} - ${message}`,
    );
  }
}
