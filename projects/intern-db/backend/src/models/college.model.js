import { EntityNotFound } from "../errors/index.js";

export default class College {
  static #colleges = [];

  /**
   * @param {object} college
   * @param {string} college.name
   * @returns {College}
   */
  constructor({ name }) {
    this.name = name;
  }

  /**
   * @param {object} college
   * @param {string} name
   * @returns {College}
   */
  static insert({ name }) {
    const college = new College({ name });
    Object.freeze(college);
    this.#colleges.push(college);
    return college;
  }

  /**
   * @returns {College[]}
   */
  static getAll() {
    return [...this.#colleges];
  }

  /**
   * @param {string} collegeName
   * @returns {College}
   */
  static get(collegeName) {
    const college = this.#colleges.find((s) => s.name === collegeName);
    if (!college) {
      throw new EntityNotFound("college", "name", collegeName);
    }

    return college;
  }

  /**
   * @param {string} collegeName
   * @returns {boolean}
   */
  static exists(collegeName) {
    const college = this.#colleges.find((s) => s.name === collegeName);

    return college !== undefined;
  }
}
