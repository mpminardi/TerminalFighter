#pragma once

#include <map>

#include <SDL2/SDL.h>
#include <SDL_image.h>

#include "I_GraphicsHandler.h"

class GraphicsHandler : public I_GraphicsHandler {

public:
    /*
     * Constructor for the Graphics Handler
     * Constructor that takes an SDL_Renderer and a vector of std::strings that point to graphics assets
     * @param renderer the <code>SDL_Renderer&</code> that will be used for all the graphics 
     *  manipulation and draws to the screen
     * @param graphic_paths is the path to graphics assets that you want pre-loaded upon creation
     *  of this object, rather than loading them (which you can) during the game play
     *  These assets will be loaded into <code>game_graphics_</code> 
     */
    GraphicsHandler(SDL_Renderer& renderer, std::vector<std::string> graphic_paths);
    void init(const std::vector<std::string>& graphic_paths);
    void draw(SDL_Texture* texture, SDL_Rect dest_rect,
              GraphicPriority priority, bool cleanup, double angle_clockwise, SDL_Point* rotation_point);

    void draw(SDL_Texture* texture, int x_pos, int y_pos,
              GraphicPriority priority, bool cleanup, double angle_clockwise, SDL_Point* rotation_point);

    void draw(SDL_Surface* surface, int x_pos, int y_pos,
              GraphicPriority priority, bool cleanup, double angle_clockwise, SDL_Point* rotation_point);

    void draw(SDL_Texture* texture, SDL_Rect dest_rect,
              GraphicPriority priority, bool cleanup);

    void draw(SDL_Texture* texture, int x_pos, int y_pos,
              GraphicPriority priority, bool cleanup);

    void draw(SDL_Surface* surface, int x_pos, int y_pos,
              GraphicPriority priority, bool cleanup);

    SDL_Texture* load_image(std::string path); /*will return textures that were loaded on init()*/
    void update_screen();

private:
    SDL_Texture* internal_load_image(std::string path);
    SDL_Renderer& renderer_;
    std::map <std::string, SDL_Texture*> game_graphics_;
    std::map <GraphicPriority, std::vector<DrawRequest>> draw_queue_;
};
