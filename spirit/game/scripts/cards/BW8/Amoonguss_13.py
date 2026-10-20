from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="655d3016-30d4-5c53-9fef-eead32738dbf",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Amoonguss.Name",
    display_name="Amoonguss",
    searchable_by=["Amoonguss", "Stage 1", "Team Plasma", "Amoonguss"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=13,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name",
    family_id=590,
    abilities=[
        Attack(
            title="Astonish",
            game_text="Flip a coin. If heads, choose a random card from your opponent's hand. Your opponent reveals that card and shuffles it into his or her deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Miracle Powder",
            game_text="Flip a coin. If heads, choose a Special Condition. The Defending Pok\u00e9mon is now affected by that Special Condition.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)