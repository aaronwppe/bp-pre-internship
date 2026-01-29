import { Router } from "express";
import internRouter from "./intern.routes.js";
import uploadRouter from "./upload.routes.js";
import collegeRouter from "./college.routes.js";
import streamRouter from "./stream.routes.js";

const router = Router();

router.use("/intern", internRouter);
router.use("/upload", uploadRouter);
router.use("/college", collegeRouter);
router.use("/stream", streamRouter);

export default router;
