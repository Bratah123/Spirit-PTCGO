from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import magma_ring_no_retreat


card = PokemonCardDef(
    guid="a6968703-43dd-5fc2-b9c5-d2d0904151dc",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name",
    display_name="Trapinch δ",
    searchable_by=["Trapinch \u03b4", "Basic", "Trapinch"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="EX13",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=328,
    abilities=[
        Attack(
            title="Big Bite",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=magma_ring_no_retreat(),
        ),
        Attack(
            title="Mud Slap",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)