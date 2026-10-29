from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm6 import sticky_membrane_passive

card = PokemonCardDef(
    guid="6d9a9a21-781e-5fb4-9ee8-06a1c2c0a703",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Goomy.Name",
    display_name="Goomy",
    searchable_by=["Goomy", "Basic", "Goomy"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=704,
    abilities=[
        Ability(
            title="Sticky Membrane",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, your opponent's Pok\u00e9mon's attacks cost Colorless more.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=sticky_membrane_passive,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
        ),
    ],
)
