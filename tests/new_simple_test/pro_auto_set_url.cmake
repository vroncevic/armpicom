#
# @brief   new_simple_test setup project url
# @version v1.9.1
# @date    2024-07-08
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

# Macro for setup project url
macro(pro_auto_set_url TARGET)
    file(
        RELATIVE_PATH URL_REL_PATH "${PRO_PATH}" "${CMAKE_CURRENT_LIST_DIR}"
    )
    pico_set_program_url(${TARGET} "${URL_REL_PATH}")
endmacro()

