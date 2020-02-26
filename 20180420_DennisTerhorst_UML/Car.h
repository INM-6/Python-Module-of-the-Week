/// class Car - General interface of a car
class Car {
  // Attributes
public:
  int[10] badvariable;
private:
  static int Ninstances;
  double weight;
  // Operations
public:
  ~Car ();
  virtual location position () = 0;
};

