from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="48c3cadc-785c-57a6-a17b-3d33b36f512f",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CoalossalV.Name",
    display_name="Coalossal V",
    searchable_by=["Coalossal V", "Basic", "V", "CoalossalV"],
    subtypes=["Basic", "V"],
    collector_number=98,
    set_code="SWSH4",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=839,
    abilities=[
        Attack(
            title="Searing Flame",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Boulder Crush",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
        ),
    ],
)