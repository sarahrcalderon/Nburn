import './App.css';
import { ThemeProvider, createTheme } from "@mui/material/styles";
import { CssBaseline, Button } from "@mui/material";


const theme = createTheme({
  palette: {
    mode: "dark", // Modo claro ou escuro
    primary: {
      main: "#1976d2",
    },
    secondary: {
      main: "#dc004e",
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
    <CssBaseline />
    <div>
      <h1>teste thema</h1>
      <Button variant="contained" color="primary">
        Botão Primário
      </Button>
    </div>
  </ThemeProvider>
  );
}

export default App;
