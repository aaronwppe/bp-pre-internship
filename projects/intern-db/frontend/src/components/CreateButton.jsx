import { createIntern } from "../api/intern.api";
import { useState } from "react";
import { toast } from "react-toastify";

const BUTTON_MODE = {
  CREATE: "Create",
  SAVE: "Save",
};

export default function CreateButton({ internData, setInternData }) {
  const [buttonMode, setButtonMode] = useState(BUTTON_MODE.CREATE);

  const onCreateHandler = () => {
    setInternData((prev) => [
      ...prev,
      {
        id: "",
        name: "",
        githubUsername: "",
        stream: "",
        college: "",
      },
    ]);

    setButtonMode(BUTTON_MODE.SAVE);
  };

  const onSaveHandler = () => {
    let newIntern = internData.find((intern) => intern.id === "");
    console.log(newIntern);

    if (
      !newIntern.name ||
      !newIntern.githubUsername ||
      !newIntern.college ||
      !newIntern.stream
    ) {
      return;
    }

    createIntern(newIntern)
      .then((assignedId) => {
        setInternData((prevData) =>
          prevData.map((intern) => {
            return intern.id === "" ? { ...newIntern, id: assignedId } : intern;
          }),
        );

        setButtonMode(BUTTON_MODE.CREATE);
        toast.success(`Created new Intern Record for ${newIntern.name}.`);
      })
      .catch((err) => {
        console.log(err.message);
        toast.error(
          `Failed to create new Intern Record for ${newIntern.name}.`,
        );
      });
  };

  return (
    <button
      onClick={
        buttonMode === BUTTON_MODE.CREATE ? onCreateHandler : onSaveHandler
      }
    >
      {buttonMode}
    </button>
  );
}
