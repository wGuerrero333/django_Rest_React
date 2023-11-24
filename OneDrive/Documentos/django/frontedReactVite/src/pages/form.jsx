import {useForm} from 'react-hook-form'
// useForm sirve par registrar los campos de los forms
export function Formulario() {
  const {registrar} = useForm()
  return (
    <div>
      <form action="">
        <input placeholder="Ingrese Title" />
        <textarea rows={3} placeholder="descripcion" > </textarea>
        <button>Save</button>
      </form>

    </div>
  )
}

