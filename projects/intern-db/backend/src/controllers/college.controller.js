import { College } from "../models/index.js";

export function getAllColleges(req, res) {
  const colleges = College.getAll().map((college) => college.name);

  return res.status(200).json({
    success: true,
    data: { colleges },
    message: "Fetched all colleges.",
  });
}
