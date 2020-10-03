import math

def most_likely_translation(current_object: ((float, float), float), previous_objects: ([(float, float)], [float])) -> (float, float):
    
    current_point, current_area = current_object
    
    previous_points, previous_area = previous_objects
    
    smallest_distance = -1
    smallest_distance_index = -1
    closest_ratio_difference_to_zero = -1
    closest_area_index = -1
    
    for i in range(0, len(previous_points)):
        
        distance = math.sqrt( (current_point[0] - previous_points[i][0]) ** 2)
        
        if smallest_distance_index != -1 and distance < smallest_distance:
            smallest_distance = distance
            smallest_distance_index = i
        
        if smallest_distance_index == -1:
            smallest_distance = distance
            smallest_distance_index = i
            
        area_ratio = previous_area[i] / current_area
        ratio_difference = abs( 1 - area_ratio)
        
        if closest_area_index != -1 and ratio_difference < closest_ratio_difference_to_zero:
            closest_ratio_difference_to_zero = ratio_difference
            closest_area_index = i
            
        if closest_area_index == -1:
            closest_ratio_difference_to_zero = ratio_difference
            closest_area_index = i
            
    if smallest_distance_index != closest_area_index:
        distance_weight = 0.8
        area_ratio_weight = 0.1
        
        point_a_distance = math.sqrt( (current_point[0] - previous_points[smallest_distance_index][0]) ** 2 )
        point_a_area_ratio = previous_area[smallest_distance_index] / current_area
        point_a_ratio_difference = abs( 1 - point_a_area_ratio )
        
        point_b_distance = math.sqrt(( current_point[0] - previous_points[closest_area_index][0]) ** 2 )
        point_b_area_ratio = previous_area[closest_area_index] / current_area
        point_b_ratio_difference = abs( 1 - point_b_area_ratio )
        
        probability_mapping_to_a = ( distance_weight ) * ( point_a_distance ) - ( area_ratio_weight ) * ( point_a_ratio_difference )
        
        probability_mapping_to_b = ( distance_weight ) * ( point_b_distance ) - ( area_ratio_weight ) * ( point_b_ratio_difference )
        
        if probability_mapping_to_a < probability_mapping_to_b: most_probable_mapping_index = smallest_distance_index
        else: most_probable_mapping_index = closest_area_index
        
    else: 
        most_probable_mapping_index = smallest_distance_index
        
    return previous_points[most_probable_mapping_index]