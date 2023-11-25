import {useForm} from 'react-hook-form'

// useForm sirve par registrar y guardar los campos de los forms
// cuando el form haga el submit va a guardar los data con handlesubmit
export function Formulario() {
  const {register, handleSubmit, formState:{errors}} = useForm()
  const onSubmit = (data) =>
  alert(JSON.stringify(data));

  return (

      <form onSubmit={handleSubmit(onSubmit)} >
        <input placeholder="Ingrese Title" 
         {...register("title",{required:true})} 
         />
         {errors.title && <span>Title requerido</span> }
        <textarea rows={3} placeholder="descripcion" 
         {...register("descripcion",{required:true})} 
        
        > </textarea>
         {errors.descripcion && <span>Descripcion requerido</span> }

        <button>Save</button>
      </form>

    
  )
}

