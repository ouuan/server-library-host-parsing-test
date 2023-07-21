use hyper::header::{CONNECTION, CONTENT_TYPE, HOST};
use hyper::service::{make_service_fn, service_fn};
use hyper::{http, Body, Request, Response, Server};
use std::net::SocketAddr;

async fn handle_request(req: Request<Body>) -> Result<Response<Body>, http::Error> {
    let host_header = match req.headers().get(HOST) {
        Some(header_value) => header_value.to_str().unwrap(),
        None => "undefined",
    };

    Response::builder()
        .header(CONTENT_TYPE, "text/plain")
        .header(CONNECTION, "close")
        .body(Body::from(format!("[{}]", host_header)))
}

#[tokio::main]
async fn main() {
    let addr = SocketAddr::from(([127, 0, 0, 1], 3003));

    let make_svc = make_service_fn(|_| async { Ok::<_, http::Error>(service_fn(handle_request)) });

    let server = Server::bind(&addr).serve(make_svc);

    println!("Server running at http://{}", addr);

    if let Err(e) = server.await {
        eprintln!("Server error: {}", e);
    }
}
