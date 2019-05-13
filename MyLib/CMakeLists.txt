project(MYLIB)

IF (APPLE)
  set(INSTALL_NAME_DIR @executable_path/../lib)
  set(CMAKE_MACOSX_RPATH 1)
ENDIF (APPLE)

# Sets for output directory for executables and libraries.
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

file(GLOB MY_LIB_ALL RELATIVE ${PROJECT_SOURCE_DIR} src/*.c)

add_library(mylib SHARED ${MY_LIB_ALL})
target_include_directories(mylib PUBLIC ${PROJECT_SOURCE_DIR}/include)

install(TARGETS mylib
          LIBRARY DESTINATION lib
          PUBLIC_HEADER DESTINATION include)
