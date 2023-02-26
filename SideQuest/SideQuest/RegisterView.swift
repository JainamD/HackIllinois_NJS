//
//  RegisterView.swift
//  SideQuest
//
//  Created by Siya Digra on 2/25/23.
//

import SwiftUI

struct RegisterView: View {
    @State private var username: String = ""

    var body: some View {
        VStack {
            Text("Sign up")
                .font(.largeTitle)
                .fontWeight(.bold)
                .padding(.bottom, 30)
            TextField("Username", text: $username)
                .padding()
                .background(Color.gray.opacity(0.2))
                .cornerRadius(5.0)
                .padding(.bottom, 20)
            Button(action: {
                // Handle registration logic here
            }) {
                Text("Register")
                    .font(.headline)
                    .foregroundColor(.white)
                    .padding()
                    .frame(maxWidth: .infinity)
                    .background(Color.blue)
                    .cornerRadius(5.0)
            }
        }
        .padding()
    }
}

struct RegisterView_Previews: PreviewProvider {
    static var previews: some View {
        RegisterView()
    }
}
