const BASE_UPLOAD_URL = new URL("upload/", import.meta.env.VITE_API_BASE_URL);

/**
 * @param {string} fileName
 * @param {Blob} data
 * @param {number} index
 * @param {number} totalChunks
 */
export async function uploadChunk(fileName, data, index, totalChunks) {
  return await fetch(BASE_UPLOAD_URL, {
    method: "POST",
    headers: {
      "content-type": "application/octet-stream",
      "X-file-name": fileName,
      "X-chunk-index": index,
      "X-total-chunks": totalChunks,
    },
    body: data,
  });
}
