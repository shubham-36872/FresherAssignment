#include<iostream>
using namespace std;
class Shape
{
private:
	float area;
public:
	Shape( void )
	{
		this->area = 0;
	}
    void setArea(int area){
        this->area = area;
    }
    float getArea(void){
        return this->area;
    }
	virtual void acceptRecord( void ) = 0;

	virtual float calculateArea( void ) = 0;
	
	void printRecord( void ){
		cout<<"Area	:	"<<this->getArea()<<endl;
	}
};
class Rectangle : public Shape
{
private:
	float breadth;
    float length;
public:
	Rectangle( void )
	{
		this->length = 0;
		this->breadth = 0;
	}
	void setBreadth(int breadth){
		this->breadth = breadth;
	}
	float getBreadth(void){
		return this->breadth;
	}
	void setLength(int length){
		this->length= length;
	}
	float getLength(void){
		return this->length;
	}
	void acceptRecord( void )
	{
		cout<<"Length	:	";
		cin>>this->length;
		cout<<"Breadth	:	";
		cin>>this->breadth;
	}
	float calculateArea( void )
	{
		this->setArea( this->length * this->breadth);
		return this->getArea();
	}
};


class Circle : public Shape
{
private:
	float radius;
public:
	Circle( void ){
		this->radius = 0;
	}
	void setRadius(int radius){
		this->radius = radius;
	}
	float getRadius(){
		return this->radius;
	}
	void acceptRecord( void ){
		cout<<"Radius	:	";
		cin>>this->radius;
	}
	float calculateArea( void ){
		this->setArea( 3.142 * radius * radius);
		return this->getArea();
	}
};
class Triangle:public Shape{
private:
	float base;
	float height;
public:
	Triangle( void ){
		this->base = 0;
		this->height = 0;
	}
	void setBase(int base){
		this->base = base;
	}
	float getBase(){
		return this->base;
	}
	void setHeight(int height){
		this->height= height;
	}
	float getHeight(){
		return this->height;
	}
	void acceptRecord( void ){
		cout<<"Enter Base	:	";
		cin>>this->base;
		cout<<"Enter height	:	";
		cin>>this->height;
	}
	float calculateArea( void ){
		this->setArea( (this->base * this->height)/2);
		return this->getArea();
	}	
};
class Square : public Rectangle{
public:
    Square(){
        this->setLength(0);
    }  
    void acceptRecord( void ){
    int value;
	cout<<"Length	:	";
	cin>>value;
	this->setLength(value);
   }
   float calculateArea( void ){
	this->setArea( this->getLength() * this->getLength());
	return this->getArea();
   }
};

int menu_list( void )
{
	int choice;
	cout<<"0.Exit"<<endl;
	cout<<"1.Rectangle"<<endl;
	cout<<"2.Circle"<<endl;
	cout<<"3.Triangle"<<endl;
	cout<<"4.Square"<<endl;
	cout<<"Enter choice	:	";
	cin>>choice;
	return choice;
}
int main( void )
{
	int choice;
	while( ( choice = ::menu_list( ) ) != 0 )
	{
		Shape *ptr = NULL;
		switch( choice )
		{
		case 1:
			ptr = new Rectangle( );	
			break;
		case 2:
			ptr = new Circle( );	
			break;
		case 3:
			ptr = new Triangle( );	
			break;	
		case 4:
		    ptr = new Square();
		}
		if( ptr != NULL )
		{
			ptr->acceptRecord( );	
			ptr->calculateArea( );	
			ptr->printRecord( );
			delete ptr;
		}
	}
	return 0;
}