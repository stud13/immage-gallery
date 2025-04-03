import React from "react";
//import { Button, Col, Container, Form, Row } from "react-bootstrap";
import Button from "react-bootstrap/Button";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import Form from "react-bootstrap/Form";
import Row from "react-bootstrap/Row";

const Search = ({word, setWord, handleSubmit}) => {
    return(
        <Container className="mt-4">
            <Row className="justify-content-center">
                <Col xs={12} md={8}>
                    <Form onSubmit={handleSubmit}>
                        <Form.Group as={Row}>
                            <Col xs={9}>
                                <Form.Control
                                    type="text"
                                    value={word}
                                    onChange={(e) => setWord(e.target.value)}
                                    placeholder="Search for new image" 
                                />
                            </Col>
                            <Col>
                                <Button onClick={() => setWord("")} variant="primary" type="submit">Search</Button>
                            </Col>
                        </Form.Group>
                    </Form>
                </Col>
            </Row>
        </Container>
    );
};

export default Search;