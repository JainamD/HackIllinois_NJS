import SwiftUI

struct MainMenuView: View {
    var body: some View {
        VStack {
            Text("Main Menu")
                .font(.largeTitle)
                .fontWeight(.bold)
                .padding(.bottom, 30)
        }
    }
}

struct MainMenuView_Previews: PreviewProvider {
    static var previews: some View {
        MainMenuView()
    }
}
