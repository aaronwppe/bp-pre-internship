import { useEffect, useState } from "react";

export default function DropdownCell({ getValue, table, row, column }) {
  const initialValue = getValue();
  const [selectedValue, setSelectedValue] = useState(initialValue);

  useEffect(() => {
    setSelectedValue(initialValue);
  }, [initialValue]);

  const onOptionChangeHandler = (value) => {
    setSelectedValue(value);
    table.options.meta.updateData(row.id, column.id, value);
  };

  return (
    <select
      value={selectedValue ?? ""}
      onChange={(event) => onOptionChangeHandler(event.target.value)}
    >
      <option key="" value="" disabled></option>
      {column.columnDef.meta.options.map((opt) => (
        <option key={opt} value={opt}>
          {opt}
        </option>
      ))}
    </select>
  );
}
