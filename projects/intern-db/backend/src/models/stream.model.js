import { EntityNotFound } from "../errors/index.js";

export default class Stream {
  static #streams = [];

  /**
   * @param {object} stream
   * @param {string} stream.name
   * @returns {Stream}
   */
  constructor({ name }) {
    this.name = name;
  }

  /**
   * @param {object} stream
   * @param {string} stream.name
   * @returns {Stream}
   */
  static insert({ name }) {
    try {
      return this.get(name);
    } catch (err) {
      if (!(err instanceof EntityNotFound)) {
        throw err;
      }
    }

    const stream = new Stream({ name });
    Object.freeze(stream);
    this.#streams.push(stream);
    return stream;
  }

  /**
   * @returns {Stream[]}
   */
  static getAll() {
    return [...this.#streams];
  }

  /**
   * @param {string} streamName
   * @returns {Stream}
   */
  static get(streamName) {
    const stream = this.#streams.find((s) => s.name === streamName);
    if (!stream) {
      throw new EntityNotFound("stream", "name", streamName);
    }

    return stream;
  }

  /**
   * @param {string} streamName
   * @returns {boolean}
   */
  static exists(streamName) {
    const stream = this.#streams.find((s) => s.name === streamName);
    return stream !== undefined;
  }
}
