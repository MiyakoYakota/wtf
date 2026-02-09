USE [WebApp]
GO

/****** Object:  Table [dbo].[users] ******/
SET ANSI_NULLS ON
GO

CREATE TABLE [dbo].[users](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[email] [nvarchar](255) NOT NULL,
	[username] [nvarchar](100) NULL,
	[password] [nvarchar](255) NOT NULL,
	[name] [nvarchar](200) NULL,
PRIMARY KEY CLUSTERED ([id] ASC)
)
GO

INSERT [dbo].[users] ([id], [email], [username], [password], [name]) VALUES (1, N'alice@example.com', N'alice', N'hunter2', N'Alice Smith')
GO
INSERT [dbo].[users] ([id], [email], [username], [password], [name]) VALUES (2, N'bob@example.com', N'bob_jones', N'p@ssw0rd', N'Bob Jones')
GO
INSERT [dbo].[users] ([id], [email], [username], [password], [name]) VALUES (3, N'charlie@test.org', N'charlie', N'qwerty123', N'Charlie Brown')
GO
