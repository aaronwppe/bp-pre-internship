import { useEffect, useState } from "react";

export default function EditableCell({ getValue, table, row, column }) {
  const initialValue = getValue() ?? "";
  const [newValue, setNewValue] = useState(initialValue);

  const onBlur = () => {
    if (newValue === initialValue) {
      return;
    }

    table.options.meta.updateData(row.id, column.id, newValue);
  };

  useEffect(() => {
    setNewValue(initialValue);
  }, [initialValue]);

  return (
    <input
      value={newValue}
      onChange={(e) => setNewValue(e.target.value)}
      onBlur={onBlur}
    />
  );
}
