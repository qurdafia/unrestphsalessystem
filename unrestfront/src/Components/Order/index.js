import React, { Component } from "react";

import axios from "axios";

import moment from "moment-timezone";
// import Moment from "moment";

export default class Order extends Component {
  constructor(props) {
    super(props);
    this.state = {
      orders:[],
    };
    this.loadOrders = this.loadOrders.bind(this);
  }

  componentDidMount() {
    this.loadOrders();
  }

  async loadOrders()
  {
    const auth = { username: 'mormash', password: '23responder23'}
    const promise = await axios.get("http://localhost:8000/api/orders/", {
      auth: auth
    });

    const status = promise.status;
    // console.log(status);

    if (status===200) {
      const data = promise.data.results;
      const ordersArray = data;
      const orderDetail = [];
      for (const x in ordersArray) {
        const obj = ordersArray[x];
        const cus_url = obj.customer;
        const item_url = obj.item
        const cus_prom = await axios.get(cus_url, {
          auth: auth
        });
        const item_prom = await axios.get(item_url, {
          auth: auth
        });
        orderDetail.push({
          'customer': cus_prom.data, 
          'item': item_prom.data,
          'order_date': obj.order_date,
          'height_inches': obj.height_inches,
          'width_inches': obj.width_inches,
          'quantity': obj.quantity,
          'is_paid': obj.is_paid,
          'is_delivered': obj.is_delivered,
          'is_cancelled': obj.is_cancelled,
          'initial_payment': obj.initial_payment 
        });
      }
      this.setState({orders: orderDetail});
    }
    console.log(this.state.orders);
  }

  render() {
    return(
      <div>
        <h1>Orders</h1>
            {this.state.orders.map((order, index) => { return <div className="order-list" key={index}>
              <span id="date-small">Date: {moment.utc(order.order_date).format('LLL')}</span><br />
              {order.item.name === 'Stickers' || order.item.name === 'Tarpaulin' 
                ? <div>
                    Item: {order.item.name}<br />
                    Price: {order.item.price}<br />
                    Quantity: {order.quantity}<br />
                    Width in inches: {order.width_inches}<br />
                    Hieght in inches: {order.height_inches}<br />
                    Initial payment: {order.initial_payment}<br />
                    {order.is_paid === true 
                      ? <div>
                          <div className="order-balance">
                            <strong>Balance: {Math.round((order.item.price * order.quantity * (order.width_inches * order.height_inches / 144) - (order.initial_payment)) * 100) / 100}</strong><br />
                          </div>
                        </div>
                      : <div>
                          <div className="order-balance-red">
                            <strong>Balance: {Math.round((order.item.price * order.quantity * (order.width_inches * order.height_inches / 144) - (order.initial_payment)) * 100) / 100}</strong><br />
                          </div>
                        </div>
                    }
                    <div className="order-status">
                      Paid: {order.is_paid ? <span id="checked">&#10003;</span> : <span id="unchecked">&#x2715;</span>}&nbsp;
                      Delivered: {order.is_delivered ? <span id="checked">&#10003;</span> : <span id="unchecked">&#x2715;</span>}&nbsp; 
                      Cancelled: {order.is_cancelled ? <span id="checked">&#10003;</span> : <span id="unchecked">&#x2715;</span>}
                    </div>
                  </div>
                : <div>
                    Item: {order.item.name}<br />
                    Price: {order.item.price}<br />
                    Quantity: {order.quantity}<br />
                    Initial payment: {order.initial_payment}<br />
                    {order.is_paid === true 
                      ? <div>
                          <div className="order-balance">
                            <strong>Balance: {Math.round((order.item.price * order.quantity - order.initial_payment) * 100) / 100}</strong><br />
                          </div>
                        </div>
                      : <div>
                          <div className="order-balance-red">
                            <strong>Balance: {Math.round((order.item.price * order.quantity - order.initial_payment) * 100) / 100}</strong><br />
                          </div>
                        </div>
                    }
                    <div className="order-status">
                      Paid: {order.is_paid ? <span id="checked">&#10003;</span> : <span id="unchecked">&#x2715;</span>}&nbsp;
                      Delivered: {order.is_delivered ? <span id="checked">&#10003;</span> : <span id="unchecked">&#x2715;</span>}&nbsp; 
                      Cancelled: {order.is_cancelled ? <span id="checked">&#10003;</span> : <span id="unchecked">&#x2715;</span>}
                    </div>
                  </div>
              }
            </div> })}
      </div>
    )
  }
}