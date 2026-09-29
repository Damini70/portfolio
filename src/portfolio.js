/* Change this file to get your personal Portfolio */

// To change portfolio colors globally go to the  _globalColor.scss file

import emoji from "react-easy-emoji";
import splashAnimation from "./assets/lottie/splashAnimation";

// Splash Screen

const splashScreen = {
  enabled: true, // set false to disable splash screen
  animation: splashAnimation,
  duration: 2000 // Set animation duration as per your animation
};

// Summary And Greeting Section

const illustration = {
  animated: true // Set to false to use static SVG
};

const greeting = {
  username: "Damini Raj",
  title: "Hi all, I'm Damini",
  subTitle: emoji(
    "A passionate MERN Stack Developer & Full Stack Developer with AI 🚀 with 4 years of experience building responsive, scalable, and high-performance web applications using React.js, Next.js, Node.js, TypeScript, Tailwind CSS, and modern AI/LLM integrations."
  ),
  resumeLink: "/Damini_Node_React_4.pdf", // Set to empty to hide the button
  displayGreeting: true // Set false to hide this section, defaults to true
};

// Social Media Links

const socialMediaLinks = {
  github: "https://github.com/Damini70",
  linkedin: "https://www.linkedin.com/in/damini-raj",
  gmail: "daminiraj70@gmail.com",
  gitlab: "",
  facebook: "",
  medium: "",
  stackoverflow: "",
  instagram: "",
  twitter: "",
  kaggle: "",
  display: true // Set true to display this section, defaults to false
};

// Skills Section

const skillsSection = {
  title: "What I do",
  subTitle:
    "MERN STACK DEVELOPER | FULL STACK DEVELOPER WITH AI BUILDING PRODUCTION SYSTEMS",
  skills: [
    emoji(
      "⚡ Building responsive, scalable, and high-performance web applications using React.js, Next.js, TypeScript, and Generative AI / LLMs"
    ),
    emoji(
      "⚡ Crafting modern UI/UX architectures with Tailwind CSS, Material UI, Bootstrap, and shadcn/ui"
    ),
    emoji(
      "⚡ Developing backend APIs, microservices, and databases with Python, Node.js, Express.js, MongoDB (Aggregation Framework), and JWT Authentication"
    ),
    emoji(
      "⚡ Implementing real-time communication via WebSocket & SSE, with centralized Redux Toolkit & React Query state management"
    )
  ],

  /* Make Sure to include correct Font Awesome Classname to view your icon
https://fontawesome.com/icons?d=gallery */

  softwareSkills: [
    {
      skillName: "React.js",
      fontAwesomeClassname: "fab fa-react"
    },
    {
      skillName: "Next.js",
      fontAwesomeClassname: "fas fa-laptop-code"
    },
    {
      skillName: "Node.js",
      fontAwesomeClassname: "fab fa-node"
    },
    {
      skillName: "Python",
      fontAwesomeClassname: "fab fa-python"
    },
    {
      skillName: "JavaScript",
      fontAwesomeClassname: "fab fa-js"
    },
    {
      skillName: "TypeScript",
      fontAwesomeClassname: "fas fa-code"
    },
    {
      skillName: "HTML5",
      fontAwesomeClassname: "fab fa-html5"
    },
    {
      skillName: "CSS3",
      fontAwesomeClassname: "fab fa-css3-alt"
    },
    {
      skillName: "Tailwind / SASS",
      fontAwesomeClassname: "fab fa-sass"
    },
    {
      skillName: "Bootstrap",
      fontAwesomeClassname: "fab fa-bootstrap"
    },
    {
      skillName: "MongoDB / Database",
      fontAwesomeClassname: "fas fa-database"
    },
    {
      skillName: "Git",
      fontAwesomeClassname: "fab fa-git-alt"
    },
    {
      skillName: "AWS",
      fontAwesomeClassname: "fab fa-aws"
    },
    {
      skillName: "Docker",
      fontAwesomeClassname: "fab fa-docker"
    },
    {
      skillName: "NPM",
      fontAwesomeClassname: "fab fa-npm"
    },
    {
      skillName: "AI / LLMs",
      fontAwesomeClassname: "fas fa-robot"
    }
  ],
  categorySkills: [
    {
      category: "Languages & Frameworks",
      skills: [
        "Python",
        "React.js",
        "Next.js",
        "Node.js",
        "Express.js",
        "TypeScript",
        "JavaScript (ES6+)"
      ]
    },
    {
      category: "UI & Modern Styling",
      skills: [
        "Tailwind CSS",
        "shadcn/ui",
        "Material UI",
        "Bootstrap",
        "Responsive Design",
        "SASS / CSS3"
      ]
    },
    {
      category: "Backend & Databases",
      skills: [
        "MongoDB (Aggregation)",
        "RESTful APIs",
        "Mongoose",
        "JWT Authentication",
        "Redux Toolkit",
        "TanStack Query"
      ]
    },
    {
      category: "Real-Time, AI & Cloud",
      skills: [
        "Generative AI / LLMs",
        "Prompt Engineering",
        "WebSocket",
        "SSE",
        "AWS (EC2, S3)",
        "Docker",
        "Git & CI/CD",
        "Jest"
      ]
    }
  ],
  display: true // Set false to hide this section, defaults to true
};

// Education Section

const educationInfo = {
  display: true, // Set false to hide this section, defaults to true
  schools: [
    {
      schoolName: "Indira Gandhi National Open University (IGNOU)",
      logo: require("./assets/images/ignouLogo.png"),
      subHeader: "Master of Computer Applications (MCA) — Pursuing",
      duration: "Present",
      desc: "Pursuing Master of Computer Applications (MCA) focusing on Advanced Software Engineering, Cloud Computing, Database Architectures, and Full Stack Systems.",
      descBullets: [
        "Advanced specialization in Enterprise Application Design, Data Structures, and Scalable Backend Systems.",
        "Strengthening core computer science foundations alongside active production software engineering."
      ]
    },
    {
      schoolName: "Aryabhatta Knowledge University",
      logo: require("./assets/images/akuLogo.png"),
      subHeader: "Bachelor of Technology (B.Tech)",
      duration: "2016 – 2020",
      desc: "Completed Bachelor of Technology with hands-on coursework in computer science, software development, data structures, algorithms, and system design.",
      descBullets: [
        "Strong foundation in Data Structures, Algorithms, Object-Oriented Programming, and Web Engineering.",
        "Demonstrated technical excellence with focus on scalable web technologies."
      ]
    }
  ]
};

// Your top 3 proficient stacks/tech experience

const techStack = {
  viewSkillBars: true, //Set it to true to show Proficiency Section
  experience: [
    {
      Stack: "Full Stack (MERN / React.js / Node.js / Next.js)",
      progressPercentage: "95%"
    },
    {
      Stack: "Frontend & UI (TypeScript / Tailwind CSS / shadcn/ui)",
      progressPercentage: "90%"
    },
    {
      Stack: "Backend & DB (Node.js / Express.js / MongoDB / Python)",
      progressPercentage: "85%"
    },
    {
      Stack: "AI, Python & Real-time (Python / LLMs / WebSocket / SSE)",
      progressPercentage: "80%"
    }
  ],
  displayCodersrank: false
};

// Work experience section

const workExperiences = {
  display: true, //Set it to true to show workExperiences Section
  experience: [
    {
      role: "Software Engineer",
      company: "Techugo",
      companylogo: require("./assets/images/techugoLogo.png"),
      date: "Sep 2025 – Present",
      desc: "Led frontend development of responsive and scalable web applications using React.js, Next.js, TypeScript, Tailwind CSS, SSE, and WebSocket.",
      descBullets: [
        "Developed the Autaras User Portal, Service Provider Portal, and Admin Panel for a vehicle mobility platform supporting car wash, car rental, and transportation services.",
        "Designed and built REST APIs (Node.js, Express.js) for Autaras service workflows including transportation booking, car rental, and car wash requests, covering booking creation, provider assignment, and status updates.",
        "Built reusable frontend components and scalable application logic to improve maintainability and development efficiency.",
        "Integrated REST APIs and implemented frontend state management for complex application workflows.",
        "Developed and optimized Unigoal, a career counselling platform, improving frontend performance by 40%.",
        "Improved responsive behavior and cross-browser compatibility across web applications.",
        "Collaborated with clients, designers, backend developers, and stakeholders to convert business requirements into production-ready features."
      ]
    },
    {
      role: "MERN Stack Developer",
      company: "Indiana Commerce",
      companylogo: require("./assets/images/indianaLogo.png"),
      date: "Dec 2023 – Jul 2025",
      desc: "Developed scalable and responsive web applications using React.js, Redux, JavaScript, Tailwind CSS, React Hook Form, React Router, Node.js, Express.js, and MongoDB.",
      descBullets: [
        "Integrated 10+ REST APIs to support application workflows and dynamic user experiences.",
        "Implemented multilingual functionality supporting 5+ languages using react-i18next.",
        "Developed secure authentication flows and frontend workflows for application users using Node.js, Express.js, and MongoDB.",
        "Designed REST endpoints and MongoDB aggregation queries (Node.js, Express.js) to serve real-time dashboard data.",
        "Built interactive dashboards with live data using React.js, Redux, Node.js, Fusion Charts, and AM Charts.",
        "UCAAS: Built responsive interfaces using React.js, Redux, WebSocket, and Tailwind CSS; implemented secure authentication and real-time messaging functionality.",
        "GOTRUST: Developed DSR features using React.js, Redux, shadcn/ui, and REST APIs, improving request processing efficiency by 30%."
      ]
    },
    {
      role: "Junior Developer",
      company: "Iotas Solutions Pvt. Ltd.",
      companylogo: require("./assets/images/iotasLogo.png"),
      date: "Jan 2023 – Nov 2023",
      desc: "Provided technical support, UI troubleshooting, and frontend performance optimization for websites and IT systems for 50+ clients.",
      descBullets: [
        "Provided technical support and product assistance for websites and IT systems for 50+ clients.",
        "Performed UI troubleshooting, performance testing, and code reviews to identify and resolve frontend issues for CivilTrack.",
        "Improved application load speed by 25% through frontend performance optimization.",
        "Collaborated with clients to understand requirements, resolve technical issues, and improve application reliability through rigorous testing and frontend performance optimization."
      ]
    },
    {
      role: "Full Stack Developer Intern",
      company: "Newton School",
      companylogo: require("./assets/images/newtonLogo.png"),
      date: "Feb 2022 – Dec 2022",
      desc: "Built full-stack web applications and responsive user interfaces with modern web standards.",
      descBullets: [
        "Developed responsive web interfaces using React.js, JavaScript, HTML5, and CSS3.",
        "Built and deployed REST API services handling user data with MongoDB for application data end-to-end from schema design to deployment on Vercel/Render.",
        "Worked with MongoDB and SQL for application data management.",
        "Deployed applications using Vercel and Render."
      ]
    }
  ]
};

/* Your Open Source Section to View Your Github Pinned Projects
To know how to get github key look at readme.md */

const openSource = {
  showGithubProfile: "true", // Set true or false to show Contact profile using Github, defaults to true
  display: true // Set false to hide this section, defaults to true
};

// Some big projects you have worked on

const bigProjects = {
  title: "Featured Projects",
  subtitle: "PRODUCTION PLATFORMS & HIGH-IMPACT WEB APPLICATIONS",
  projects: [
    {
      image: require("./assets/images/autarasLogo.png"),
      projectName: "Autaras — Vehicle Mobility Platform",
      projectDesc:
        "Developed and maintained User Portal, Service Provider Portal, and Admin Panel for a vehicle mobility platform supporting car wash, car rental, and transportation services. Built responsive and reusable UI components using React.js, Next.js, TypeScript, and Tailwind CSS. Architected client-side data-fetching layer using TanStack Query and Axios, reducing redundant network requests by 35%. Implemented real-time updates using SSE and WebSocket. Owned the file-storage system end-to-end: designed the upload/retrieval workflow, integrated Amazon S3 for secure scalable storage, and built the frontend upload UI.",
      footerLink: [
        {
          name: "React.js",
          url: "https://github.com/Damini70"
        },
        {
          name: "Next.js",
          url: "https://github.com/Damini70"
        },
        {
          name: "TypeScript",
          url: "https://github.com/Damini70"
        },
        {
          name: "Node.js & Express",
          url: "https://github.com/Damini70"
        },
        {
          name: "Tailwind CSS",
          url: "https://github.com/Damini70"
        },
        {
          name: "SSE & WebSocket",
          url: "https://github.com/Damini70"
        },
        {
          name: "Amazon S3",
          url: "https://github.com/Damini70"
        }
      ]
    },
    {
      image: require("./assets/images/unigoalLogo.png"),
      projectName: "Unigoal — Career Counselling Platform",
      projectDesc:
        "Developed responsive and user-friendly frontend interfaces for a career counselling platform using React.js and JavaScript. Integrated REST APIs to manage dynamic career counselling workflows and application data. Reduced page load time by 40% and improved LCP by implementing code splitting, dynamic imports, and memoized selectors in React. Enhanced responsive behavior and cross-browser compatibility.",
      footerLink: [
        {
          name: "React.js",
          url: "https://github.com/Damini70"
        },
        {
          name: "JavaScript",
          url: "https://github.com/Damini70"
        },
        {
          name: "Tailwind CSS",
          url: "https://github.com/Damini70"
        },
        {
          name: "REST APIs",
          url: "https://github.com/Damini70"
        }
      ]
    },
    {
      image: require("./assets/images/ucaasLogo.png"),
      projectName: "UCAAS — Communication & Messaging Platform",
      projectDesc:
        "Developed responsive and scalable frontend interfaces using React.js, Redux, and Tailwind CSS. Implemented real-time messaging and communication features using WebSocket for seamless user-to-user interactions. Designed and implemented JWT-based authentication and session management on the backend (Node.js, Express.js, MongoDB), including token refresh and role-based access control, then integrated it across the frontend application.",
      footerLink: [
        {
          name: "React.js",
          url: "https://github.com/Damini70"
        },
        {
          name: "Redux",
          url: "https://github.com/Damini70"
        },
        {
          name: "WebSocket",
          url: "https://github.com/Damini70"
        },
        {
          name: "Node.js & Express",
          url: "https://github.com/Damini70"
        },
        {
          name: "MongoDB",
          url: "https://github.com/Damini70"
        },
        {
          name: "JWT Auth",
          url: "https://github.com/Damini70"
        }
      ]
    },
    {
      image: require("./assets/images/gotrustLogo.png"),
      projectName: "GOTRUST — DSR & Request Management Platform",
      projectDesc:
        "Developed DSR-related application features using React.js, Redux, and shadcn/ui with a focus on responsive and reusable interfaces. Integrated REST APIs to support dynamic request management and centralized Redux state management, improving request processing efficiency by 30%. Built reusable UI components using shadcn/ui to maintain consistency and configured CI/CD pipelines to streamline application releases.",
      footerLink: [
        {
          name: "React.js",
          url: "https://github.com/Damini70"
        },
        {
          name: "Redux",
          url: "https://github.com/Damini70"
        },
        {
          name: "shadcn/ui",
          url: "https://github.com/Damini70"
        },
        {
          name: "REST APIs",
          url: "https://github.com/Damini70"
        },
        {
          name: "CI/CD",
          url: "https://github.com/Damini70"
        }
      ]
    }
  ],
  display: true // Set false to hide this section, defaults to true
};

// Achievement Section
// Include certificates, talks etc

const achievementSection = {
  title: emoji("Achievements & Certifications 🏆"),
  subtitle:
    "Data Structures, Algorithms, Competitive Programming & Problem Solving",

  achievementsCards: [
    {
      title: "LeetCode: 250+ Solved",
      subtitle:
        "Solved 250+ Data Structures and Algorithms problems on LeetCode covering arrays, strings, hashing, recursion, two pointers, dynamic programming, and trees.",
      image: require("./assets/images/leetcodeLogo.png"),
      imageAlt: "LeetCode Logo",
      footerLink: [
        {
          name: "LeetCode Profile",
          url: "https://leetcode.com/progress"
        }
      ]
    }
  ],
  display: true // Set false to hide this section, defaults to true
};

// Blogs Section

const blogSection = {
  title: "Blogs",
  subtitle: "",
  displayMediumBlogs: "false",
  blogs: [],
  display: false // Set false to hide this section, defaults to true
};

// Talks Sections

const talkSection = {
  title: "TALKS",
  subtitle: "",
  talks: [],
  display: false // Set false to hide this section, defaults to true
};

// Podcast Section

const podcastSection = {
  title: "Podcast",
  subtitle: "",
  podcast: [],
  display: false // Set false to hide this section, defaults to true
};

// Resume Section
const resumeSection = {
  title: "Resume",
  subtitle: "Feel free to download my resume",
  display: true // Set false to hide this section, defaults to true
};

const contactInfo = {
  title: emoji("Contact Me ☎️"),
  subtitle:
    "Discuss a project or looking for an immediate joiner? My Inbox is open for all.",
  number: "+91 7488128085",
  email_address: "daminiraj70@gmail.com"
};

// Twitter Section

const twitterDetails = {
  userName: "",
  display: false // Set true to display this section, defaults to false
};

const isHireable = true; // Set false if you are not looking for a job. Also isHireable will be display as Open for opportunities: Yes/No in the GitHub footer

export {
  illustration,
  greeting,
  socialMediaLinks,
  splashScreen,
  skillsSection,
  educationInfo,
  techStack,
  workExperiences,
  openSource,
  bigProjects,
  achievementSection,
  blogSection,
  talkSection,
  podcastSection,
  contactInfo,
  twitterDetails,
  isHireable,
  resumeSection
};
