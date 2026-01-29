import { deleteInterns } from "../api/intern.api";
import { toast } from "react-toastify";

export default function DeleteButton({ setInternData, rowSelection }) {
  const onDeleteHandler = () => {
    const selectedIds = Object.keys(rowSelection);

    if (selectedIds.length === 0) {
      const toastId = "empty-delete";
      const toastduration = 2000;

      toast.isActive(toastId)
        ? toast.update(toastId, { autoClose: toastduration })
        : toast.warning("No Intern selected.", {
            toastId: toastId,
            autoClose: 2000,
          });

      return;
    }

    deleteInterns(selectedIds)
      .then(() => {
        setInternData((prevData) =>
          prevData.filter((intern) => {
            return selectedIds.find((selectedId) => selectedId === intern.id)
              ? false
              : true;
          }),
        );

        toast.success(`Delete successful.`);
      })
      .catch((err) => {
        console.log(err.message);
        toast.error("Delete operation failed.");
      });
  };

  return <button onClick={onDeleteHandler}>Delete</button>;
}
