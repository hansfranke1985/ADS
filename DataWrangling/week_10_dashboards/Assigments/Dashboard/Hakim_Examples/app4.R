##########################################################
######## Example 3: Data distribution ####################
##########################################################

library(shinydashboard)

u <- pageWithSidebar(
   headerPanel('Data distribution'),
   sidebarPanel(
      selectInput('xcol', 'X Variable', names(iris)),
      sliderInput(inputId = 'n_bins', label = 'Number of histogram bins', value = 20,
                  min = 10, max = 50, step = 5),
      checkboxInput(inputId = 'density', label = strong("Show density estimation"), value = FALSE),
   ),
   
   mainPanel(
      plotOutput('plothist'),
      conditionalPanel(condition = "input.density == true",
                       sliderInput(inputId = 'bw_adjust', label = 'Bandwidth Adjustment', value = 0.2,
                                   min = 0.1, max = 2, step = 0.2)
      )
   )
)

s <- function(input, output, session) {
   
   # Create a dataframe for the selected variable
   selectedData <- reactive({
      iris[, input$xcol]
   })
   
   
   output$plothist <- renderPlot({
      hist(selectedData(), probability = TRUE, breaks = as.numeric(input$n_bins),
           xlab = input$xcol, main = c("The distribution of ", input$xcol))
      if (input$density){
         dens <- density(selectedData(), adjust = as.numeric(input$bw_adjust))
         lines(dens, col = "blue")
      }
   })
   
}

shinyApp(ui = u, server = s)
