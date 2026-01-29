export default function LoadingToast({ fileName, progressPercentage }) {
  return (
    <div>
      <p>Uploading {fileName}</p>
      <div
        style={{
          marginTop: 5,
          height: 8,
          width: "100%",
          backgroundColor: "gray",
          borderRadius: 4,
        }}
      >
        <div
          style={{
            height: "100%",
            width: `${progressPercentage}%`,
            backgroundColor: "green",
            borderRadius: 4,
            transition: "width 0.2s",
          }}
        />
      </div>
    </div>
  );
}
