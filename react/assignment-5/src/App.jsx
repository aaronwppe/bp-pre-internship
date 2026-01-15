import { useState, useEffect } from 'react'
import './App.css';
import { ReactElement } from "react";

/**
 * Loads user data from external api. Displays a random user's name and email after data is fully fetched. 
 *
 * @returns {ReactElement}
 */
function App() {
  const usersUrl = "https://jsonplaceholder.typicode.com/users";

  const [user, setUser] = useState({});

  useEffect(() => {
    async function fetchUsers() {
      const response = await fetch(usersUrl);
      const usersJson = await response.json();

      const randomIndex = Math.floor(Math.random() * usersJson.length);
      const randomUser = usersJson[randomIndex];

      setUser({
        name: randomUser.name,
        email: randomUser.email,
      });
    }

    fetchUsers();

  }, []);

  return (
    <>
      <h2>Name: {user.name || "loading..."}</h2>
      <h2>Email: {user.email || "loading..."}</h2>
    </>
  )
}

export default App;
