# MLOPS_OOPS
This repo will cover end to end for Python OOPs

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Office-Oriented Practice with Python OOP</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background-color: #f4f6f8;
      color: #333;
      margin: 0;
      padding: 20px;
    }
    h1, h2 {
      color: #2c3e50;
    }
    h1 {
      text-align: center;
      margin-bottom: 30px;
    }
    section {
      margin-bottom: 40px;
    }
    code {
      background-color: #eef;
      padding: 4px 6px;
      border-radius: 4px;
      font-family: Consolas, monospace;
    }
    pre {
      background-color: #eef;
      padding: 15px;
      border-radius: 6px;
      overflow-x: auto;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 15px;
    }
    th, td {
      border: 1px solid #ccc;
      padding: 10px;
      text-align: left;
    }
    th {
      background-color: #dfe6e9;
    }
    .emoji {
      font-size: 1.2em;
      margin-right: 5px;
    }
  </style>
</head>
<body>

  <h1>🏢 Office-Oriented Practice with Python OOP</h1>

  <section>
    <h2>📦 1. What is a Class?</h2>
    <p>A <strong>class</strong> is a blueprint for creating objects. It defines the properties (attributes) and behaviors (methods) that the objects created from it will have.</p>
    <pre><code>class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def work(self):
        print(f"{self.name} is working in the {self.department} department.")</code></pre>
  </section>

  <section>
    <h2>🧍 2. What is an Object?</h2>
    <p>An <strong>object</strong> is an instance of a class. It’s a real-world entity created using the class blueprint.</p>
    <pre><code>emp1 = Employee("Raj", "Engineering")
emp2 = Employee("Priya", "Marketing")

emp1.work()  # Output: Raj is working in the Engineering department.</code></pre>
  </section>

  <section>
    <h2>⚙️ 3. What is the <code>__init__</code> Function?</h2>
    <p>The <code>__init__</code> function is a special method called a <strong>constructor</strong>. It runs automatically when a new object is created and is used to initialize the object’s attributes.</p>
    <pre><code>def __init__(self, name, department):
    self.name = name
    self.department = department</code></pre>
  </section>

  <section>
    <h2>🧬 4. What is Inheritance?</h2>
    <p><strong>Inheritance</strong> allows one class to inherit the properties and methods of another. It promotes code reuse and logical hierarchy.</p>
    <pre><code>class Manager(Employee):
    def __init__(self, name, department, team_size):
        super().__init__(name, department)
        self.team_size = team_size

    def manage(self):
        print(f"{self.name} manages a team of {self.team_size} people.")</code></pre>

    <pre><code>mgr = Manager("Anita", "Engineering", 5)
mgr.work()     # Inherited from Employee
mgr.manage()   # Defined in Manager</code></pre>
  </section>

  <section>
    <h2>🧑‍🎓 Bonus: Intern Class Example</h2>
    <pre><code>class Intern(Employee):
    def __init__(self, name, department, duration):
        super().__init__(name, department)
        self.duration = duration

    def learn(self):
        print(f"{self.name} is learning for {self.duration} months.")</code></pre>

    <pre><code>intern = Intern("Karan", "Design", 3)
intern.work()
intern.learn()</code></pre>
  </section>

  <section>
    <h2>🧠 Summary Table</h2>
    <table>
      <thead>
        <tr>
          <th>Concept</th>
          <th>Description</th>
          <th>Example Class</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Class</td>
          <td>Blueprint for creating objects</td>
          <td><code>Employee</code></td>
        </tr>
        <tr>
          <td>Object</td>
          <td>Instance of a class</td>
          <td><code>emp1 = Employee(...)</code></td>
        </tr>
        <tr>
          <td><code>__init__</code></td>
          <td>Constructor method to initialize object attributes</td>
          <td><code>def __init__(...)</code></td>
        </tr>
        <tr>
          <td>Inheritance</td>
          <td>One class inherits from another to reuse and extend functionality</td>
          <td><code>Manager(Employee)</code></td>
        </tr>
      </tbody>
    </table>
  </section>

</body>
</html>

