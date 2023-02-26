//
//  HomeView.swift
//  SideQuest
//
//  Created by Nishka Awasthi on 2/26/23.
//

import SwiftUI

struct HomeView: View {
    @State private var register: Bool = false
    @State private var login: Bool = false
    @State var username: String
    
    var body: some View {
        ZStack {
            Image("other_tree_bg") // replace "your-background-image-name" with your actual image name
                            .resizable()
                            .aspectRatio(contentMode: .fill)
                            .edgesIgnoringSafeArea(.all)
            VStack {
//                Text("Welcome to \nSide Quest!")
//                    .font(.largeTitle)
//                    .fontWeight(.bold)
//                    .padding(.bottom, 30)
                Image("sidequestlogo2")
                    .resizable()
                    .scaledToFit()
                    .frame(width: 200, height: 400)
                    .padding(.bottom, 20)
                    .padding(.top, -450)
                Button("Receive Quest") {
                    self.login = true
                }.font(.title)
                    .fontWeight(.bold)
                    .padding(.horizontal, 50)
                    .padding(.vertical, 15)
                    .foregroundColor(.white)
                    .background(Color.green)
                    .cornerRadius(10)
                    .sheet(isPresented: $login, content: {
                    LoginView()
                })
                Button("Add New Goals") {
                    self.register = true
                }.font(.title)
                    .fontWeight(.bold)
                    .padding(.horizontal, 50)
                    .padding(.vertical, 15)
                    .foregroundColor(.white)
                    .background(Color.green)
                    .cornerRadius(10)
                    .sheet(isPresented: $register, content: {
                    InsertQuestView(username: username)
                })
                Button("How to use") {
                    self.register = true
                }.font(.title)
                    .fontWeight(.bold)
                    .padding(.horizontal, 50)
                    .padding(.vertical, 15)
                    .foregroundColor(.white)
                    .background(Color.green)
                    .cornerRadius(10)
                    .sheet(isPresented: $register, content: {
                    RegisterView()
                })
            }
            .padding(.top, 100)
        }
    }
}

struct HomeView_Previews: PreviewProvider {
    static var previews: some View {
        HomeView(username:"")
    }
}
