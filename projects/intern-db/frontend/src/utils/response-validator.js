import ApiError from "../errors/api-error";

export default function validateResponse(
  requestUrl,
  response,
  json,
  propertyName,
  propertyTypeValidator,
) {
  const errorParameters = {
    requestUrl: requestUrl,
    httpCode: response.status,
    httpMessage: response.statusText,
    apiMessage: json?.message ?? "",
  };

  let message;

  if (!response.ok || json?.success === false) {
    message = "Response returned with failure.";
  } else if (
    !json?.data ||
    (propertyName &&
      propertyTypeValidator &&
      !propertyTypeValidator(json.data[propertyName]))
  ) {
    message = "Response data object invalid.";
  }

  if (message) {
    throw new ApiError({ ...errorParameters, message });
  }
}
