#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/proc_fs.h>
#include <linux/sched.h>
#include <asm/uaccess.h>
#include <linux/linkage.h>
#include <linux/uaccess.h>
#include <linux/slab.h>
//#include "suma.c"

int len,temp,sumaa, semilla;
unsigned long to_user, from_user;

char *msg;
char opcion [1];




int read_proc(struct file *filp,char *buf,size_t count,loff_t *offp ) 
{
	if(count>temp)
	{
		count=temp;
	}
	temp=temp-count;
	printk(KERN_INFO "Se ejecuto read_proc() de vuelta"); 
	to_user = copy_to_user(buf,msg, count);
	printk(KERN_INFO "read: msg = %s\n",msg);
	printk(KERN_INFO "read: buf = %s\n",buf);
	
	
	if(count==0)
		temp=len;
	   
	return count;
}

int write_proc(struct file *filp,const char *buf,size_t count,loff_t *offp)
{

	from_user = copy_from_user(msg,buf,count);
	opcion[0] = buf[0];
	printk(KERN_INFO "se ejecuto write_proc()"); 
	printk(KERN_INFO "write: buf = %s\n",buf); 
	printk(KERN_INFO "write: msg = %s\n",msg);
	printk(KERN_INFO "write: opcion: %s\n",opcion);
	//sumaa = suma(2,3);
	//printk(KERN_INFO "write: suma: %d\n",sumaa);
	//mysrand(42);
	//semilla = myrand();
	//printk(KERN_INFO "write: semilla: %d\n",semilla);
	
	len=count;
	temp=len;
	return count;
}

struct file_operations proc_fops = {
	read: read_proc,
	write: write_proc
};

void create_new_proc_entry(void)  //use of void for no arguments is compulsory now 
{
	proc_create("hello",7,NULL,&proc_fops);
	msg=kmalloc(2*sizeof(char),GFP_USER);
	printk(KERN_INFO "Se creo una nueva entrada en /proc\n"); 
}

int proc_init (void)
{
	create_new_proc_entry();
	return 0;
}

void proc_cleanup(void)
{
	remove_proc_entry("hello",NULL);
	kfree(msg);
}

MODULE_LICENSE("GPL"); 
module_init(proc_init);
module_exit(proc_cleanup);
