import { Stream } from "../models/index.js";

export function getAllStreams(req, res) {
  const streams = Stream.getAll().map((stream) => stream.name);

  return res.status(200).json({
    success: true,
    data: { streams },
    message: "Fetched all streams.",
  });
}
