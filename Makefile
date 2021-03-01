# f = frontend
# b = backend

B_PATH := ./Backend/property_project
F_PATH := ./Frontend/property-project

b_up:
	make -C $(B_PATH) up

f_up:
	make -C $(F_PATH) up

b_stop:
	make -C $(B_PATH) stop

f_stop:
	make -C $(F_PATH) stop


up: b_up f_up

stop: b_stop f_stop