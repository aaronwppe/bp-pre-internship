import { EntityNotFound } from "../errors/index.js";
import { College, Stream, Intern } from "../models/index.js";

export function getAllInterns(req, res) {
  const interns = Intern.getAll().map((intern) => {
    return {
      ...intern,
      college: intern.college.name,
      stream: intern.stream.name,
    };
  });

  return res.status(200).json({
    success: true,
    data: { interns },
    message: "Fetched all interns.",
  });
}

export function createNewIntern(req, res) {
  let { name, githubUsername, stream, college } = req.body;

  const intern = Intern.insert({
    name,
    githubUsername,
    stream: Stream.get(stream),
    college: College.get(college),
  });

  return res.status(201).json({
    success: true,
    data: {
      internId: intern.id,
    },
    message: "Created new intern.",
  });
}

export function updateIntern(req, res) {
  const intern = new Intern({
    id: req.params.internId,
    name: req.body.name,
    githubUsername: req.body.githubUsername,
    stream: Stream.get(req.body.stream),
    college: College.get(req.body.college),
  });

  Intern.update(intern);

  return res.status(200).json({
    success: true,
    data: {},
    message: "Updated intern.",
  });
}

export function deleteIntern(req, res) {
  const internId = req.params.internId;

  Intern.delete(internId);

  return res.status(200).json({
    success: true,
    data: {},
    message: "Deleted intern.",
  });
}

export function batchDeleteInterns(req, res) {
  const internIds = req.body.internIds;

  let failed = [];

  for (let internId of internIds) {
    try {
      Intern.delete(internId);
    } catch (err) {
      if (!(err instanceof EntityNotFound)) {
        throw err;
      }

      failed.push({ id: internId, error: err.message });
    }
  }

  let statusCode = 200;
  let responseJson = {
    success: true,
    data: { failed },
    message: "Deleted all interns.",
  };

  if (failed.length === internIds.length) {
    statusCode = 404;
    responseJson.success = false;
    responseJson.message = "Failed to delete all interns.";
  } else if (failed.length > 0) {
    statusCode = 207;
    responseJson.success = false;
    responseJson.message = "Partially deleted interns.";
  }

  return res.status(statusCode).json(responseJson);
}
