-- Constants for the game
local GRID_SIZE = 20  -- Size of each grid cell in pixels
local GRID_WIDTH = 20  -- Number of cells in the grid (horizontally)
local GRID_HEIGHT = 15  -- Number of cells in the grid (vertically)
local score = 0  -- Initialize the score to 0

-- Enum for the different types of game objects
local OBJECT_TYPE = {
  SNAKE = 1,
  FOOD = 2,
  WALL = 3,
}

-- Game object class
local GameObject = {}

function GameObject:new(x, y, type)
  local object = {x = x, y = y, type = type}
  self.__index = self
  return setmetatable(object, self)
end

function GameObject:draw()
  -- Draw the object based on its type
  if self.type == OBJECT_TYPE.SNAKE then
    love.graphics.setColor(1, 1, 1)  -- White color for the snake
  elseif self.type == OBJECT_TYPE.FOOD then
    love.graphics.setColor(0, 1, 0)  -- Green color for the food
  elseif self.type == OBJECT_TYPE.WALL then
    love.graphics.setColor(0, 0, 0)  -- Black color for the walls
  end
  
  -- Draw a rectangle at the object's position
  love.graphics.rectangle('fill', (self.x - 1) * GRID_SIZE, (self.y - 1) * GRID_SIZE, GRID_SIZE, GRID_SIZE)
end

-- Snake class
local Snake = {}

function Snake:new(x, y)
  local snake = {
    body = {GameObject:new(x, y, OBJECT_TYPE.SNAKE)},  -- Initialize the snake's body with a single cell at (x, y)
    direction = 'right',  -- Initial direction of the snake
  }
  self.__index = self
  return setmetatable(snake, self)
end

function Snake:update()
  -- Move the snake's body in the current direction
  local head = self.body[1]
  local next_x, next_y = head.x, head.y
  if self.direction == 'right' then
    next_x = next_x + 1
  elseif self.direction == 'left' then
    next_x = next_x - 1
  elseif self.direction == 'up' then
    next_y = next_y - 1
  elseif self.direction == 'down' then
    next_y = next_y + 1
  end

  -- Check if the snake has collided with a wall or itself
  local game_over = false
  for i, object in ipairs(game_objects) do
    if object.x == next_x and object.y == next_y then
      if object.type == OBJECT_TYPE.WALL or object.type == OBJECT_TYPE.SNAKE then
        game_over = true
        break
      end
    end
  end
  -- Increment the score when the snake eats a piece of food
  if self.growing then
    score = score + 1
  end
  
  if game_over then
    -- End the game if the snake has collided with a wall or itself
    love.event.quit()
  else
    -- Add a new cell at the head of the snake
    local new_head = GameObject:new(next_x, next_y, OBJECT_TYPE.SNAKE)
    table.insert(self.body, 1, new_head)
    
    -- Check if the snake has eaten a piece of food
    if not self.growing then
      -- Remove the last cell of the snake if it is not growing
      table.remove(self.body)
    end
    self.growing = false  -- Reset the growing flag
  end


  -- Limit the frame rate to 10 FPS
  love.timer.sleep(1/10)
end


function Snake:draw()
  -- Draw all cells of the snake's body
  for i, cell in ipairs(self.body) do
    cell:draw()
  end
end

function Snake:changeDirection(direction)
  -- Change the direction of the snake if it is not moving in the opposite direction
  if self.direction == 'right' and direction ~= 'left' then
    self.direction = direction
  elseif self.direction == 'left' and direction ~= 'right' then
    self.direction = direction
  elseif self.direction == 'up' and direction ~= 'down' then
    self.direction = direction
  elseif self.direction == 'down' and direction ~= 'up' then
    self.direction = direction
  end
end

-- Set up the game
function love.load()
  -- Initialize the random seed
  math.randomseed(os.time())
  
  -- Initialize the game objects list
  game_objects = {}
  
  -- Add walls around the perimeter of the grid
  for x = 0, GRID_WIDTH + 1 do
    for y = 0, GRID_HEIGHT + 1 do
      if x == 0 or x == GRID_WIDTH + 1 or y == 0 or y == GRID_HEIGHT + 1 then
        table.insert(game_objects, GameObject:new(x, y, OBJECT_TYPE.WALL))
      end
    end
  end
  
  -- Add the snake to the game
  snake = Snake:new(10, 10)
  table.insert(game_objects, snake)
  
  -- Add some food to the game
  addFood()
end

-- Update the game
function love.update(dt)
  -- Update the snake
  snake:update()
  
  -- Check if the snake has eaten a piece of food
  for i, object in ipairs(game_objects) do
    if object.type == OBJECT_TYPE.FOOD and object.x == snake.body[1].x and object.y == snake.body[1].y then
      -- Remove the eaten food from the game
      table.remove(game_objects, i)
      
      -- Add a new piece of food
      addFood()
      
      -- Make the snake grow
      snake.growing = true
    end
  end
end

-- Draw the game
function love.draw()
  -- Draw all game objects
  for i, object in ipairs(game_objects) do
    object:draw()
  end
  love.graphics.print("Score: " .. score, 10, 10)
end

-- Handle key press events
function love.keypressed(key)
  if key == 'right' then
    snake:changeDirection('right')
  elseif key == 'left' then
    snake:changeDirection('left')
  elseif key == 'up' then
    snake:changeDirection('up')
  elseif key == 'down' then
    snake:changeDirection('down')
  end
end

-- Add a piece of food to the game
function addFood()
  -- Generate a random position for the food
  local x, y = math.random(GRID_WIDTH), math.random(GRID_HEIGHT)
  
  -- Make sure the position is not already occupied
  while isPositionOccupied(x, y) do
    x, y = math.random(GRID_WIDTH), math.random(GRID_HEIGHT)
  end
  
  -- Add the food to the game
  table.insert(game_objects, GameObject:new(x, y, OBJECT_TYPE.FOOD))
end

-- Check if a position is occupied by a game object
function isPositionOccupied(x, y)
  for i, object in ipairs(game_objects) do
    if object.x == x and object.y == y then
      return true
    end
  end
  return false
end
