import { io } from "socket.io-client";

const BASE_URL = import.meta.env.VITE_API_BASE_URL;

export function openSocket(setServerTime) {
  const socket = io(BASE_URL);

  socket.on("time", setServerTime);

  socket.on("connect", () => {
    socket.emit("subscribe-time");
  });

  return socket;
}

export function closeSocket(socket) {
  socket.disconnect();
}
