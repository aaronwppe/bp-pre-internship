import validateResponse from "../utils/response-validator";

export async function getAllColleges() {
  const url = new URL("college/", import.meta.env.VITE_API_BASE_URL);

  const response = await fetch(url);
  const json = await response.json();

  validateResponse(url, response, json, "colleges", Array.isArray);
  return json.data.colleges;
}
