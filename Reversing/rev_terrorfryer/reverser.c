uint64_t fryer(char* arg)
{
    if (init.1 == 0)
    {
        seed = 0x13377331;
        init.1 = 1;
    }
    
    int result = strlen(arg);
    int len = result;
    if (result > 1)
    {
        int64_t r14_1 = (result - 1);
        int64_t i = 0;
        
        do
        {
            int j = ((COMBINE(0, rand_r(&seed)) % (len - i)) + i);
            result = arg[i];
            char* rdx_5 = &arg[j];
            arg[i] = *rdx_5;
            *rdx_5 = result;
            i += 1;
        } while (i != r14_1);
    }
    
    return result;
}

int main(int argc, char** argv, char** envp)
{
    void* fsbase;
    int64_t rax = *(fsbase + 0x28);
    setvbuf(__bss_start, nullptr, 2, 0);
    printf("Please enter your recipe for fry…");
    void buf;
    fgets(&buf, 0x40, stdin);
    char* rax_3 = strchr(&buf, 0xa);
    
    if (rax_3 != 0)
        *rax_3 = 0;
    
    fryer(&buf);
    printf("got:      `%s`\nexpected: `%s`\n", &buf, "1_n3}f3br9Ty{_6_rHnf01fg_14rlbtB…");
    
    if (strcmp("1_n3}f3br9Ty{_6_rHnf01fg_14rlbtB…", &buf) == 0)
        puts("Correct recipe - enjoy your meal…");
    else
        puts("This recipe isn't right :(");
    
    *(fsbase + 0x28);
    
    if (rax == *(fsbase + 0x28))
        return 0;
    
    __stack_chk_fail();
    /* no return */
}