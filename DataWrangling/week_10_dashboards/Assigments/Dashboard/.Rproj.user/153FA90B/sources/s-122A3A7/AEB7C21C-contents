## app.R ##
library(shinydashboard)
library(DT)
library(DDoutlier)


createTextPlot <- function(stringToDisplay){
  par(mar = c(0,0,0,0))
  plot(c(0, 1), c(0, 1), ann = F, bty = 'n', type = 'n', xaxt = 'n', yaxt = 'n')
  text(x = 0.5, y = 0.5, stringToDisplay, 
       cex = 1.6, col = "black")
}

##  content
ui <- dashboardPage(
  dashboardHeader(title = "OD Example"),
  ## Sidebar content
  dashboardSidebar(
    sidebarMenu(
      menuItem("Select Data", tabName = "load"),
      menuItem("Outlier Detection", tabName = "od")
    )
  ),
  dashboardBody(
    tabItems(
      # First tab content (loading the data)
      tabItem(tabName = "load",
              sidebarPanel(
                #Selector for file upload
                fileInput('datafile', 'Choose CSV file',
                          accept=c('text/csv', 'text/comma-separated-values,text/plain', '.csv'))
              ),
              mainPanel(
                DT::dataTableOutput("filetable")
              )
      ),
      
      
      # Outlier Detection Tab
      tabItem(tabName = "od",
              tabsetPanel(
                # The id lets us use input$tabset1 on the server to find the current tab
                id = "odtabset",
                tabPanel("Statistical Test",
                         sidebarPanel(
                           uiOutput("statodCol"),
                         ),
                         mainPanel(
                           plotOutput('statodPlot')
                         )   
                ),
                tabPanel("DB", 
                         sidebarPanel(
                           uiOutput("dbodCol1"),
                           uiOutput("dbodCol2"),
                           numericInput('radius', 'Neighborhood radius', 5),
                           numericInput('ratio', 'Ratio of points in r-neighborhood', 0.05),
                         ),
                         mainPanel(
                           plotOutput('odDBPlot')
                         )
                )
              )
      )    # End of Outlier Detection tab
      
      
    )  # End of tabitems
  )  # End of dashboardbody
)  # End of dashboardPage




server <- function(input, output) {
  #This function is repsonsible for loading in the selected file
  filedata <- reactive({
    infile <- input$datafile
    if (is.null(infile)) {
      # User has not uploaded a file yet
      return(NULL)
    }
    read.csv(infile$datapath)
  })
  
  
  #The following set of functions populate the column selectors
  output$expCol <- renderUI({
    df <-filedata()
    if (is.null(df)) return(NULL)
    
    items=names(df)
    names(items)=items
    selectInput("exploreCol", "Seclect a Column:",items)
    
  })
  
  output$statodCol <- renderUI({
    df <-filedata()
    if (is.null(df)) return(NULL)
    
    items=names(df)
    names(items)=items
    selectInput("stodCol", "Seclect a Column:",items)
    
  })
  
  output$dbodCol1 <- renderUI({
    df <-filedata()
    if (is.null(df)) return(NULL)
    
    items=names(df)
    names(items)=items
    selectInput("dbCol1", "Seclect First Column:",items)
  })
  output$dbodCol2 <- renderUI({
    df <-filedata()
    if (is.null(df)) return(NULL)
    
    items=names(df)
    names(items)=items
    selectInput("dbCol2", "Seclect Second Column:",items, selected = items[2])
  })
  

  
  
  #This previews the CSV data file
  output$filetable <- DT::renderDataTable({
    df <-filedata()
    if (is.null(df)) return(NULL)
    data.frame(names(df))
  })
  
  
  
  
  # This renders the detected outliers using the statistical test
  output$statodPlot <- renderPlot({
    createTextPlot("TODO: You have to implement this...")
  })
  
  # This renders the detected outliers
  output$odDBPlot <- renderPlot({
    df <-filedata()
    if (is.null(df)) return(NULL)
    if (is.null(input$dbCol1) || is.null(input$dbCol2)) return(NULL)
    if (input$dbCol1 == input$dbCol2)
    { return(createTextPlot("You have selected the same column twice"))}
    odDBData <- df[, c(input$dbCol1, input$dbCol2)]
    # Remove any records with missing values -- in case you used movies data
    odDBData <- odDBData[complete.cases(odDBData), ]
    idx = vector(mode = "logical", length = nrow(odDBData))
    for (col in names(odDBData)){
      idx = idx || (odDBData[, col] == "")
    }
    odDBData <- odDBData[!idx, ]
    
    # Check if radius and ratio are numeric or not 
    if (!is.numeric(input$radius) || !is.numeric(input$ratio) ||
        !is.numeric(odDBData[,1]) || !is.numeric(odDBData[, 2])){
      return (NULL)      
    }
    # Classify observations
    cls_observations <- DB(dataset=odDBData, d=input$radius, fraction=input$ratio)$classification
    
    # Remove outliers from dataset
    Xi <- odDBData[cls_observations=='Inlier',]
    classes <- replace(cls_observations, cls_observations == 'Inlier', 4)
    classes <- replace(classes, classes == 'Outlier', 2)
    
    plot(odDBData, col = classes, pch = 4, cex = 3, lwd = 4,
         xlab = input$dbCol1, ylab = input$dbCol2)
  })
  

  
 
}

shinyApp(ui, server)

