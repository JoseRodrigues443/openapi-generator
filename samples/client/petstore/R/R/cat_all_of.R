#' Create a new CatAllOf
#'
#' @description
#' CatAllOf Class
#'
#' @docType class
#' @title CatAllOf
#' @description CatAllOf Class
#' @format An \code{R6Class} generator object
#' @field declawed  character [optional]
#' @field additional_properties named list(character) [optional]
#' @importFrom R6 R6Class
#' @importFrom jsonlite fromJSON toJSON
#' @export
CatAllOf <- R6::R6Class(
  "CatAllOf",
  public = list(
    `declawed` = NULL,
    `additional_properties` = NULL,
    #' Initialize a new CatAllOf class.
    #'
    #' @description
    #' Initialize a new CatAllOf class.
    #'
    #' @param declawed declawed
    #' @param additional_properties additonal properties (optional)
    #' @param ... Other optional arguments.
    #' @export
    initialize = function(
        `declawed` = NULL, additional_properties = NULL, ...
    ) {
      if (!is.null(`declawed`)) {
        stopifnot(is.logical(`declawed`), length(`declawed`) == 1)
        self$`declawed` <- `declawed`
      }
      if (!is.null(additional_properties)) {
        for (key in names(additional_properties)) {
          self$additional_properties[[key]] <- additional_properties[[key]]
        }
      }
    },
    #' To JSON string
    #'
    #' @description
    #' To JSON String
    #'
    #' @return CatAllOf in JSON format
    #' @export
    toJSON = function() {
      CatAllOfObject <- list()
      if (!is.null(self$`declawed`)) {
        CatAllOfObject[["declawed"]] <-
          self$`declawed`
      }
      for (key in names(self$additional_properties)) {
        CatAllOfObject[[key]] <- self$additional_properties[[key]]
      }

      CatAllOfObject
    },
    #' Deserialize JSON string into an instance of CatAllOf
    #'
    #' @description
    #' Deserialize JSON string into an instance of CatAllOf
    #'
    #' @param input_json the JSON input
    #' @return the instance of CatAllOf
    #' @export
    fromJSON = function(input_json) {
      this_object <- jsonlite::fromJSON(input_json)
      if (!is.null(this_object$`declawed`)) {
        self$`declawed` <- this_object$`declawed`
      }
      self
    },
    #' To JSON string
    #'
    #' @description
    #' To JSON String
    #'
    #' @return CatAllOf in JSON format
    #' @export
    toJSONString = function() {
      jsoncontent <- c(
        if (!is.null(self$`declawed`)) {
          sprintf(
          '"declawed":
            %s
                    ',
          tolower(self$`declawed`)
          )
        }
      )
      jsoncontent <- paste(jsoncontent, collapse = ",")
      json_string <- as.character(jsonlite::minify(paste("{", jsoncontent, "}", sep = "")))
      json_obj <- jsonlite::fromJSON(json_string)
      for (key in names(self$additional_properties)) {
        json_obj[[key]] <- self$additional_properties[[key]]
      }
      json_string <- as.character(jsonlite::minify(jsonlite::toJSON(json_obj, auto_unbox = TRUE, digits = NA)))
    },
    #' Deserialize JSON string into an instance of CatAllOf
    #'
    #' @description
    #' Deserialize JSON string into an instance of CatAllOf
    #'
    #' @param input_json the JSON input
    #' @return the instance of CatAllOf
    #' @export
    fromJSONString = function(input_json) {
      this_object <- jsonlite::fromJSON(input_json)
      self$`declawed` <- this_object$`declawed`
      self
    },
    #' Validate JSON input with respect to CatAllOf
    #'
    #' @description
    #' Validate JSON input with respect to CatAllOf and throw an exception if invalid
    #'
    #' @param input the JSON input
    #' @export
    validateJSON = function(input) {
      input_json <- jsonlite::fromJSON(input)
    },
    #' To string (JSON format)
    #'
    #' @description
    #' To string (JSON format)
    #'
    #' @return String representation of CatAllOf
    #' @export
    toString = function() {
      self$toJSONString()
    },
    #' Return true if the values in all fields are valid.
    #'
    #' @description
    #' Return true if the values in all fields are valid.
    #'
    #' @return true if the values in all fields are valid.
    #' @export
    isValid = function() {
      TRUE
    },
    #' Return a list of invalid fields (if any).
    #'
    #' @description
    #' Return a list of invalid fields (if any).
    #'
    #' @return A list of invalid fields (if any).
    #' @export
    getInvalidFields = function() {
      invalid_fields <- list()
      invalid_fields
    }
  ),
  # Lock the class to prevent modifications to the method or field
  lock_class = TRUE
)

# Unlock the class to allow modifications of the method or field
CatAllOf$unlock()

#' Print the object
#'
#' @description
#' Print the object
#'
#' @export
CatAllOf$set("public", "print", function(...) {
  print(jsonlite::prettify(self$toJSONString()))
  invisible(self)
})

# Lock the class to prevent modifications to the method or field
CatAllOf$lock()

