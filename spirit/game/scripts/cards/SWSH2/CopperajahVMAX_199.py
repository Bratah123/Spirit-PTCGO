from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, active_is
from spirit.game.session.effects import is_basic_pokemon

card = PokemonCardDef(
    guid="78daab62-dde9-56f0-88dc-add9f0870d3a",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CopperajahVMAX.Name",
    display_name="Copperajah VMAX",
    searchable_by=["Copperajah VMAX", "VMAX", "CopperajahVMAX"],
    subtypes=["VMAX"],
    collector_number=199,
    set_code="SWSH2",
    rarity=Rarities.RareRainbow,
    hp=340,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.VMAX,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CopperajahV.Name",
    family_id=879,
    abilities=[
        Attack(
            title="Dangerous Nose",
            game_text="If your opponent's Active Pok\u00e9mon is a Basic Pok\u00e9mon, this attack does 100 more damage.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=bonus_if(active_is(is_basic_pokemon), 100),
        ),
        Attack(
            title="G-Max Hammer",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=240,
        ),
    ],
)