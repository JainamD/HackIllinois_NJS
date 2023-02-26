import SwiftUI

struct ContentView: View {
    @State private var register: Bool = false
    @State private var login: Bool = false
    
    var body: some View {
        ZStack {
            Image("sidequestbackground") // replace "your-background-image-name" with your actual image name
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
                    .frame(width: 400, height: 400)
                    .padding(.bottom, 30)
                Button("Login") {
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
                Button("Register") {
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

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
