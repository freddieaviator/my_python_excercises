def say_my_name()->None:
    """ Returns Fredrik in a cool way
    
    Args: 
        none

    Returns:
        none
    """
  
    print("""
######## ########  ######## ########  ########  #### ##    ## 
##       ##     ## ##       ##     ## ##     ##  ##  ##   ##  
##       ##     ## ##       ##     ## ##     ##  ##  ##  ##   
######   ########  ######   ##     ## ########   ##  #####    
##       ##   ##   ##       ##     ## ##   ##    ##  ##  ##   
##       ##    ##  ##       ##     ## ##    ##   ##  ##   ##  
##       ##     ## ######## ########  ##     ## #### ##    ## """)

def say_many_names(times):
    for i in range(times):
        say_my_name()

