# **Flask REST Homework**

###### Import insomnia file to have all the required queries

Use '/rooms', '/tenants' or '/staff' for full info on respective topic. 
Here's some examples of other queries.

### **Get info by one of the fields**

Use GET '/page?field=value' format. Only information that was required by homework is 
available.

### **Add a room**

Make a POST to '/rooms' with full room JSON body.

### **Delete an element**
 
 Make DELETE query to '/rooms?number=_value_', '/tenants?pass_id=_value_'
 or '/staff?pass_id=_value_'.
 
### **Update info**

Make a PATCH to '/_page_' with full JSON body of respective class. 
A unique field (number or pass_id) must match an existing object and the query will
update this object's info.
