import { getAllInterns, updateIntern } from "./api/intern.api";
import { getAllStreams } from "./api/stream.api";
import { getAllColleges } from "./api/college.api";
import InternTable from "./components/InternTable";
import CreateButton from "./components/CreateButton";
import DeleteButton from "./components/DeleteButton";
import { useEffect, useState } from "react";
import { Slide, ToastContainer, toast } from "react-toastify";
import { closeSocket, openSocket } from "./socket/time.socket";
import FileUploader from "./components/FileUploader";

function App() {
  const [internData, setInternData] = useState([]);
  const [rowSelection, setRowSelection] = useState([]);
  const [serverTime, setServerTime] = useState("");
  const [streams, setStreams] = useState([]);
  const [colleges, setColleges] = useState([]);

  useEffect(() => {
    const socket = openSocket(setServerTime);
    return () => closeSocket(socket);
  }, []);

  useEffect(() => {
    getAllInterns()
      .then(setInternData)
      .catch((err) => {
        toast.error("Failed to fetch Intern data.", {
          autoClose: false,
        });

        console.log(err);
      });

    getAllStreams()
      .then(setStreams)
      .catch((err) => {
        toast.error("Failed to fetch Stream options.", {
          autoClose: false,
        });

        console.log(err);
      });

    getAllColleges()
      .then(setColleges)
      .catch((err) => {
        toast.error("Failed to fetch College options.", {
          autoClose: false,
        });

        console.log(err);
      });
  }, []);

  const updateInternHandler = (updatedInternObject) => {
    if (updatedInternObject.id === "") {
      setInternData((prevData) =>
        prevData.map((intern) => {
          return intern.id === updatedInternObject.id
            ? updatedInternObject
            : intern;
        }),
      );
      return;
    }

    updateIntern(updatedInternObject)
      .then(() => {
        setInternData((prevData) =>
          prevData.map((intern) => {
            return intern.id === updatedInternObject.id
              ? updatedInternObject
              : intern;
          }),
        );

        toast.success(`Updated ${updatedInternObject.name}`);
      })
      .catch((err) => {
        console.log(err);
        toast.error(`Failed to update Intern ${updatedInternObject.name}`);
      });
  };

  return (
    <>
      <FileUploader />
      <CreateButton internData={internData} setInternData={setInternData} />
      <DeleteButton rowSelection={rowSelection} setInternData={setInternData} />
      <InternTable
        internData={internData}
        updateIntern={updateInternHandler}
        rowSelection={rowSelection}
        setRowSelection={setRowSelection}
        colleges={colleges}
        streams={streams}
      />
      <ToastContainer
        position="bottom-right"
        transition={Slide}
        draggable={false}
        hideProgressBar={true}
      />

      <p>{serverTime}</p>
    </>
  );
}

export default App;
