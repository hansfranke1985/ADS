
##########################################################
######## Example 5: Different Data Visualization Styles ##
##########################################################

library(shiny)
library(shinydashboard)
library(DT)
library(tidyverse)



##  content
u <- dashboardPage(
  dashboardHeader(title = "My Dashboard"),
  ## Sidebar content
  dashboardSidebar(
    sidebarMenu(
      menuItem("Select Data", tabName = "load"),
      menuItem("Data Exploration", tabName = "explore"),
      menuItem("Outlier Detection", tabName = "od"),
      menuItem("Clustering", tabName = "cluster")
    )
  ),
  dashboardBody(
    tabItems(
      # First tab content
      tabItem(tabName = "load",
              sidebarPanel(
                #Selector for file upload
               
                fileInput('datafile', 'Choose CSV file',
                          accept=c('text/csv', 'text/comma-separated-values,text/plain', '.csv'))
              ),
              mainPanel(
                uiOutput("download"),
                DT::dataTableOutput("filetable")
              )
      ),
      
      # Second tab content
      tabItem(tabName = "explore",
              selectInput("visStyle", "Visualization Style", c("Select an option .. ", "Scatter", "Histogram", "Tabular")),
              conditionalPanel(condition = "(input.visStyle == 'Scatter')",
                               sidebarPanel(
                                 uiOutput("expCol"),
                                 #uiOutput("expCol2"),
                                 uiOutput("expCol5"),
                                 #selectInput(inputId = 'shape', label = "Point Shape", seq(from = 1, to = 20), selected = 5),
                                 #selectInput(inputId = 'color', label = "Point Color", seq(from = 1, to = 20), selected = 2),
                                 #selectInput(inputId = 'msize', label = "Marker Size", seq(from = 1, to = 10), selected = 2),
                                 #selectInput(inputId = 'lwidth', label = "Border Line Width", seq(from = 1, to = 10), selected = 2)
                               ),
                               mainPanel(
                                 plotOutput('scatterPlot')
                               ),
              ),
              conditionalPanel(condition = "(input.visStyle == 'Histogram')",
                               sidebarPanel(
                                 uiOutput("expCol2"),
                                 sliderInput(inputId = 'n_bins', label = 'Number of histogram bins', value = 20,
                                             min = 5, max = 25, step = 5)
                                 
                               ),
                               mainPanel(
                                 plotOutput('histPlot')
                               )
              ),
              conditionalPanel(condition = "(input.visStyle == 'Tabular')",

                               mainPanel(
                                 
                                 sliderInput(inputId = "nrows", label = "Chose number of rows", min = 1, max = 100, value = 5 ),
                                 tableOutput('table')
                               )
              )
      ),
      
      # Third tab content
      tabItem(tabName = "od",
              tabsetPanel(
                # The id lets us use input$tabset1 on the server to find the current tab
                id = "tabset1",
                tabPanel("Statistical Outlier Detection", 
                         mainPanel(
                           plotOutput('boxplot')
                          )
                ),
                  
                tabPanel("Distance-Based Outleir Detection", "TODO: implement distance-based outlier detection")
              ),
      ),
      
      # Fourth tab content
      tabItem(tabName = "cluster",
              uiOutput("expCol3"),
              uiOutput("expCol4"),
              sliderInput(inputId = "num_k",
                          label = "Chose a Number of Means",
                          value = 4, step=1,
                          min = 1, max = 10),
              sliderInput(inputId = "num_eps",
                          label = "DBS_SCAN: EPS",
                          value = 0.2, step=0.1,
                          min = 0.1, max = 1),
              #submitButton("Update Plots"),
              
              tabsetPanel(
                # The id lets us use input$tabset1 on the server to find the current tab
                id = "tabset2",
                tabPanel("kmeans", 
                         mainPanel(
                            #uiOutput("expCol3"),
                            #uiOutput("expCol4"),
                            plotOutput('kmeans', height = "300px")     
                            )
                      ),
                tabPanel("DBSCAN", mainPanel(
                     # uiOutput("expCol3"),
                     # uiOutput("expCol4"),
                      
                      plotOutput('DBSCAN', height = "300px")     
                    ) )
              ),
      )
    )
  )
  
)

s <- function(input, output) {
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
    selectInput(inputId = "selectedCol", label = "Select Column:",items)
    
  })
  
  output$expCol2 <- renderUI({
    df <-filedata()
    if (is.null(df)) return(NULL)
    
    items=names(df)
    names(items)=items
    selectInput(inputId = "selectedCol2", label = "Select Column:",items)
    
  })
  
  output$expCol3 <- renderUI({
    df <-filedata()
    df <- df[,1:8]
    if (is.null(df)) return(NULL)
    
    items=names(df)
    names(items)=items
    selectInput(inputId = "selectedCol3", label = "Select Column for X-Axis:",items)
    
  })
  
  output$expCol4 <- renderUI({
    df <-filedata()
    df <- df[,1:8]
    if (is.null(df)) return(NULL)
    
    items=names(df)
    names(items)=items
    selectInput(inputId = "selectedCol4", label = "Select Column for Y-axis:",items)
    
  })
  
  output$expCol5 <- renderUI({
    df <-filedata()
    df <- df[,1:8]
    if (is.null(df)) return(NULL)
    
    items=names(df)
    names(items)=items
    selectInput(inputId = "selectedCol5", label = "Select Column:",items)
    
  })
  
  #text to publish app online (users might download the same .csv file)
  
  output$download <- renderUI({
    url <- a("Link", href="https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_10_dashboards/Assigments/Dashboard/pid.csv")
    tagList("Please download an example file pid.csv", url)
  })
  
  # output$download <- renderText("Please download example file https://github.com/hansfranke1985/ADS/blob/master/DataWrangling/week_10_dashboards/Assigments/Dashboard/pid.csv")
  
  #This previews the CSV data file
  
  output$filetable <- DT::renderDataTable({
    
    df <-filedata()
    if (is.null(df)) return(NULL)
    data.frame(names(df))
  }
  )
    # This renders the scatter plot for the selected column
  
  output$scatterPlot <- renderPlot({
    df <-filedata()
    if (is.null(df)) return(NULL)
    if (input$visStyle == 'Scatter'){
      x <- df[, input$selectedCol]
      y <- df[, input$selectedCol5]
      label <- as_factor(df[,9])
      if(is.numeric(x)){
        #plot(x,y, pch = as.numeric(input$shape), col = as.numeric(input$color),
        #     cex = as.numeric(input$msize), lwd = input$lwidth)
        (ggplot(df, aes(x,y, color=label))+geom_point()+labs(title = ("Simple Scatter Plot")) +theme_minimal())
      }
      else{
        return(NULL)
      }
    }
    else{
      return(NULL)
    }
  })
  
  # This renders the histogramn plot for the selected column
  output$histPlot <- renderPlot({
    df <-filedata()
    if (is.null(df)) return(NULL)
    if (input$visStyle == 'Histogram'){
      selectedData <- df[, input$selectedCol2]
      if (is.numeric(selectedData)){
        hist(selectedData, breaks = as.numeric(input$n_bins))
      }
      else{
        return(NULL)
      }
    }
    else{
      return(NULL)
    }
  })
  
  output$table <- renderTable({
    df <-filedata()
    head(df, n = input$nrows)
  })
  
  # This runs KMeans
  output$kmeans <- renderPlot({
    df <- filedata()
    df <- df[,1:8]
    means <- kmeans(df, centers = input$num_k)
    df <- df %>%
      mutate("labels" = as_factor(means$cluster),
  
      )
    x=df[,input$selectedCol3]
    y=df[,input$selectedCol4]
    
    (ggplot(df, aes(x,y, color=labels))+geom_point()+geom_jitter()+ theme_minimal())
  })
  
  #this runs DBSCAN
  output$DBSCAN <- renderPlot({
    df <- filedata()

    library("fpc")
    fpc_dbs <- fpc::dbscan(df, eps = input$num_eps, MinPts = 5)

    fviz_cluster(fpc_dbs, df, geom = "point", pointsize = input$num_eps)
 
  })
  
  #this runs boxplot (outlier detection)
  output$boxplot <- renderPlot({
      df <- filedata()
      
      ggplot(df, aes(x=df[,8]),y=df[,1])+geom_boxplot()+theme_minimal()
      
     
  }
  )
}

shinyApp(ui = u, server = s)

