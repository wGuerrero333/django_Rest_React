import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom';

// import { tareas } from './pages/tasks'; LOS MOULOS DEBEN EMPEZAR EN MAYUSCULA
import { Formulario } from './pages/form';
import { Tareas } from './pages/tasks'
import { Navigator } from './componentes/Navigator';
function App() {
  return (

<BrowserRouter>
<Navigator/>
<Routes>
<Route path='/' element={ <Navigate to={'/main'} />}/>

  <Route path='/main' element={"hello Main page"}/>
  <Route path="/tareas" element={< Tareas />} />
  <Route path="/form" element={< Formulario />} />

</Routes>
</BrowserRouter>

  );
}


export default App
