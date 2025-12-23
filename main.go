package main

import (
	"fmt"
	"math"
)

type Rectangle struct {
	Width  float64
	Height float64
	Color  string
}

func (r Rectangle) Area() float64 {
	return r.Width * r.Height
}

func (r Rectangle) String() string {
	return fmt.Sprintf("Прямоугольник %s цвета шириной %.0f и высотой %.0f. Площадь = %.2f.",
		r.Color, r.Width, r.Height, r.Area())
}

type Circle struct {
	Radius float64
	Color  string
}

func (c Circle) Area() float64 {
	return math.Pi * c.Radius * c.Radius
}

func (c Circle) String() string {
	return fmt.Sprintf("Круг %s цвета радиусом %.0f. Площадь = %.2f.",
		c.Color, c.Radius, c.Area())
}

type Square struct {
	Side  float64
	Color string
}

func (s Square) Area() float64 {
	return s.Side * s.Side
}

func (s Square) String() string {
	return fmt.Sprintf("Квадрат %s цвета со стороной %.0f. Площадь = %.2f.",
		s.Color, s.Side, s.Area())
}


func printColored(text string, colorCode string) {
	resetColor := "\033[0m"
	fmt.Println(colorCode + text + resetColor)
}


func main() {
	const (
		ColorRed   = "\033[31m"
		ColorGreen = "\033[32m"
		ColorBlue  = "\033[34m"
	)

	N := 10.0

	rect := Rectangle{Width: N, Height: N, Color: "синего"}
	circle := Circle{Radius: N, Color: "зеленого"}
	square := Square{Side: N, Color: "красного"}

	printColored(fmt.Sprintf("Создан %s", rect), ColorBlue)
	printColored(fmt.Sprintf("Создан %s", circle), ColorGreen)
	printColored(fmt.Sprintf("Создан %s", square), ColorRed)
}
