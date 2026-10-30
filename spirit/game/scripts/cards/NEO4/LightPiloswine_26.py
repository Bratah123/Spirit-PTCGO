from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import fluffy_wool, knock_over


card = PokemonCardDef(
    guid="d78afa19-9dc3-57cc-b1ed-0cab2c9f4301",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightPiloswine.Name",
    display_name="Light Piloswine",
    searchable_by=["Light Piloswine", "Stage 1", "LightPiloswine"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swinub.Name",
    family_id=220,
    abilities=[
        Ability(
            title="Fluffy Wool",
            game_text="During your opponent's turn, if Light Piloswine is your Active Pok\u00e9mon and is damaged by your opponent's attack (even if it's Knocked Out), flip a coin. If heads, the attacking Pok\u00e9mon is now Asleep. This power stops working if Light Piloswine is already Asleep, Confused, or Paralyzed when your opponent attacks.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=fluffy_wool,
        ),
        Attack(
            title="Knock Over",
            game_text="If there is a Stadium card in play, you may discard it.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=knock_over,
        ),
    ],
)
