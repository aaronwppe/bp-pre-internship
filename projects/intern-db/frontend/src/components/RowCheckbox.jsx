import { useEffect, useRef } from "react";

export default function RowCheckbox({ checked, indeterminate, onChange }) {
  const ref = useRef();

  useEffect(() => {
    if (typeof indeterminate === "boolean") {
      ref.current.indeterminate = !checked && indeterminate;
    }
  }, [checked, indeterminate]);

  return (
    <input type="checkbox" checked={checked} onChange={onChange} ref={ref} />
  );
}
