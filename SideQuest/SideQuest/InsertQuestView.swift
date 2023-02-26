//
//  InsertQuestView.swift
//  SideQuest
//
//  Created by Siya Digra on 2/25/23.
//

import SwiftUI

struct Quest: Identifiable {
    let id = UUID()
    let name: String
    let description: String
}

struct QuestCardView: View {
    let quest: Quest
    
    var body: some View {
        VStack(alignment: .leading) {
            Text(quest.name)
                .font(.headline)
            Text(quest.description)
                .font(.subheadline)
        }
        .padding()
        .background(Color.white)
        .cornerRadius(10)
        .shadow(radius: 5)
    }
}

struct InsertQuestView: View {
    @State var username: String
    
    @State private var isPresentingModal = false
    @State private var questName: String = ""
    @State private var questDescription: String = ""
    @State private var quests: [Quest] = []
    
    @State private var isHappy: Bool = false
    @State private var isSad: Bool = false
    @State private var isTired: Bool = false
    @State private var isMotivated: Bool = false
    @State private var isBored: Bool = false
    @State private var isHungry: Bool = false
    
    let minutes = Array(stride(from: 5, to: 61, by: 5))
    @State private var selectedMinuteIndex = 0
        
    var body: some View {
        VStack {
            Button(action: {
                isPresentingModal = true
            }) {
                Image(systemName: "plus")
                    .font(.system(size: 30))
                    .foregroundColor(.white)
            }
            .frame(width: 50, height: 50)
            .background(Color.blue)
            .clipShape(Circle())
            .padding(.bottom, 30)
            
            ForEach(quests) { quest in
                QuestCardView(quest: quest)
            }
            
            Spacer()
        }
        .padding()
        .sheet(isPresented: $isPresentingModal) {
            VStack(spacing: 20) {
                TextField("Enter quest name", text: $questName)
                    .padding()
                    .background(Color.gray.opacity(0.1))
                    .cornerRadius(10)
                
                TextField("Enter quest description", text: $questDescription)
                    .padding()
                    .background(Color.gray.opacity(0.1))
                    .cornerRadius(10)
                
                Text("In what mood would you be best able to accomplish this task?")
                
                Group {
                    Toggle(isOn: $isHappy) {
                        Text("Happy")
                    }
                    .toggleStyle(iOSCheckboxToggleStyle())
                    
                    Toggle(isOn: $isSad) {
                        Text("Sad")
                    }
                    .toggleStyle(iOSCheckboxToggleStyle())
                    
                    Toggle(isOn: $isTired) {
                        Text("Tired")
                    }
                    .toggleStyle(iOSCheckboxToggleStyle())
                    
                    Toggle(isOn: $isMotivated) {
                        Text("Motivated")
                    }
                    .toggleStyle(iOSCheckboxToggleStyle())
                    
                    Toggle(isOn: $isBored) {
                        Text("Bored")
                    }
                    .toggleStyle(iOSCheckboxToggleStyle())
                    
                    Toggle(isOn: $isHungry) {
                        Text("Hungry")
                    }
                    .toggleStyle(iOSCheckboxToggleStyle())
                }
                
                Text("Select a duration for this quest:")
                Picker("Duration", selection: $selectedMinuteIndex) {
                    ForEach(0 ..< minutes.count) {
                        Text("\(self.minutes[$0]) minutes")
                    }
                }
                .pickerStyle(MenuPickerStyle())
                .padding()

                Button("Create Quest") {
                    createQuest()
                    quests.append(Quest(name: questName, description: questDescription))
                    isPresentingModal = false
                    questName = ""
                    questDescription = ""
                    isHappy = false
                    isSad = false
                    isTired = false
                    isMotivated = false
                    isBored = false
                    isHungry = false
                    selectedMinuteIndex = 0
                }
                .padding()
                .background(Color.blue)
                .foregroundColor(.white)
                .cornerRadius(10)
            }
            .padding()
        }
    }
    
    func createQuest() {
        // Define the endpoint URL for creating a new user
        let endpointUrl = URL(string: "http://localhost:8081/add_quest")!

        // Define the request body
        let requestBody: [String: Any] = [
              "name": questName,
              "desc": questDescription,
              "happy": isHappy,
              "sad": isSad,
              "tired": isTired,
              "motv": isMotivated,
              "bored": isBored,
              "hungy": isHungry,
              "mins": 5*($selectedMinuteIndex.wrappedValue+1),
              "finish": 0,
              "user": username
          ]
        
        print(requestBody)

        var request = URLRequest(url: endpointUrl)
        request.httpMethod = "POST"
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
        
        // Encode the quest data in the request body
        do {
            request.httpBody = try JSONSerialization.data(withJSONObject: requestBody)
        } catch let error {
            print("Failed to encode quest data:", error)
            return
        }
        
        // Send the request to the server
        let task = URLSession.shared.dataTask(with: request) { data, response, error in
            if let error = error {
                print("Error sending request: \(error.localizedDescription)")
                return
            }
            if let response = response as? HTTPURLResponse {
                if let responseData = data, let responseString = String(data: responseData, encoding: .utf8) {
                    print("Server response: \(response.statusCode)\n\(responseString)")
                } else {
                    print("Empty response from server")
                }
                if response.statusCode != 200 {
                    print("Failed to create quest. HTTP status code: \(response.statusCode)")
                } else {
                    print("Quest created successfully!")
                }
            } else {
                print("Invalid response from server")
            }
        }
        task.resume()
    }
}

struct iOSCheckboxToggleStyle: ToggleStyle {
    func makeBody(configuration: Configuration) -> some View {
        // 1
        Button(action: {

            // 2
            configuration.isOn.toggle()

        }, label: {
            HStack {
                // 3
                Image(systemName: configuration.isOn ? "checkmark.square" : "square")

                configuration.label
            }
        })
    }
}
