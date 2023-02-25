import SwiftUI

struct ContentView: View {
    @State private var selection: String? = nil
    
    var body: some View {
        VStack {
            Text("Side Quest")
                .font(.largeTitle)
                .fontWeight(.bold)
                .padding(.bottom, 30)
            Image("logo")
                .resizable()
                .scaledToFit()
                .frame(width: 200, height: 200)
                .padding(.bottom, 30)
            NavigationLink(destination: MainMenuView(), tag: "mainMenu", selection: $selection) {
                Button(action: {
                    self.selection = "mainMenu"
                }) {
                    Text("Start")
                        .font(.title)
                        .fontWeight(.bold)
                        .padding(.horizontal, 50)
                        .padding(.vertical, 15)
                        .foregroundColor(.white)
                        .background(Color.blue)
                        .cornerRadius(10)
                }
            }
        }
        .padding(.top, 100)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
