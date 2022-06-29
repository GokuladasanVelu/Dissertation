def velocities(np):

    npindex=np+1

    u_list = []
    u_value=0
    u_list.extend([u_value for i in range(1, npindex)])

    v_list = []
    v_value=0
    v_list.extend([v_value for i in range(1, npindex)])

    return v_list, u_list
