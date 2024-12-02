import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-icons/font/bootstrap-icons.css';
import { CssVarsProvider, extendTheme } from '@mui/joy/styles'; 
import { ThemeProvider, createTheme } from '@mui/material/styles'; 
import { grey } from '@mui/material/colors';
import './App.css';


declare global {
  interface Window {
    googleTranslateElementInit: () => void;
  }
}
const checkbox = document.getElementById("checkbox");
if (checkbox) {
  checkbox.addEventListener("change", () => {
    document.body.classList.toggle("dark");
  });
}

function App() {
  const joyTheme = extendTheme({
    colorSchemes: {
      light: {
        palette: {
          background: {
            body: grey[900], 
          },
          text: {
            primary: grey[800], 
          },
        },
      },
    },
  });
  
  const materialTheme = createTheme({
    palette: {
      background: {
        default: grey[50], 
      },
      text: {
        primary: grey[800],
      },
    },
  });

  return (
 <>
 <div className="container">
    <CssVarsProvider theme={joyTheme}>
      <ThemeProvider theme={materialTheme}> 
      </ThemeProvider>
    </CssVarsProvider>
</div>
 </>
  );
}

export default App;
