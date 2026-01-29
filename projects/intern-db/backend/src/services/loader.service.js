import { parse } from "csv-parse";
import { createReadStream } from "fs";
import Intern from "../models/intern.model.js";
import College from "../models/college.model.js";
import Stream from "../models/stream.model.js";

/**
 *
 * @param {string} csvFilePath
 * @returns {void}
 */
function loadAllStaticModels(csvFilePath) {
  return new Promise((resolve) => {
    const parser = parse({ columns: true, bom: true });

    parser.on("readable", () => {
      let internJson;

      while ((internJson = parser.read()) !== null) {
        internJson.college = College.exists(internJson.college)
          ? College.get(internJson.college)
          : College.insert({ name: internJson.college });

        internJson.stream = Stream.exists(internJson.stream)
          ? Stream.get(internJson.stream)
          : Stream.insert({ name: internJson.stream });

        Intern.insert(internJson);
      }
    });

    parser.on("end", () => {
      resolve();
    });

    createReadStream(csvFilePath, { encoding: "utf-8" }).pipe(parser);
  });
}

export default loadAllStaticModels;
