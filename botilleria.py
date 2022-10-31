class product
{
  code= #codigo interno
  bar_code= #codigo de barras
  name= #nombre del producto
  brand= #marca
  price= #precio del producto
  
    ##fin seccion atributos##
  
    ##metodos##
  
  get_code()
  get_bar_code()
  get_name()
  get_brand()
  get_price()
  
    ##Fin seccion Metodos##
}  
  
class stock
{
  product= #clase producto
  quantity= #cantidad de este producto
  
   ##fin seccion atributos##
   
   ##metodos##

  get_product()
  get_quantity()
    
    ##Fin seccion Metodos##
}

class supplier
{
  code= #codigo del proveedor
  name= #nombre del proveedor
  email= #correo electronico del proveedor
  
    ##fin seccion atributos##
    
    ##metodos##
  
  get_code()
  get_name()
  get_email()
  
    ##Fin seccion Metodos##
}
 
class supplying
{
  supplier= #clase proveedor
  product= #clase producto
  quantity= #cantidad odenada
  arrives_at= #fecha de llegada
  arrived= #indica si llego o no
  
    ##fin seccion atributos##
   
    ##metodos##
  
  get_supplier()
  get_product()
  get_quantity()
  get_arrives_at()
  get_arrived()
  
    ##Fin seccion Metodos##
}

class customer
{
  code= #codigo del cliente
  first_name= #nombre del cliente
  last_name= #apellido paterno  del cliente
  email= #correo electronico del cliente
    
    ##fin seccion atributos##
    
    ##metodos##
  
  get_code()
  get_first_name()
  get_last_name()
  get_email()
  
    ##Fin seccion Metodos##
}
