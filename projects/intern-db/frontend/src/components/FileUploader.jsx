import { useState } from "react";
import { uploadChunk } from "../api/upload.api";
import { toast } from "react-toastify";
import LoadingToast from "./LoadingToast";

export default function FileUploader() {
  const toastId = "loading-toast";
  const [file, setFile] = useState(null);
  // const [progressPercentage, setProgressPercentage] = useState(0);

  const onFileChangeHandler = (e) => {
    if (e.target.files) {
      setFile(e.target.files[0]);
    }
  };

  const onUploadHandler = () => {
    if (!file) {
      return;
    }

    const fileReader = new FileReader();

    const chunkSize = 1024 * 10; // 10 KB
    const chunksCount = Math.ceil(file.size / chunkSize);

    let chunkIndex = 0;

    fileReader.addEventListener("load", (e) => {
      uploadChunk(file.name, e.target.result, chunkIndex, chunksCount)
        .then(() => {
          chunkIndex++;
          if (chunkIndex === chunksCount) {
            toast.dismiss(toastId);
            toast.success(`Uploaded file '${file.name}' successfully.`);
            return;
          }

          let startByte = chunkIndex * chunkSize;

          fileReader.readAsArrayBuffer(
            file.slice(startByte, startByte + chunkSize),
          );

          const percent = Math.round(((chunkIndex + 1) * 100) / chunksCount);

          toast.update(toastId, {
            render: (
              <LoadingToast fileName={file.name} progressPercentage={percent} />
            ),
          });
        })
        .catch((err) => {
          console.log(err);
        });
    });

    toast.info(<LoadingToast fileName={file.name} progressPercentage={0} />, {
      closeButton: false,
      autoClose: false,
      toastId: toastId,
    });
    fileReader.readAsArrayBuffer(file.slice(0, chunkSize));
  };

  return (
    <div>
      <input type="file" onChange={onFileChangeHandler} />
      {file && <button onClick={onUploadHandler}>Upload</button>}
    </div>
  );
}

// import { useState } from "react";

// const STATUS = {
//   IDLE: "idle",
//   UPLOADING: "uploading",
//   SUCCESS: "success",
//   ERROR: "error",
// };

// export default function FileUploader() {
//   const [file, setFile] = useState(null);
//   const [status, setStatus] = useState(STATUS.IDLE);

//   const onFileChangeHandler = (event) => {
//     if (event.target.files) {
//       setFile(event.target.files[0]);
//     }
//   };

//   const onUploadHandler = () => {
//     if (!file) {
//       return;
//     }

//     setStatus(STATUS.UPLOADING);

//     const formData = new FormData();
//     formData.append('file', file);

//     try {
//       await fetch("/upload")
//     }
//   }

//   return (
//     <div>
//       {file && (
//         <div>
//           <p>Name: {file.name}</p>
//           <p>Size: {(file.size / 1024).toFixed(2)} KB</p>
//         </div>
//       )}
//       <input type="file" onChange={onFileChangeHandler} />
//       {file && status !== STATUS.UPLOADING && <button>Upload</button>}
//     </div>
//   );
// }
