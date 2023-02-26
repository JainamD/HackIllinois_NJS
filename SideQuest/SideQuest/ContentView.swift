import SwiftUI

struct ContentView: View {
    @State private var register: Bool = false
    
    var body: some View {
        VStack {
            Text("Welcome to \nSide Quest!")
                .font(.largeTitle)
                .fontWeight(.bold)
                .padding(.bottom, 30)
            Image("logo")
                .resizable()
                .scaledToFit()
                .frame(width: 200, height: 200)
                .padding(.bottom, 30)
            Button("Register") {
                        self.register = true
                    }.sheet(isPresented: $register, content: {
                        RegisterView()
                    })
           // NavigationLink(destination: MainMenuView()) {
//                Button(action: {
//                    start = true
//                }) {
//                    Text("Start")
//                        .font(.title)
//                        .fontWeight(.bold)
//                        .padding(.horizontal, 50)
//                        .padding(.vertical, 15)
//                        .foregroundColor(.white)
//                        .background(Color.blue)
//                        .cornerRadius(10)
//                }
           // }
        }
        .padding(.top, 100)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
