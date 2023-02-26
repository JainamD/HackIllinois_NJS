//
//  LoginView.swift
//  SideQuest
//
//  Created by Siya Digra on 2/25/23.
//

import SwiftUI

struct LoginView: View {
    @State private var username: String = ""
    
    var body: some View {
        ZStack {
            Image("leafy_bg") // replace "your-background-image-name" with your actual image name
                            .resizable()
                            .aspectRatio(contentMode: .fill)
                            .edgesIgnoringSafeArea(.all)
            VStack {
                Text("Log into your Account")
                    .font(.largeTitle)
                    .fontWeight(.bold)
                    .padding(.bottom, 30)
                    .foregroundColor(.white)
                TextField("Username", text: $username)
                    .padding()
                    .background(Color.brown.opacity(0.8))
                    .cornerRadius(5.0)
                    .padding(.bottom, 20)
                    .frame(width: 250)
                    .accentColor(.white)
                    .fontWeight(.bold)
                Button(action: {
                    // Handle login logic here
                    loginUser()
                }) {
                    Text("Resume Questing")
                        .font(.title)
                        .fontWeight(.bold)
                        .padding(.horizontal, 50)
                        .padding(.vertical, 15)
                        .foregroundColor(.white)
                        .background(Color.green)
                        .cornerRadius(10)
                }
            }
            .padding()
        }
    }
    
    func loginUser() {
        // Define the endpoint URL for creating a new user
        let endpointUrl = URL(string: "http://localhost:8081/login")!

        // Define the request body
        let requestBody = ["user": username]
        print(requestBody)

        // Serialize the request body to JSON data
        let jsonEncoder = JSONEncoder()
        let requestData = try? jsonEncoder.encode(requestBody)

        // Create the request object
        var request = URLRequest(url: endpointUrl)
        request.httpMethod = "POST"
        request.httpBody = requestData
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
    
        let task = URLSession.shared.dataTask(with: request) { data, response, error in
            if let error = error {
                print("Error:",error)
            } else if let data = data {
                // Handle the response data
                let jsonDecoder = JSONDecoder()
                let responseDict = try? jsonDecoder.decode([String: String].self, from: data)
                print("Response: ", responseDict)
            }
        }
        task.resume()
    }
}

struct LoginView_Previews: PreviewProvider {
    static var previews: some View {
        LoginView()
    }
}
