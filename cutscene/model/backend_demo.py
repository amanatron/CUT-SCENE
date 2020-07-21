import cutscene
import pickle
import json


# DEMO

#initialise the project
project = cutscene.CutSceneProject(name="Demo Project",
                                   description="my first project",
                                   genre="demo genre",
                                   author="Matthew Bowley")

# LEVELS
# make a new level, you can store the Level handle
level_1 = project.addLevel(name="the first level",
                           description="this is the first level created using CutScene!")
# or leave the handle...
project.addLevel(name="the second level",
                 description="another level has been added")
# and get them all back later! the .get() works with all "container" classes
levels = project.get()
print("levels: {}".format(levels))




# SUBLEVELS
# let's add a sublevel using the list of all our levels
level_2 = levels[1]
level_2_sub_1 = level_2.addSubLevel(name="a sublevel",
                                    description="the plot thickens...")
# and a scene to that sublevel
scene = level_2_sub_1.addScene(name="A Scene",
                               description="a cold, misty morning...")




# ANIMATION
# let's start the scene with an animation
animation = scene.addAnimation(name="an animation",
                               description="mark and ron meet")
# but first, we need some characters!
mark = project.characters.addCharacter(name="Mark", 
                                       description="The hero of our tale", 
                                       entityType="PLAYER")
ron = project.characters.addCharacter(name="Ron", 
                                      description="Mark's friend", 
                                      entityType="OTHER")
# and maybe a talking bench? idk ha
bench = project.objects.addObject(name="Bench", 
                                  description="A talking bench", 
                                  entityType="RESPONSIVE")
# Like levels, it's easy to get all the character objects using get()
characters = project.characters.get()
print("characters: {}".format(characters))
# let's introduce the animation
animation.addAct(description="Act 1, The Bench")
animation.addHeading(description="The first time mark and ron meet the bench")
animation.addAction(description="It's a cold and misty morning. Mark is walking through the park with his cold cup of coffee, when from through the mist, he hears the voice of his friend Ron...")
animation.addTransition(description="Fade in from black...")
# The order that things are added to the animation is stored, and the animation elements can be moved around
# Quick demo on moving stuff around
print("\nAnimation before moveUp(3) (look at the 'Fade in from black')")
for element in animation.get():
    print(element.description)
# Our transition is in the wrong place! we want to fade in from black before the action.
# so, we moveUp the element at index number 3
animation.moveUp(3)
print("\nAnimation after moveUp(3)")
for element in animation.get():
    print(element.description)
# let's add some dialogue
animation.addDialogue(character_name="Ron",
                      dialogue="Oh, hi Mark!", 
                      paranthetical="sees Mark walking towards him")
animation.addDialogue(character_name="Mark", 
                      dialogue="I did not hit her! I did not!", 
                      paranthetical="throws his coffee on the ground")
# Let's see the animation now
print("\nFinished animation")
for element in animation.get():
    if type(element) is cutscene.sceneElements.animation.Dialogue: # TODO: Nicer way of telling the types of object returned? Maybe every element has a dict() method that comes with descriptive keys?
        print("{} ({}): {}".format(element.character_name, element.paranthetical, element.dialogue))
    else:
        print(element.description)
print("\nanimation.get() now gives us: {}".format(animation.get()))


print("\n\n\n")

cutscene.saveProject(project, "project.cutscene")

# print(project)
# print(project.characters.get()[0].name)
# print(project.characters.get()[0].description)

# SAVE/LOAD FUNCTIONALITY
# print("\n\nNow going to demonstrate saving and loading the project")
# x = pickle.dumps(project)
# print("\nFirst, serialise the CutSceneProject instance, giving this string:\n")
# print(x)
# print("\nNow we delete the project instance")
# del project
# try:
#     print(project)
# except NameError as e:
#     print(e)
# print("it's gone!")
# print("\nNow we can recreate the entire project from the serialised string (above)")
# project = pickle.loads(x)
# print("\nAnd voila, our project is fully restored")
