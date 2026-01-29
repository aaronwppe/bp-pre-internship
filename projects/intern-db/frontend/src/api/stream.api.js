import validateResponse from "../utils/response-validator";

export async function getAllStreams() {
  const url = new URL("stream/", import.meta.env.VITE_API_BASE_URL);

  const response = await fetch(url);
  const json = await response.json();

  validateResponse(url, response, json, "streams", Array.isArray);
  return json.data.streams;
}
