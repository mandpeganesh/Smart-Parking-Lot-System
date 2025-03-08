```mermaid
graph TD
    %% Client Applications
    subgraph "Client Applications"
        MobileApp["Mobile App"]
        KioskSystem["Entry/Exit Kiosk"]
        AdminPortal["Admin Portal"]
    end

    %% API Gateway
    subgraph "API Gateway"
        APIGateway["API Gateway / Load Balancer"]
    end

    %% Microservices
    subgraph "Microservices"
        ParkingMS["Parking Service"]
        AllocationMS["Spot Allocation Service"]
        VehicleMS["Vehicle Service"]
        TransactionMS["Transaction Service"]
        FeeMS["Fee Calculation Service"]
        PaymentMS["Payment Service"]
        ReportingMS["Reporting Service"]
        AuthService["Authentication Service"]
        LoggingMS["Logging & Monitoring Service"]
        CacheLayer["Cache (Redis)"]
    end

    %% Database
    subgraph "Database"
        DB[(Parking Database)]
    end

    %% External Systems
    subgraph "External Systems"
        PaymentGateway["Payment Gateway"]
        NotificationService["Notification Service"]
    end

    %% Client to API Gateway connections
    MobileApp --> APIGateway
    KioskSystem --> APIGateway
    AdminPortal --> APIGateway

    %% API Gateway to Microservices
    APIGateway --> ParkingMS
    APIGateway --> ReportingMS
    APIGateway --> AuthService

    %% Service Dependencies
    ParkingMS --> AllocationMS
    ParkingMS --> VehicleMS
    ParkingMS --> TransactionMS
    ParkingMS --> FeeMS
    ParkingMS --> PaymentMS
    ParkingMS --> CacheLayer

    %% Database connections
    AllocationMS --> DB
    VehicleMS --> DB
    TransactionMS --> DB
    FeeMS --> DB
    PaymentMS --> DB
    ReportingMS --> DB

    %% External Connections
    PaymentMS --> PaymentGateway
    TransactionMS --> NotificationService
    PaymentMS --> NotificationService

    %% Logging and Caching
    APIGateway --> LoggingMS
    ParkingMS --> LoggingMS
    TransactionMS --> LoggingMS
    ParkingMS --> CacheLayer
    TransactionMS --> CacheLayer
    FeeMS --> CacheLayer
