import { Router } from "express";
import * as controller from "../controllers/college.controller.js";

const collegeRouter = Router();

collegeRouter.get("/", controller.getAllColleges);

export default collegeRouter;
