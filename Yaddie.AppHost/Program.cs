var builder = DistributedApplication.CreateBuilder(args);

var apiService = builder.AddProject<Projects.Yaddie_ApiService>("apiservice");

builder.AddProject<Projects.Yaddie_Web>("webfrontend")
    .WithExternalHttpEndpoints()
    .WithReference(apiService);

builder.Build().Run();
