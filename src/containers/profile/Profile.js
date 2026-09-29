import React, {useState, useEffect} from "react";
import {openSource} from "../../portfolio";
import GithubProfileCard from "../../components/githubProfileCard/GithubProfileCard";
import Contact from "../contact/Contact";

export default function Profile() {
  const [prof, setrepo] = useState(null);

  useEffect(() => {
    if (openSource.showGithubProfile === "true") {
      fetch("/profile.json")
        .then(result => {
          if (result.ok) {
            return result.json();
          }
        })
        .then(response => {
          if (response && response.data && response.data.user) {
            const user = response.data.user;
            user.bio = "Full Stack Developer";
            setrepo(user);
          }
        })
        .catch(function (error) {
          console.error(error);
          setrepo({
            name: "Damini Raj",
            bio: "Full Stack Developer",
            avatarUrl: "/damini.png",
            location: "Gurgaon, India"
          });
        });
    }
  }, []);

  if (openSource.showGithubProfile === "true" && prof) {
    return <GithubProfileCard prof={prof} key={prof.id || "profile"} />;
  } else {
    return <Contact />;
  }
}
