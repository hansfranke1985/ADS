#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(mvtnorm)

draw_normal_contour <- function(s1 = 1, s2 = 1, rho = 0, resolution = 50) {
    
    points <- seq(-4, 4, length.out = resolution)
    points_grid <- as.data.frame(expand.grid(x = points, y = points))
    
    cov12 <- rho * s1 * s2
    Sigma <- matrix(c(s1^2, cov12, cov12, s2^2), nrow = 2)
    Z <- apply(points_grid, 1, dmvnorm, sigma = Sigma)
    Z <- matrix(Z, nrow = resolution, ncol = resolution)
    par(mar = c(2, 2, 2, 2))
    contour(points, points, Z)
    
}

# Define UI for application that draws a histogram
ui <- fluidPage(

    # Application title
    titlePanel("Contour ellipse on bivariate Gaussian"),

    # Sidebar with a slider input for number of bins 
    sidebarLayout(
        sidebarPanel(
            actionButton("reset_input", "Reset all to defaults"),
            sliderInput("rho",
                        withMathJax("$$\\text{Correlation} (\\rho)$$"),
                        min = -1,
                        max = 1,
                        value = 0,
                        step = 0.01),
            sliderInput("s1",
                        withMathJax("$$\\text{Standard deviation}\\; x_1$$"),
                        min = 1e-4,
                        max = 3,
                        value = 1,
                        step = 0.01),
            sliderInput("s2",
                        withMathJax("$$\\text{Standard deviation}\\; x_2$$"),
                        min = 1e-4,
                        max = 3,
                        value = 1,
                        step = 0.01),
            numericInput("resolution", 
                         "Line quality (more is better but slower)",
                         min = 10,
                         max = 1000,
                         value = 50,
                         step = 10)
        ),

        # Show a plot of the generated distribution
        mainPanel(
           plotOutput("distPlot", width = "500px", height = "500px")
        )
    )
)

# Define server logic required to draw a histogram
server <- function(input, output, session) {
    
    observeEvent(input$reset_input, {
        updateNumericInput(session, "resolution", value = 50)
        updateSliderInput(session, "rho", value = 0)
        updateSliderInput(session, "s1", value = 1)
        updateSliderInput(session, "s2", value = 1)
    })
    
    output$distPlot <- renderPlot({
        draw_normal_contour(input$s1^2,
                            input$s2^2,
                            rho = input$rho,
                            resolution = input$resolution)
        
    })
}

# Run the application 
shinyApp(ui = ui, server = server)
