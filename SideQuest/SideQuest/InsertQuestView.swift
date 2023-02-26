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
    @State private var isPresentingModal = false
    @State private var questName = ""
    @State private var questDescription = ""
    @State private var quests: [Quest] = []
    
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
                
                Button("Create Quest") {
                    quests.append(Quest(name: questName, description: questDescription))
                    isPresentingModal = false
                }
                .padding()
                .background(Color.blue)
                .foregroundColor(.white)
                .cornerRadius(10)
            }
            .padding()
        }
    }
}
