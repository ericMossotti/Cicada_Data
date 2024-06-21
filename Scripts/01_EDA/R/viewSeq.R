# ---- Exploratory data analysis functions with R
# ---- viewDNA 
# 
# Returns sequences
viewSeq <- function (r_filePath = r_filePath,
                     set = NULL,
                     seqFormat = "fasta",
                     isDNA = TRUE) {
    
    if (exists("codeSeq") == FALSE) { # Determine if object is in memory
        if (isTRUE(isDNA)) {
            # For DNA, hence "DNA"...StringSet
            codeSeq <- Biostrings::readDNAStringSet(filepath = r_file_path, format = seqFormat)
            
        } else { # For other sequence data types, hence "B"...StringSet
            codeSeq <- Biostrings::readBStringSet(filepath = r_file_path, format = seqFormat)
        }
    }
    
    if (!is.null(set)) { # Return subset or full sequence
        return(codeSeq[set])
    } else {
        return(codeSeq)
    }
}
