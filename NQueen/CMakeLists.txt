cmake_minimum_required(VERSION 3.10)
project(nqueen)

set(SOURCE_FILES
    "src/main.cpp"
    "src/NQueen.cpp"
    "src/UCS.cpp"
    "src/Genetic.cpp"
    "src/DisplayTable.cpp"
    "src/HillClimbing.cpp")

add_executable(${PROJECT_NAME} ${SOURCE_FILES})