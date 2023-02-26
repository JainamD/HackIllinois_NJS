//
//  RegisterView.swift
//  SideQuest
//
//  Created by Siya Digra on 2/25/23.
//

import SwiftUI

struct RegisterView: View {
    @State private var username = ""
    @State private var showSuccessAlert = false
    @State private var showErrorAlert = false
    @State private var errorMessage = ""

    var body: some View {
        ZStack {
            Image("wood_grain") // replace "your-background-image-name" with your actual image name
                            .resizable()
                            .aspectRatio(contentMode: .fill)
                            .edgesIgnoringSafeArea(.all)
            VStack {
                Text("Create my account")
                    .font(.largeTitle)
                    .fontWeight(.bold)
                    .padding(.top, 20)
                    .padding(.bottom, 30)
                    .foregroundColor(.white)

                TextField("My Unique Username", text: $username)
                    .padding()
                    .background(Color.green.opacity(0.2))
                    .cornerRadius(5.0)
                    .padding(.bottom, 20)
                    .frame(width: 250)
                    .accentColor(.white)
                    .fontWeight(.bold)
                    

                Button(action: {
                    // Handle registration logic here
                    registerUser()
                }) {
                    Text("Start Questing")
                        .font(.title)
                        .fontWeight(.bold)
                        .padding(.horizontal, 50)
                        .padding(.vertical, 15)
                        .foregroundColor(.white)
                        .background(Color.green)
                        .cornerRadius(10)
                    
                }
            }
            //.background(Color.brown.opacity(0.9))
            //.overlay(RoundedRectangle(cornerRadius: 5.0).stroke(Color.white, lineWidth: 3))
            .padding()
        }
    }
    
    func registerUser() {
        // Define the endpoint URL for creating a new user
        let endpointUrl = URL(string: "http://localhost:8081/register")!

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
                InsertQuestView(username: username)
            }
        }
        task.resume()
    }
}

struct RegisterView_Previews: PreviewProvider {
    static var previews: some View {
        RegisterView()
    }
}
