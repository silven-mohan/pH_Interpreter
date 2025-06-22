import tkinter
from tkinter import messagebox, simpledialog
from cffi import FFI

ffi=FFI()

ffi.cdef("""
    const char* main(const char* pH_str);
""")

C_SOURCE=r"""
    /** pH Range Identifier **/

    #include<stdio.h>
    #include<ctype.h>
    const char* main(const char* pH_str)
    {
            int pH=atoi(pH_str);
            
            if(pH==1)
            {
                    return "Extremely Acidic";
            }
            else if(pH==2)
            {
                    return "Very Strongly Acidic";
            }
            else if(pH==3)
            {
                    return "Strongly Acidic";
            }
            else if(pH==4)
            {
                    return "Moderately Acidic";
            }
            else if(pH==5)
            {
                    return "Weakly Acidic";
            }
            else if(pH==6)
            {
                    return "Very Weakly Acidic";
            }
            else if(pH==7)
            {
                    return "Neutral";
            }
            else if(pH==8)
            {
                    return " Very Weakly Basic";
            }
            else if(pH==9)
            {
                    return "Weakly Basic";
            }
            else if(pH==10)
            {
                    return "Moderately Basic";
            }
            else if(pH==11)
            {
                    return "Strongly Basic";
            }
            else if(pH==12)
            {
                    return "Very Strongly Basic";
            }
            else if(pH==13)
            {
                    return "Extremely Basic";
            }
            else if(pH==14)
            {
                    return "Highly Basic";
            }
            else
            {
                    return "Please enter between the pH Range(1-14)";
            }
    }
"""

C=ffi.verify(C_SOURCE)

user_input_I=simpledialog.askstring("pH Interpreter", "Enter the pH of the solution:")
user_input=user_input_I.strip().replace(" ", "")

result_cstr=C.main(user_input.encode('utf-8'))
result_str=ffi.string(result_cstr).decode('utf-8')

messagebox.showinfo("pH Interpreter", result_str)
