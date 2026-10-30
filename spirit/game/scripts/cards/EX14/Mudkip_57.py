from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import submerge_all_attacks_passive

card = PokemonCardDef(
    guid="f2836d70-ce95-5ba8-ac4e-271735008c06",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mudkip.Name",
    display_name="Mudkip",
    searchable_by=["Mudkip", "Basic", "Mudkip"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="EX14",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=258,
    abilities=[
        Ability(
            title="Submerge",
            game_text="As long as Mudkip is on your Bench, prevent all damage done to Mudkip by attacks (both yours and your opponent's).",
            ability_type=AbilityTypes.POKE_BODY,
            passive=submerge_all_attacks_passive(),
            effect=None,
        ),
        Attack(
            title="Mud Slap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)