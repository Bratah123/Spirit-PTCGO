from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm4 import submerge_passive

card = PokemonCardDef(
    guid="9ecb3c0f-77de-552b-9ead-69912893b831",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    display_name="Feebas",
    searchable_by=["Feebas", "Basic", "Feebas"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="DM",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=349,
    abilities=[
        Ability(
            title="Submerge",
            game_text="As long as this Pok\u00e9mon is on your Bench, prevent all damage done to this Pok\u00e9mon by attacks (both yours and your opponent's).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=submerge_passive,
        ),
        Attack(
            title="Rain Splash",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)