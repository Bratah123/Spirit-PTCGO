from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bcb8fcca-4e78-5119-8418-1276a2d53500",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MoltresEX.Name",
    display_name="Moltres-EX",
    searchable_by=["Moltres-EX", "Basic", "EX", "Team Plasma", "MoltresEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=14,
    set_code="BW8",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=146,
    abilities=[
        Attack(
            title="Destructive Flame",
            game_text="Flip a coin. If heads, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Power Flame",
            game_text="If this Pok\u00e9mon has any Plasma Energy attached to it, this attack does 40 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)