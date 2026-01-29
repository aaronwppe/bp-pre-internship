const ROOM_NAME = "time";

export function setupSubscribeTimeSocket(socket) {
  socket.on("subscribe-time", () => {
    socket.join(ROOM_NAME);
  });
}

export function setupTimeBroadcast(io) {
  const intervalId = setInterval(() => {
    const date = new Date();
    io.to(ROOM_NAME).emit("time", date.toLocaleTimeString());
  }, 1000);

  io.on("close", () => clearInterval(intervalId));
}
