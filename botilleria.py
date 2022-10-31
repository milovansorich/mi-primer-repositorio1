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
  
  set_code(code)
  set_bar_code(bar_code)
  set_name(name)
  set_brand(brand)
  set_price(price)
}  
  
class stock
{
  product= #clase producto
  quantity= #cantidad de este producto
    
  ##metodos##

  get_product()
  get_quantity()
  
  set_product(product)
  set_quantity(quantity)
}

class supplier
{
  code= #codigo del proveedor
  name= #nombre del proveedor
  email= #correo electronico del proveedor
  
  ##metodos##
  
  get_code()
  get_name()
  get_email()
  
  set_code(code)
  set_name(name)
  set_email(email)  
}
 
class supplying
{
  supplier= #clase proveedor
  product= #clase producto
  quantity= #cantidad odenada
  arrives_at= #fecha de llegada
  arrived= #indica si llego o no
  
  
  ##metodos##
  
  get_supplier()
  get_product()
  get_quantity()
  get_arrives_at()
  get_arrived()
  
  set_supplier(supplier)
  set_product(product)
  set_quantity(quantity)
  set_arrives_at(arrives_at)
  set_arrived(arrived) 
}

class customer
{
  code= #codigo del cliente
  first_name= #nombre del cliente
  last_name= #apellido paterno  del cliente
  email= #correo electronico del cliente
   
  ##metodos##
  
  get_code()
  get_first_name()
  get_last_name()
  get_email()
  
  set_code(code)
  set_first_name(first_name)
  set_last_name(last_name)
  set_email(email) 
}

class order
{
  code= #codigo de la orden
  ordered_at= #fecha de la orden
  total= #total a pagar de la orden
  
   ##metodos##
  
  get_code()
  get_ordered_at()
  get_total()
   
  set_code(code)
  set_ordered_at(ordered_at)
  set_total(total)
}

class product_order
{
  order= #clase orden
  product= #clase producto
  quantity= #cantidad de productos pedidos
  
   ##metodos##
  
  get_order()
  get_product()
  get_quantity()
  
  set_order(order)
  set_product(product)
  set_quantity(quantity) 
}
