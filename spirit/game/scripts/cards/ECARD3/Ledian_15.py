from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import pollen_shield, swift


card = PokemonCardDef(
    guid="74a73ef5-c17f-5871-bbc2-698c2f81d56a",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ledian.Name",
    display_name="Ledian",
    searchable_by=["Ledian", "Stage 1", "Ledian"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="ECARD3",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ledyba.Name",
    family_id=165,
    abilities=[
        Attack(
            title="Pollen Shield",
            game_text="During your opponent's next turn, Ledian can't become affected by a Special Condition. (Any other effects of attacks, Pok\u00e9-Powers, Pok\u00e9-Bodies, and Trainer cards still happen.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=pollen_shield,
        ),
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=swift,
        ),
    ],
)
