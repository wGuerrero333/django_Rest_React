import { useEffect, useState } from "react"
import { getAllTask } from "../api/getAllTask"
// tareas inicia como un []
// luego es actulizado constantemente (useEffect)  por setTareas
export function ListaTareasDb() {
    const [tareas, setTareas] = useState([])
    useEffect(() => {
        async function loadTasks() {
            const res = await getAllTask()
            // console.log(res.data)
            setTareas(res.data);
        }
        loadTasks()
    })
    // como se hace un recorrido si usa el mismo key que trae
    return (
        <div> <h1>ListaTareasDb </h1>   
            {
                tareas.map( i => (
                    
                    <div key={i.id}> 
                    <h2> {i.title}</h2>
                    <h4> {i.objetivo}</h4>
                   </div>
                                    

                ))
            }

        </div>
    
  )
}

