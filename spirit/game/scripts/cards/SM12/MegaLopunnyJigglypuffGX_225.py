from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm12 import jumping_balloon, puffy_smashers_gx

card = PokemonCardDef(
    guid="4bf24f20-a014-5123-bc8e-7333d8c3a58a",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaLopunnyJigglypuffGX.Name",
    display_name="Mega Lopunny & Jigglypuff-GX",
    searchable_by=["Mega Lopunny & Jigglypuff-GX", "Basic", "TAG TEAM", "GX", "MegaLopunnyJigglypuffGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=225,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    hp=240,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=39,
    abilities=[
        Attack(
            title="Jumping Balloon",
            game_text="This attack does 60 more damage for each of your opponent's Pok\u00e9mon-GX and Pok\u00e9mon-EX in play.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=jumping_balloon,
        ),
        Attack(
            title="Puffy Smashers-GX",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep. If this Pok\u00e9mon has at least 4 extra Energy attached to it (in addition to this attack's cost), this attack does 200 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=puffy_smashers_gx,
        ),
    ],
)