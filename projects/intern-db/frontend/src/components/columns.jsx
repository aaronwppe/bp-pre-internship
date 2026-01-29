import DropdownCell from "./DropdownCell";
import EditableCell from "./EditableCell";
import RowCheckbox from "./RowCheckBox";

export default function getColumns(streams, colleges) {
  return [
    {
      id: "select-column",
      header: ({ table }) => (
        <RowCheckbox
          checked={table.getIsAllRowsSelected()}
          indeterminate={table.getIsSomeRowsSelected()}
          onChange={table.getToggleAllRowsSelectedHandler()}
        />
      ),
      cell: ({ row }) => (
        <RowCheckbox
          checked={row.getIsSelected()}
          onChange={row.getToggleSelectedHandler()}
        />
      ),
    },
    {
      accessorKey: "name",
      header: "Name",
      cell: EditableCell,
    },
    {
      accessorKey: "githubUsername",
      header: "Github",
      cell: EditableCell,
    },
    {
      accessorKey: "stream",
      header: "Stream",
      cell: DropdownCell,
      meta: {
        options: streams,
      },
    },
    {
      accessorKey: "college",
      header: "College",
      cell: DropdownCell,
      meta: {
        options: colleges,
      },
    },
  ];
}
