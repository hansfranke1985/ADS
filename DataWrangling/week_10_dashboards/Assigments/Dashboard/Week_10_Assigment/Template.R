
library(shiny)


# Define UI for application that draws a histogram
ui <- fluidPage(
 
  headerPanel(title = "Sample Aplication"),
  sidebarPanel(
  # *input() functions
  sliderInput(inputId = "num",
              label = "Chose a Number",
              value = 25, step=10,
              min = 1, max = 100),
  textInput(inputId = "title2", label = 'Write a title', value = 'Type your title'),
  
 ),
 mainPanel(
  actionButton(inputId = "go", label = "Update") ,
  # *outputs() functions
  plotOutput(outputId = "hist"),
  verbatimTextOutput(outputId = 'stats'))
)

# Define server logic required to draw a histogram
server <- function(input, output) {
  #store paramets to use at same time:
  data_rect <- eventReactive(input$go, {rnorm(input$num)})
  
  data <- reactive({
    rnorm(input$num)
                  })
  # Logic of Server side (Assemble inputs into outputs)
  #1 save objects output$ (from ui = Outputs)
  output$hist <- renderPlot( { 
                              hist( data_rect(), main = isolate(input$title2 ))
                              } )
  output$stats <- renderPrint( { 
            
            summary( data_rect() )
                               } )
  
  #2 Display with Render()_TYPEOFOBJECT _CODE BLOCK_{}
  # datatable(), image(), plot(), print(), table(), text(), Ui()

  #3 use input values with input$
  
} #end of server

# Run the application 
shinyApp(ui = ui, server = server)



