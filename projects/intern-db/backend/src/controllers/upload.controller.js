export function downloadChunk(req, res) {
  return res.status(200).json({
    success: true,
    message: "Received Chunk",
  });
}
