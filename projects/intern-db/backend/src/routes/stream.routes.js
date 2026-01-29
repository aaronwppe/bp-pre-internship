import { Router } from "express";
import * as controller from "../controllers/stream.controller.js";

const streamRouter = Router();

streamRouter.get("/", controller.getAllStreams);

export default streamRouter;
