import { EntityNotFound, DuplicateField } from "../errors/index.js";
import { College, Stream } from "./index.js";

export default class Intern {
  static #interns = new Map();

  /**
   * @param {object} intern
   * @param {string} intern.id
   * @param {string} intern.name
   * @param {string} intern.githubUsername
   * @param {Stream} intern.stream
   * @param {College} intern.college
   * @returns {Intern}
   */
  constructor({ id, name, githubUsername, stream, college }) {
    this.id = id;
    this.name = name;
    this.githubUsername = githubUsername;
    this.stream = stream;
    this.college = college;
  }

  /**
   * @param {object} intern
   * @param {string} [intern.id]
   * @param {string} intern.name
   * @param {string} intern.githubUsername
   * @param {Stream} intern.stream
   * @param {College} intern.college
   * @returns {Intern}
   */
  static insert({ id = null, name, githubUsername, stream, college }) {
    if (id && this.#interns.has(id)) {
      throw new DuplicateField("id", id);
    }

    this.#interns.forEach((intern, _) => {
      if (intern.githubUsername === githubUsername) {
        throw new DuplicateField("githubUsername", githubUsername);
      }
    });

    const intern = new Intern({
      id: id ?? crypto.randomUUID(),
      name,
      githubUsername,
      stream,
      college,
    });

    Object.freeze(intern);
    this.#interns.set(intern.id, intern);

    return intern;
  }

  /**
   * @returns {Intern[]}
   */
  static getAll() {
    return [...this.#interns.values()];
  }

  /**
   *
   * @param {Intern} newIntern
   * @returns {void}
   */
  static update(newIntern) {
    if (!this.#interns.has(newIntern.id)) {
      throw new EntityNotFound("intern", "id", newIntern.id);
    }

    this.#interns.forEach((intern, id) => {
      if (
        intern.githubUsername === newIntern.githubUsername &&
        id !== newIntern.id
      ) {
        throw new DuplicateField("githubUsername", newIntern.githubUsername);
      }
    });

    this.#interns.set(newIntern.id, newIntern);
  }

  /**
   *
   * @param {string} internId
   * @returns {void}
   */
  static delete(internId) {
    const deleteStatus = this.#interns.delete(internId);

    if (deleteStatus === false) {
      throw new EntityNotFound("intern", "id", internId);
    }
  }
}
