from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm12 import bubble_launcher_gx, splash_maker

card = PokemonCardDef(
    guid="82eafda2-83ff-5163-ac78-86dd48c66fd3",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlastoisePiplupGX.Name",
    display_name="Blastoise & Piplup-GX",
    searchable_by=["Blastoise & Piplup-GX", "Basic", "TAG TEAM", "GX", "BlastoisePiplupGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=214,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    hp=270,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=9,
    abilities=[
        Attack(
            title="Splash Maker",
            game_text="You may attach up to 3 Water Energy cards from your hand to your Pok\u00e9mon in any way you like. If you do, heal 50 damage from those Pok\u00e9mon for each card you attached to them in this way.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=splash_maker,
        ),
        Attack(
            title="Bubble Launcher-GX",
            game_text="Your opponent's Active Pok\u00e9mon is now Paralyzed. If this Pok\u00e9mon has at least 3 extra Water Energy attached to it (in addition to this attack's cost), this attack does 150 more damage. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=bubble_launcher_gx,
        ),
    ],
)