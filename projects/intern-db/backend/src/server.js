import httpServer from "./app.js";
import College from "./models/college.model.js";
import loadAllStaticModels from "./services/loader.service.js";

const PORT = 3000;
const INTERN_CSV_FILE_PATH = "./data/intern.csv";

await loadAllStaticModels(INTERN_CSV_FILE_PATH);

httpServer.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT} ...`);
});
