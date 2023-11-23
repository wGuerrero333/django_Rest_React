import {Link} from 'react-router-dom'

export function Navigator() {
  return (
    <div>Navigator
    <br />

    <Link to={'/tareas'} > Ir a Tareas </Link>
    <br />
    
    <Link to={'/form'} > Ir a Form</Link>
    <br />
    
    </div>
  )
}

