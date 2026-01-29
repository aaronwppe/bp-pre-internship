import { Router } from "express";
import * as controller from "../controllers/intern.controller.js";
import {
  internBodyValidator,
  batchDeleteValidator,
} from "../middlewares/validator.middleware.js";

const internRouter = Router();

internRouter.get("/", controller.getAllInterns);

internRouter.post("/", internBodyValidator, controller.createNewIntern);

internRouter.delete(
  "/batch",
  batchDeleteValidator,
  controller.batchDeleteInterns,
);

internRouter.put("/:internId", internBodyValidator, controller.updateIntern);

internRouter.delete("/:internId", controller.deleteIntern);

export default internRouter;
