import ApiError from "../errors/api-error";
import validateResponse from "../utils/response-validator";

const BASE_INTERN_URL = new URL("intern/", import.meta.env.VITE_API_BASE_URL);

export async function getAllInterns() {
  const url = BASE_INTERN_URL;

  const response = await fetch(url);
  const json = await response.json();

  validateResponse(url, response, json, "interns", Array.isArray);
  return json.data.interns;
}

export async function createIntern(intern) {
  const url = BASE_INTERN_URL;

  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(intern),
  });

  const json = await response.json();

  validateResponse(
    url,
    response,
    json,
    "internId",
    (internId) => typeof internId === "string",
  );

  return json.data.internId;
}

export async function updateIntern(intern) {
  const url = new URL(`${intern.id}`, BASE_INTERN_URL);

  const response = await fetch(url, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(intern),
  });

  const json = await response.json();

  validateResponse(url, response, json);
}

export async function deleteIntern(internId) {
  const url = new URL(`${internId}`, BASE_INTERN_URL);
  const response = await fetch(url, { method: "DELETE" });
  const json = await response.json();

  validateResponse(url, response, json);
}

export async function deleteInterns(internIds) {
  if (internIds.length === 1) {
    return deleteIntern(internIds[0]);
  }

  const url = new URL("batch", BASE_INTERN_URL);

  const response = await fetch(url, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ internIds }),
  });

  const json = await response.json();

  validateResponse(url, response, json, "failed", Array.isArray);

  if (json.data.failed.length > 0) {
    throw new ApiError({
      requestUrl: url,
      httpCode: response.status,
      httpMessage: response.statusText,
      apiMessage: json.message ?? "",
      message: `Failed to delete interns of ids: [${json.data.failed}]`,
    });
  }
}
