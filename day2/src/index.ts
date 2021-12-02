import fs from "fs";

class Dive {
  depth: number = 0;
  horizontalPosition: number;
  multipliedPosition: number;
  aim: number;
  commands: string[];

  constructor() {
    this.depth = 0;
    this.horizontalPosition = 0;
    this.aim = 0;
    this.commands = [];
  }

  handleCommands(filename: string): void {
    // Get commands from text file
    this.commands = fs.readFileSync(filename).toString().split("\r\n");
    for (let i = 0; i < this.commands.length; i++) {
      this.readCommands(this.commands[i]);
    }
  }

  readCommands(command: string): void {
    const direction = command.charAt(0);
    const distance = Number(command.charAt(command.length - 1));
    if (direction === "f") {
      this.horizontalPosition += distance;
      this.depth += this.aim * distance;
    } else if (direction === "d") {
      //   this.depth += distance;
      this.aim += distance;
    } else {
      //   this.depth -= distance;
      this.aim -= distance;
    }
  }

  calculatePosition(filename: string): number {
    this.handleCommands(filename);
    console.log(
      "Final Depth:",
      this.depth,
      "Final Horizontal Position:",
      this.horizontalPosition
    );
    this.multipliedPosition = this.depth * this.horizontalPosition;
    return this.multipliedPosition;
  }
}

const main = () => {
  const filepath: string = "./src/input.txt";
  const submarine = new Dive();
  const finalPosition: number = submarine.calculatePosition(filepath);
  console.log("Final position:", finalPosition);
};

main();
