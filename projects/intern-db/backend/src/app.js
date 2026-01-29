import express from "express";
import router from "./routes/index.js";
import errorHandler from "./middlewares/error.middleware.js";
import cors from "cors";
import { createServer } from "http";
import { Server } from "socket.io";
import {
  setupTimeBroadcast,
  setupSubscribeTimeSocket,
} from "./sockets/time.socket.js";

const app = express();

app.use(express.json());

app.use(cors());
app.use("/", router);

app.use((req, res, next) => {
  res.status(404).json({
    success: false,
    error: "Route not found",
  });
});

app.use(errorHandler);

const httpServer = createServer(app);
const io = new Server(httpServer, { cors: { origin: "*" } });

setupTimeBroadcast(io);

io.on("connection", (socket) => {
  setupSubscribeTimeSocket(socket);
});

export default httpServer;
