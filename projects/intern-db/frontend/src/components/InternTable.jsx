import getColumns from "./columns.jsx";
import {
  flexRender,
  getCoreRowModel,
  getSortedRowModel,
  useReactTable,
} from "@tanstack/react-table";
import { useMemo, useState } from "react";

export default function InternTable({
  internData,
  updateIntern,
  rowSelection,
  setRowSelection,
  streams,
  colleges,
}) {
  const memoizedColumns = useMemo(() => getColumns(streams, colleges));

  const [sorting, setSorting] = useState([]);

  const updateDataHandler = (rowId, columnId, value) => {
    const intern = internData.find((intern) => rowId === intern.id);

    if (!intern) {
      throw new Error("Table is in an invalid state.");
    }

    updateIntern({
      ...intern,
      [columnId]: value,
    });
  };

  const table = useReactTable({
    columns: memoizedColumns,
    data: internData,
    getRowId: (intern) => intern.id,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel(),
    state: {
      sorting: sorting,
      rowSelection: rowSelection,
    },
    onSortingChange: setSorting,
    onRowSelectionChange: setRowSelection,
    meta: {
      updateData: updateDataHandler,
    },
  });

  return (
    <table>
      <thead>
        {table.getHeaderGroups().map((headerGroup) => (
          <tr key={headerGroup.id}>
            {headerGroup.headers.map((header) => (
              <th
                key={header.id}
                colSpan={header.colSpan}
                onClick={header.column.getToggleSortingHandler()}
              >
                {flexRender(
                  header.column.columnDef.header,
                  header.getContext(),
                )}
                {{ asc: "-UP", desc: "-DOWN" }[header.column.getIsSorted()]}
              </th>
            ))}
          </tr>
        ))}
      </thead>

      <tbody>
        {table.getRowModel().rows.map((row) => (
          <tr key={row.id}>
            {row.getVisibleCells().map((cell) => (
              <td key={cell.id} colSpan={cell.colSpan}>
                {flexRender(cell.column.columnDef.cell, cell.getContext())}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}
