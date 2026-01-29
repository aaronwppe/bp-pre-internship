import { Router } from "express";
import { downloadChunk } from "../controllers/upload.controller.js";

const uploadRouter = Router();

uploadRouter.post("/", downloadChunk);

export default uploadRouter;
