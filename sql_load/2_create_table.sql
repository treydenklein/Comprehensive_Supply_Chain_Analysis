-- Create sales_data table
CREATE TABLE public.sales_data (
    order_number TEXT,
    sales_channel TEXT,
    warehouse_code TEXT,
    procured_date DATE,
    order_date DATE,
    ship_date DATE,
    delivery_date DATE,
    sales_team_id TEXT,
    customer_id TEXT,
    store_id TEXT,
    product_id TEXT,
    order_quantity INT,
    unit_cost NUMERIC,
    unit_price NUMERIC,
    order_cost NUMERIC,
    order_revenue NUMERIC,
    order_profit NUMERIC
);

-- Set ownership of the tables to the postgres user
ALTER TABLE public.sales_data OWNER TO postgres;