







def draw_sphere(context, center_x, center_y, radius):






# main circle for the ball
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    context.fill()
#white circle
    context.set_source_rgb(1, 1, 1)  # Set color to white
    white_circle_x = center_x + radius * 0.2  
    white_circle_y = center_y - radius * 0.2
    context.arc(white_circle_x, white_circle_y, radius * 0.4, 0, 2 * math.pi)
    context.fill()

#shadow around the white circle
    shadow_gradient = cairo.RadialGradient(white_circle_x, white_circle_y, radius * 0.35,
                                           white_circle_x, white_circle_y, radius * 0.45)
    shadow_gradient.add_color_stop_rgba(0, 0, 0, 0, 0.2)  
    shadow_gradient.add_color_stop_rgba(1, 0, 0, 0, 0)
    context.set_source(shadow_gradient)
    context.arc(white_circle_x, white_circle_y, radius * 0.45, 0, 2 * math.pi)
    context.fill()
